from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, PatientForm, HospitalForm

def signup_p(request):
    if(request.POST):
        userForm = UserForm(request.POST)
        patientForm = PatientForm(request.POST)
        print(userForm.is_valid())
        if userForm.is_valid() and patientForm.is_valid():
            print("Valid toh hai")
            # Save User
            userF = userForm.save(commit=False)
            userF.user_type = 'P'
            userF.save()
            id = userForm.cleaned_data.get('user_id')
            password = userForm.cleaned_data.get('password')
            user = authenticate(user_id = id, password = password)
            login(request, user)

            # Save Patient
            patient = patientForm.save(commit=False)
            patient.user = userF
            patient.save()
            redirect('home')


    else:
        userForm = UserForm()
        patientForm = PatientForm()
    return render(request, 'accounts/signup_p.html', {'userForm': userForm, 'patientForm': patientForm})

def signup_h(request):
    pass
