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
            #link = form.cleaned_data['url']
            # redirect to a new URL:
            values = {'form' : form, 'link' : link}
            return render(request, 'urls/success.html', values)
        else:
            return render(request, 'urls/failure.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form

    

def index(request):
    values = {'form' : SubmitForm(),
              'recent_links' : Link.objects.all()
             }
    
    return render(request, 'urls/index.html', values)