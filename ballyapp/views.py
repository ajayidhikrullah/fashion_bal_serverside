from django.shortcuts import render
from .forms import CreateSignUpLetterForm
from django.http import HttpResponseRedirect
# fro

from django.template import RequestContext
from django.template.defaulttags import csrf_token
from .models import news_letters
from django.http import HttpResponse
# from django.contrib.auth.forms import
# Create your views here.

# HOME PAGE
def home_page(request):
     return render(request, 'ballyapp/index.html', {})
     # return render(request, 'ballyapp/index.html')

# signupLetter----to database
def create_news_letters(request):
    # return HttpResponse(request.method)
    if request.method == 'POST':
        #creating a form instance nd populate it with data from the request

        form = CreateSignUpLetterForm(request.POST)
        #check whether form conditions is valid
        if form.is_valid():
            # gets the value inserted in the html text box
            # res = form['user_mails'].value()
            new_subscrition = form.save(commit=False)
            new_subscrition.email = form['email'].value()
            # save the instance
            new_subscrition.save()
            if form.save():
                form.email = form['email'].value()
                form.save()
                return HttpResponse(form.cleaned_data['email'] + " has subscribed successfuly")
            else:
                return HttpResponse("Oops failed to subscribe to our news letter, Try again....")
        else:
            return HttpResponse(form.is_valid())
    else:
        return HttpResponse("GET REQUEST Try again....")

        return HttpResponseRedirect('/')
        # if request coming from the form is a GET request then execute the below code
        form = CreateSignUpLetterForm()
        # context = {'form': form}
        # templates = 'ballyapp/index.html'

    # return render(request, templates, context)
    return HttpResponse("skdks")
    #
    # return HttpResponseRedirect('/')
