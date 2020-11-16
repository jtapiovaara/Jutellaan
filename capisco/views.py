from django.shortcuts import render
from translate import Translator
from capisco.forms import KaantajaForm
from capisco.models import Tulkkaa


def kaantaja(request):
    """Itse rakennettu kielenkäätäjäkone. Mahdollisuus valita kielet. Taustalla Google Translator, but pythonisch"""
    kaanna = 'kirjoita tähän...'
    translation = 'käännös'
    fkieli = 'fi'
    tkieli = 'it'

    if request.method == 'POST':
        form = KaantajaForm(request.POST)
        if form.is_valid():
            kaanna = form.cleaned_data['kirjoita']
            fkieli = Tulkkaa.objects.values_list('kielikoodi', flat=True).get(pk=form.cleaned_data['fkieliselect'])
            tkieli = Tulkkaa.objects.values_list('kielikoodi', flat=True).get(pk=form.cleaned_data['tkieliselect'])
            print(tkieli)
            translator = Translator(from_lang=fkieli, to_lang=tkieli)
            translation = translator.translate(kaanna)
    else:
        form = KaantajaForm()

    context = {
        'kaanna': kaanna,
        'translation': translation,
        'form': form
    }
    return render(request, 'kaantaja.html', context)

