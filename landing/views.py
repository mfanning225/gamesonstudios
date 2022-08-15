from django.shortcuts import render, redirect
from django.http import HttpResponse

from landing.forms import LandingForm

def landing(request):
    landing_form = LandingForm()

    if request.method == 'POST':
        landing_form = LandingForm(request.POST, request.FILES)
        if landing_form.is_valid():

            landing_form.save()
            return redirect('thank-you')
        
            
    context = {'landing_form': landing_form}
    return render(request, 'landing/landing.html', context)

def thankyou(request):
    return render(request, 'landing/thank-you.html')

