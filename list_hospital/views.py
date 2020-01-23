from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .APIs import chronic, check
from accounts.models import Patient
from .apiaccess import *
from .new_conversation import *

@login_required
def search(request):
    if request.POST:
        return redirect('list_hospitals', {'data': request.POST['data']})
    else:
        return render(request, 'list_hospitals/search.html', {})


@login_required
def list_hospitals(request, disease):
    if not disease:
        # Generate all nearby facilities
        hospitals = check(str(disease), 28.6358749, 77.3738937)
    else:
        # Generate Customised facilities
        hospitals = chronic(28.6358749, 77.3738937)
    return render(request, 'list_hospitals/index.html', {'hospitals': hospitals })

########################################################################################

data = []
auth_string = "33e7b86d:1c80f2d4577c86270a5c69f560068804"
evidence = []
mentions = []
answer_norm = {
    'yes': 'present',
    'y': 'present',
    'present': 'present',
    'no': 'absent',
    'n': 'absent',
    'absent': 'absent',
    '?': 'unknown',
    'skip': 'unknown',
    'unknown': 'unknown',
    'dont know': 'unknown',
    'sí': 'present',
    'si': 'present',
    'no lo sé': 'unknown',
    'no lo se': 'unknown',
    'omitir': 'unknown',
    'omita': 'unknown',
    'salta': 'unknown',
}

@login_required
def interview(request):
    user = Patient.objects.get(user=request.user)
    case_id = user.id
    age = user.age
    sex = "male"
    question_item = "Init question?"
    global mentions
    global evidence
    global data
    if not request.POST:
        def read_complaints(complaints, auth_string, case_id, language_model=None):
            """Keep reading complaint-describing messages from user until empty message read (or just read the story if given).
            Will call the /parse endpoint and return mentions captured there."""
            context = []  # a list of ids of present symptoms in the order of reporting
            for i in range(len(complaints)):
                portion = call_parse(complaints[i], auth_string, case_id, context, language_model=language_model).get(
                    'mentions', [])
                if portion:
                    mentions.extend(portion)
                    # remember the mentions understood as context for next /parse calls
                    context.extend([m['id'] for m in mentions if m['choice_id'] == 'present'])
            evidence.extend(mentions_to_evidence(mentions))
            question_item = diagnose(age, sex, evidence)['question']['text']
            return mentions
        mentions = read_complaints(complaints, auth_string, case_id, language_model=None)

    def conduct_interview(evidence, age, sex, case_id, auth, language_model=None):
        """Keep asking questions until API tells us to stop or the user gives an empty answer."""
        resp = diagnose(age, sex,evidence)
        question_struct = resp['question']
        diagnosis = resp['conditions']
        should_stop_now = resp['should_stop']
        if should_stop_now:
            # triage recommendation must be obtained from a separate endpoint, call it now
            # and return all the information together
            # triage to be implemented in the future
            # triage_resp = call_triage(evidence, age, sex, case_id, auth, language_model=language_model)
            return diagnosis, None
        if question_struct['type'] == 'single':
            question_items = question_struct['items']
            assert len(question_items) == 1  # this is a single question
            question_item = question_items[0]
            observation_value = answer_norm[request.POST['ans']]
            # render(request,'')
            if observation_value is not None:
                evidence.extend(question_answer_to_evidence(question_item, observation_value))
        return diagnosis, question_struct['text']
    if request.POST:
        diagnosis, question_item = conduct_interview(evidence, age, sex, case_id, auth_string)
        if(question_item == None):
            return redirect('list_hospitals', disease = (str(diagnosis[0]['name']),))
    return render(request, 'list_hospitals/interview.html', {'question': question_item})


def take_symptoms(request):
    if request.POST:
        data.append(request.POST['ans'])
        return redirect("confirmation")
    return render(request,'list_hospitals/complaints.html')


def confirmation(request):
    return render(request, 'list_hospitals/confirmation.html')

















