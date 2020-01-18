from django import forms
from list_hospital.models import Patient_name,Hospital_Name

class Hospital_Nameform(forms.ModelForm):
    name=forms.CharField(help_text="Enter the name of hospital")
    pass_word=forms.CharField(widget=forms.PasswordInput,help_text="Enter the password")
    address = forms.CharField(help_text="Enter the address")
    bed_capacity = forms.IntegerField(help_text="Enter the current bed capacity of the hospital ")
    currently_free = forms.IntegerField(help_text="Enter the number of bed free in the hospital")
    user_id = forms.CharField(help_text="Enter your new user id ")
    differnt_options = (("Allergy & Clinical Immunology", "Allergy & Clinical Immunology"), ("Anaesthesia", "Anaesthesia"),
    ("Bariatric & Metabolic Surgery", "Bariatric & Metabolic Surgery"), ('Blood Disorders', 'Blood Disorders'), ("Breast Surgery", "Breast Surgery"),
    ("Cardiac Anaesthesia", "Cardiac Anaesthesia"), ("Cardiac Surgery", "Cardiac Surgery"),
    ("Cardiology", "Cardiology"), ("Cardiology - Interventional", "Cardiology - Interventional"),
    ("Dental Sciences", "Dental Sciences"), ("Dermatology", "Dermatology"),
    ("Diabetes And Endocrinology", "Diabetes And Endocrinology"),
    ("Dietetics & Clinical Nutrition", "Dietetics & Clinical Nutrition"), ("ENT", "ENT"),
    ("Geriatric Medicine", "Geriatric Medicine"),
    ("Ophthalmology", "Ophthalmology"), ("Foetal Medicine", "Foetal Medicine"),
    ("Gastroenterology", "Gastroenterology"), ("General Surgery", "General Surgery"),
    ("General and Laparoscopic Surgery", "General and Laparoscopic Surgery"),
    ("Gynaecology Oncology", "Gynaecology Oncology"),
    ("Infectious Diseases", "Infectious Diseases"), ("Infertility Medicine", "Infertility Medicine"),
    ("Intensive Care", "Intensive Care"), ("Internal Medicine", "Internal Medicine"),
    ("Interventional Radiology", "Interventional Radiology"), (
    "Laparoscopic, Gastro Intestinal, Bariatric & Metabolic Surgery",
    "Laparoscopic, Gastro Intestinal, Bariatric & Metabolic Surgery"),
    ("Liver Transplant / Hepatobiliary Surgery", "Liver Transplant / Hepatobiliary Surgery"),
    ("Medical Oncology", "Medical Oncology"),
    ("Medical Oncology, Hematology And BMT", "Medical Oncology, Hematology And BMT"),
    ("Mental Health and Behavioural Sciences", "Mental Health and Behavioural Sciences"),
    ("Neonatology", "Neonatology"),
    ("Nephrology", "Nephrology"), ("Neuro & Spine Surgery", "Neuro & Spine Surgery"),
    ("Neuro Radiology", "Neuro Radiology"), ("Neurology", "Neurology"),
    ("Non Invasive Cardiology", "Non Invasive Cardiology"),
    ("Obstetrics and Gynaecology", "Obstetrics and Gynaecology"),
    ("Onco Sciences", "Onco Sciences"), ("Oral / Maxillofacial Surgery", "Oral / Maxillofacial Surgery"),
    ("Orthopaedics & Spine Surgery", "Orthopaedics & Spine Surgery"),
    ("Orthopaedics  Bone & Joint Surgery", "Orthopaedics  Bone & Joint Surgery"),
    ("Orthopaedics  Hand & Upper Limb Surgery", "Orthopaedics  Hand & Upper Limb Surgery"),
    ("Paediatric Cardiology", "Paediatric Cardiology"), ("Paediatric Endocrinology", "Paediatric Endocrinology"),
    ("Paediatric Nephrology", "Paediatric Nephrology"), ("Paediatric Neurology", "Paediatric Neurology"),
    ("Paediatric Oncology", "Paediatric Oncology"), ("Paediatric Orthopaedics", "Paediatric Orthopaedics"),
    ("Paediatric Pulmonology", "Paediatric Pulmonology"), ("Paediatric Surgery", "Paediatric Surgery"),
    ("Paediatrics", "Paediatrics"), ("Pain management", "Pain management"),
    ("Physiotherapy and Rehabilitation", "Physiotherapy and Rehabilitation"),
    ("Plastic, Cosmetic & Reconstructive Surgery", "Plastic, Cosmetic & Reconstructive Surgery"),
    ("DiabeticFoot Care", "Diabetic Foot Care"), ("Pulmonology", "Pulmonology"),
    ("Radiation Oncology", "Radiation Oncology"), ("Radiology", "Radiology"), ("Rheumatology", "Rheumatology"),
    ("Arthroscopic Surgery", "Arthroscopic Surgery"),
    ("Surgical Oncology", "Surgical Oncology"), ("Trauma & Emergency Medicine", "Trauma & Emergency Medicine"),
    ("Urology & Andrology", "Urology & Andrology"),
    ("Urology, Andrology & Transplant Surgery", "Urology, Andrology & Transplant Surgery"),
    ("Vascular Surgery", "Vascular Surgery"),)
    specialities = forms.MultipleChoiceField(choices=differnt_options,widget=forms.CheckboxSelectMultiple())

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