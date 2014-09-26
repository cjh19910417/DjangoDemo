import datetime
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def display_request_meta(request):
    metas = request.META.items()
    return render_to_response("display_requestMeta.html", locals())


def direct_to_template(request, template_name):
    try:
        return render_to_response("%s.html" % template_name)
    except TemplateDoesNotExist:
        raise Http404()