from django import forms
from .models import Bus,POINT


class BusForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'name':'bus_name','class':'form-control'}))
    start_point = forms.ChoiceField(choices=POINT,widget=forms.Select(attrs={'name':'start_point','class':'form-control'}))
    end_point = forms.ChoiceField(choices=POINT,widget=forms.Select(attrs={'name':'end_point','class':'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','type':'number'}))
    deperture_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = Bus
        fields = "__all__"