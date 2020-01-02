from django import forms
from list_hospital.models import Patient_name,Hospital_Name

class Hospital_Nameform(forms.ModelForm):
    name=forms.CharField(help_text="Enter the name of hospital")
    pass_word=forms.CharField(widget=forms.PasswordInput,help_text="Enter the password")
    address = forms.CharField(help_text="Enter the address")
    bed_capacity = forms.IntegerField(help_text="Enter the current bed capacity of the hospital ")
    currently_free = forms.IntegerField(help_text="Enter the number of bed free in the hospital")
    user_id = forms.CharField(help_text="Enter your new user id ")

    class Meta:
        model=Hospital_Name
        fields= ('name','pass_word','address','bed_capacity','currently_free','user_id')

class Patient_nameform(forms.ModelForm):
    name = forms.CharField(max_length=250)
    age = forms.IntegerField(default=None)
    Gender = (('Male', 'M'), ('Female', 'F'), ('Others', 'O'),)  # selection of gender
    gender = forms.CharField(widget=forms.Select(choices=Gender))
    contact_no = forms.IntegerField(unique=True, blank=False)
    Social_Status = (('SC', 'SC'), ('Gen', 'Gen'), ('ST', 'ST'), ('OBC', 'OBC'),)
    social_status = forms.CharField(widget=forms.Select(choices=Social_Status))
    user_id = forms.CharField(max_length=100, blank=False)
    pass_word = forms.CharField(widget=forms.PasswordInput)
    Prefferd_hospital = forms.CharField(max_length=100)

    class Meta:
        model = Patient_name
        fields = ('name', 'age', 'gender', 'contact_no', 'social_status', 'user_id', 'pass_word', 'Prefferd_hospital')