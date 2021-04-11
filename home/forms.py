from django import forms
from home.models import Cancion
class CancionForm(forms.ModelForm):
    class Meta:
        model=Cancion
        fields=['id','nombre','autor']
        labels={'id':'El id de la song',\
            'nombre':'nombre','autor':'autor'}
        widget={'id':forms.NumberInput(),'nombre':forms.TextInput(), \
            'autor':forms.TextInput()}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    