
from django import forms
from .models import SaveStudentData
from enroll import models

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=SaveStudentData
        fields=['name','password']
        widgets =  {
                        'name': forms.TextInput(attrs={'class':'form-control'}),
                        #'email': forms.EmailInput(attrs={'class':'form-control'}),
                        'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
                    }
