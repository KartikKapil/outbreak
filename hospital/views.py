from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'P':
            return redirect('patient_dashboard')
        else :
            return redirect('hospital_dashboard')
    else:
        return redirect('login')
