from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data= request.POST.get('name')
            context = {'name': data}
            # return HttpResponseRedirect('app/index')
        return render(request,'app/result.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app/name.html', {'form': form})


def index(request):
    return render(request, 'app/index.html')

def result(request):
    return render(request, 'app/result.html')