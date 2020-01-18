from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import Patient, Hospital
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
    return render(request, 'accounts/patient/signup.html', {'userForm': userForm, 'patientForm': patientForm})

def signup_h(request):
    if(request.POST):
        userForm = UserForm(request.POST)
        hospitalForm = HospitalForm(request.POST)
        if userForm.is_valid() and hospitalForm.is_valid():
            # Save User
            user = userForm.save(commit=False)
            user.user_type = 'H'
            user.save()
            specialities=hospitalForm.cleaned_data.get('specialities')

            # Save Patient
            patient = hospitalForm.save(commit=False)
            patient.user = user
            patient.save()
            redirect('home')
    else:
        userForm = UserForm()
        hospitalForm = HospitalForm()
    return render(request, 'accounts/hospital/signup.html', {'userForm': userForm, 'hospitalForm': hospitalForm})
    pass

@login_required
def patient_dashboard(request):
    user_info = Patient.objects.get(user = request.user)
    return render(request, 'accounts/patient/dashboard.html', {'User': user_info})

@login_required
def hospital_dashboard(request):
    user_info = Hospital.objects.get(user = request.user)
    return render(request, 'accounts/hospital/dashboard.html', {'User': user_info})
