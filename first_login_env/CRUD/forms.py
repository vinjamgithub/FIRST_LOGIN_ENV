from django import forms
from .models import crud


class EmpForm(forms.ModelForm):
    class Meta:
        model = crud
        fields = 'fullname' ,'mobile','empcode','position' 
        labels = {
            'fullname' : 'Full Name',
            'empcode' : 'EMP Code'
        }

    def __init__(self, *args , **kwargs): 
        super(EmpForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Positions"
        self.fields['fullname'].required =True