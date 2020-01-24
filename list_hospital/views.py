from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .APIs import find_place, check
from accounts.models import Patient
# from .apiaccess import *
from .chatbot import *
import json

@login_required
def search(request):
    if request.POST:
        return redirect('list_hospitals', {'data': request.POST['data']})
    else:
        return render(request, 'list_hospitals/search.html', {})


@login_required
def list_hospitals(request, disease):
    if disease:
        # Generate all nearby facilities'
        print(disease[10:-2])
        # print(request.GET)
        hospitals = check(str(disease[10:-2]), 28.630999, 77.372165)
    else:
        # Generate Customised facilities
        hospitals = find_place(28.6358749, 77.3738937, ['clinic'])
    return render(request, 'list_hospitals/index.html', {'hospitals': hospitals })

complaints = []
auth_string = "33e7b86d:1c80f2d4577c86270a5c69f560068804"
evidence = []
mentions = []

@login_required
def interview(request):
    user = Patient.objects.get(user=request.user)
    case_id = user.id
    age = user.age
    sex = "male"
    question_item = "Init question?"
    global mentions
    global evidence
    global complaints
    if not request.POST:
        mentions, evidence, question_item = read_complaints(complaints, evidence, age, sex, auth_string, case_id, language_model=None)
    if request.POST:
        diagnosis, question_item, evidence = conduct_interview(evidence, request.POST['ans'], age, sex, case_id, auth_string)
        if(question_item == None):
            return redirect('list_hospitals', disease = (str(diagnosis[0]['name']),))
    return render(request, 'list_hospitals/interview.html', {'question': question_item})


def take_symptoms(request):
    if request.POST:
        complaints.append(request.POST['ans'])
        return redirect("confirmation")
    return render(request,'list_hospitals/complaints.html')


def confirmation(request):
    return render(request, 'list_hospitals/confirmation.html')

















