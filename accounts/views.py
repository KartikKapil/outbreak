from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import UserForm, PatientForm, HospitalForm

def signup_p(request):
    if(request.POST):
        userForm = UserForm(request.POST)
        patientForm = PatientForm(request.POST)
        if userForm.is_valid() and patientForm.is_valid():
            # Save User
            userF = userForm.save(commit=False)
            userF.user_type = 'P'
            userF.save()
            id = userForm.cleaned_data.get('user_id')
            password = userForm.cleaned_data.get('password')
            user = authenticate(user_id = id, password = password)
            login(request, userF)

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

@login_required
def dashboard(request):
    print(request.user)
    user_info = Patient.objects.get(user = request.user)
    print(user_info.name)
    return render(request, 'accounts/dashboard.html', {'User': user_info})
