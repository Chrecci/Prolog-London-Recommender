from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .prolog import actual
# https://stackoverflow.com/questions/57747212/multi-user-web-application-over-prolog-data-files

def convert_answer(data):
    print(actual(data))
    return actual(data)

def get_vibe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VibeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data= request.POST.get('vibe')
            request.session['input'] = [data]
        # go to results page
        return redirect(chill)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VibeForm()

    return render(request, 'app/vibe.html', {'form': form})


def index(request):
    return render(request, 'app/index.html')

def chill(request):
    if request.method == 'POST':
        form = ChillForm(request.POST)
        if form.is_valid():
            data= request.POST.get('work')
            print(data, request.session['input'])
            request.session['input'] += [data]
            print(request.session['input'])
        return redirect(result)
    else:
        form = ChillForm()

    return render(request, 'app/forms.html', {'form': form})

def result(request):
    context = {'result': request.session['input']}
    context['answer'] = convert_answer(['chill', 'yes', 'library'])
    return render(request, 'app/result.html', context=context)