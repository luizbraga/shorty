from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SubmitForm
from .models import Link

def submit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            kwargs = {'url': form.cleaned_data['url']}
            link = Link.objects.create(**kwargs)
            # redirect to a new URL:
            return render(request, 'urls/success.html', {'link': link})
        else:
            return render(request, 'urls/failure.html', {'link_form': form})

    # if a GET (or any other method) we'll create a blank form

    

def index(request):
    #values = {'link_form' : SubmitForm()}
    
    return render(request, 'urls/index.html', {'form' : SubmitForm()})