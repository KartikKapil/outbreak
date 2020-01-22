from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .APIs import chronic
from accounts.models import Patient
from .apiaccess import *

@login_required
def search(request):
    if request.POST:
        return redirect('list_hospitals', {'data': request.POST['data']})
    else:
        return render(request, 'list_hospitals/search.html', {})


@login_required
def list_hospitals(request, data):
    if not data:
        # Generate all nearby facilities
        hospitals = chronic(28.6358749, 77.3738937)
    else:
        # Generate Customised facilities
        hospitals = chronic(28.6358749, 77.3738937)
    return render(request, 'list_hospitals/index.html', {'hospitals': hospitals })
########################################################################################
data = []
auth_string = "33e7b86d:1c80f2d4577c86270a5c69f560068804"
new_evidence = []
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
    sex = user.gender
    global mentions
    if not request.POST:
        def read_complaints(auth_string, case_id, language_model=None):
            """Keep reading complaint-describing messages from user until empty message read (or just read the story if given).
            Will call the /parse endpoint and return mentions captured there."""
            global data
            
            # print(data)
            context = []  # a list of ids of present symptoms in the order of reporting
            for i in range(len(data)):
                portion = call_parse(data[i], auth_string, case_id, context, language_model=language_model).get(
                    'mentions', [])
                if portion:
                    # summarise_mentions(portion)
                    mentions.extend(portion)
                    # remember the mentions understood as context for next /parse calls
                    #context.extend(context_from_mentions(portion))
                    context.extend([m['id'] for m in mentions if m['choice_id'] == 'present'])

                    # user said there's nothing more but we've already got at least one complaint
            # print(mentions)
            return mentions
        mentions = read_complaints(auth_string, case_id, language_model=None)

    def conduct_interview(evidence, age, sex, case_id, auth, language_model=None):
        """Keep asking questions until API tells us to stop or the user gives an empty answer."""

        resp = call_diagnosis(evidence, age, sex, case_id, auth, language_model=language_model)
        question_struct = resp['question']
        diagnoses = resp['conditions']
        should_stop_now = resp['should_stop']
        if should_stop_now:
            # triage recommendation must be obtained from a separate endpoint, call it now
            # and return all the information together
            triage_resp = call_triage(evidence, age, sex, case_id, auth, language_model=language_model)
            return redirect("list_hospital/" + str(diagnoses) + '/' + str(triage_resp))
        if question_struct['type'] == 'single':
            # if you're calling /diagnosis in "disable_groups" mode, you'll only get "single" questions
            # these are simple questions that require a simple answer --
            # whether the observation being asked for is present, absent or unknown
            question_items = question_struct['items']
            assert len(question_items) == 1  # this is a single question
            question_item = question_items[0]
            observation_value = answer_norm[request.post.ans]
            # render(request,'')
            if observation_value is not None:
                new_evidence.extend(question_answer_to_evidence(question_item, observation_value))

                return diagnosis, question_item
        # else:
        #     # You'd need a rich UI to handle group questions gracefully.
        #     # There are two types of group questions: "group_single" (radio buttons)
        #     # and "group_multiple" (a bunch of single questions gathered under one caption).
        #     # Actually you can try asking sequentially for each question item from "group_multiple" question
        #     # and then adding the evidence coming from all these answers.
        #     # For "group_single" there should be only one present answer. It's recommended to include only this chosen
        #     # answer as present symptom in the new evidence.
        #     # For more details, please consult:
        #     # https://developer.infermedica.com/docs/diagnosis#group_single
        #     raise NotImplementedError('Group questions not handled in this example')
        # important: always update the evidence gathered so far with the new answers
        evidence.extend(new_evidence)
    # print(mentions)
    evidence = mentions_to_evidence(mentions)
    # print(evidence)
    diagnosis, question_item = conduct_interview(evidence, age, sex, case_id, auth_string)
    return render(request, 'list_hospitals/interview.html', {'questions': question_item})




def take_symptoms(request):
    if request.POST:
        print(request.POST)
        data.append(request.POST['ans'])  # redirect to question page
        return redirect("confirmation")
    return render(request,'list_hospitals/complaints.html')


def confirmation(request):

    return render(request, 'list_hospitals/confirmation.html')

















