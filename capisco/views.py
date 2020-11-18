from translate import Translator

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from capisco.forms import KaantajaForm
from capisco.models import Tulkkaa


def kaantaja(request):
    """Itse rakennettu kielenkäätäjäkone. Mahdollisuus valita kielet. Taustalla Google Translator, but pythonisch"""
    kaanna = 'kirjoita tähän...'
    translation = 'käännös'
    fkieliotsikko = 'Valitse kieli'
    tkieliotsikko = 'Valitse kieli'

    if request.method == 'POST':
        form = KaantajaForm(request.POST)
        if form.is_valid():
            kaanna = form.cleaned_data['kirjoita']
            fkieli = Tulkkaa.objects.values_list('kielikoodi', flat=True).get(pk=form.cleaned_data['fkieliselect'])
            tkieli = Tulkkaa.objects.values_list('kielikoodi', flat=True).get(pk=form.cleaned_data['tkieliselect'])
            # print(fkieli)
            # print(tkieli)
            translator = Translator(from_lang=fkieli, to_lang=tkieli)
            translation = translator.translate(kaanna)
    else:
        form = KaantajaForm()

    context = {
        'fkieliotsikko': fkieliotsikko,
        'tkieliotsikko': tkieliotsikko,
        'kaanna': kaanna,
        'translation': translation,
        'form': form
    }

    return render(request, 'kaantaja.html', context)


def vaihdafkieli(request):
    fkieliotsikko = request.GET.get('fkieli_val')
    return JsonResponse({'fkieliotsikko': fkieliotsikko})


def vaihdatkieli(request):
    tkieliotsikko = request.GET.get('tkieli_val')
    return JsonResponse({'tkieliotsikko': tkieliotsikko}, status=200)
