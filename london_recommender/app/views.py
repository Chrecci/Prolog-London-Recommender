from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .prolog import actual
# https://stackoverflow.com/questions/57747212/multi-user-web-application-over-prolog-data-files

def convert_answer(data):
    print(actual(data))
    return actual(data)

def index(request):
    request.session.flush()
    return render(request, 'app/index.html')

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
        # redirect to correct page
        if data == 'chill':
            return redirect(chill)
        if data == 'active':
            return redirect(active)
        if data == 'food':
            return redirect(goodfood)
        if data == 'energetic':
            return redirect(energetic)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VibeForm()

    return render(request, 'app/forms.html', {'form': form})

def chill(request):
    if request.method == 'POST':
        form = ChillForm(request.POST)
        if form.is_valid():
            data= request.POST.get('work')
            # print(data, request.session['input'])
            request.session['input'] += [data]
            print(request.session['input'])
        if data == 'yes':
            return redirect(work)
        if data == 'no':
            return redirect(walk)
    else:
        form = ChillForm()
    return render(request, 'app/forms.html', {'form': form})

def work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data= request.POST.get('env')
            # print(data, request.session['input'])
            request.session['input'] += [data]
            print(request.session['input'])
        return redirect(result)
    else:
        form = WorkForm()
    return render(request, 'app/submit.html', {'form': form})

def walk(request):
    if request.method == 'POST':
        form = WalkForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            walk= request.POST.get('walk')
            mask= request.POST.get('mask')
            travel_time = request.POST.get('travel_time')
            if int(travel_time) <= 10:
                travel = 'min'
            elif int(travel_time) <= 20:
                travel = 'avg'
            else:
                travel = 'max'
            print([walk, mask, travel])
            # print(data, request.session['input'])
            if walk == 'yes':
                request.session['input'] += [walk, travel]
                print('print', request.session['input'])
            else:
                request.session['input'] += [walk, mask]
                print('print', request.session['input'])
        return redirect(result)
    else:
        form = WalkForm()
    return render(request, 'app/submit.html', {'form': form})

def active(request):
    if request.method == 'POST':
        form = ActiveForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            bike = request.POST.get('bike')
            mask = request.POST.get('mask')
            # print(data, request.session['input'])
            request.session['input'] += [bike, mask]
            print(request.session['input'])
        return redirect(result)
    else:
        form = ActiveForm()
    return render(request, 'app/submit.html', {'form': form})

def goodfood(request):
    if request.method == 'POST':
        form = GoodFoodForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            meal = request.POST.get('meal')
            # print(data, request.session['input'])
            request.session['input'] += [meal]
            print(request.session['input'])
        if meal == "breakfast":
            return redirect(breakfast)
        else:
            return redirect(price)
    else:
        form = GoodFoodForm()
    return render(request, 'app/forms.html', {'form': form})

def breakfast(request):
    if request.method == 'POST':
        form = BreakfastForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            english = request.POST.get('english')
            # print(data, request.session['input'])
            request.session['input'] += [english]
            print(request.session['input'])
        return redirect(result)
    else:
        form = BreakfastForm()
    return render(request, 'app/submit.html', {'form': form})

def price(request):
    if request.method == 'POST':
        form = PriceForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            data = request.POST.get('price')
            # print(data, request.session['input'])
            if int(data) <= 10:
                price = 'min'
            elif int(data) <= 20:
                price = 'avg'
            else:
                price = 'max'
            request.session['input'] += [price]
            print(request.session['input'])
        return redirect(result)
    else:
        form = PriceForm()
    return render(request, 'app/submit.html', {'form': form})

def energetic(request):
    if request.method == 'POST':
        form = EnergeticForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            vulnerable = request.POST.get('vulnerable')
            energy = request.POST.get('energy')
            travel_time = request.POST.get('travel_time')
            # print(data, request.session['input'])
            if int(travel_time) <= 10:
                travel = 'min'
            elif int(travel_time) <= 20:
                travel = 'avg'
            else:
                travel = 'max'
            print([vulnerable, energy, travel])
            request.session['input'] += [vulnerable, energy, travel]
            print(request.session['input'])
        return redirect(result)
    else:
        form = EnergeticForm()
    return render(request, 'app/submit.html', {'form': form})

def result(request):
    context = {'result': request.session['input']}
    print(context)
    context['answer'] = convert_answer(context['result'])
    print('context', context)
    return render(request, 'app/result.html', context=context)