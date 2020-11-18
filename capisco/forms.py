from django import forms
from .models import Tulkkaa


class KaantajaForm(forms.Form):
    fchoice = Tulkkaa.objects.filter(fkieli=True).values_list('id', 'kielinimi')
    tchoice = Tulkkaa.objects.filter(tkieli=True).values_list('id', 'kielinimi')
    kirjoita = forms.CharField(max_length=120,
                               widget=forms.TextInput(attrs={'size': '120',
                                                             'placeholder': 'Kirjoita tähän...'})
                               )
    fkieliselect = forms.CharField(label='Valitse lähtökieli',
                                   widget=forms.RadioSelect(choices=fchoice),
                                   required=True)
    tkieliselect = forms.CharField(label='Valitse kieli, jolle käännetään',
                                   widget=forms.RadioSelect(choices=tchoice),
                                   required=True)


class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)