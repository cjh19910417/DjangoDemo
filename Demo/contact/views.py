from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Demo.contact.forms import ContactForm

__author__ = 'chenjianhua'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            return HttpResponseRedirect('/contact/thinks/')
        else:
            return render_to_response('contact_form.html', locals(), context_instance=RequestContext(request))
    else:
        form = ContactForm()
        return render_to_response('contact_form.html', locals(), context_instance=RequestContext(request))


def contact_thinks(request):
    return render_to_response('contact_thinks.html')
