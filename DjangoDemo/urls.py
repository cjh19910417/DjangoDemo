from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import TemplateView
from Demo.contact.views import contact, contact_thinks
from Demo.views import hello, hours_ahead, display_request_meta, direct_to_template
from Demo.views import current_datetime
from DjangoDemo import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^template/(?P<template_name>\w+)/$',direct_to_template),
    (r'^hello/$', hello),
    (r'now/$',current_datetime),
    (r'now/plus/(\d{1,2})/$',hours_ahead),
    (r'meta/$',display_request_meta),
    (r'contact/$',contact),
    (r'contact/thinks/$',contact_thinks),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', 'demo_app.views.demo_form'),
    url(r'^form_template$', 'demo_app.views.demo_form_with_template'),
    url(r'^form_inline$', 'demo_app.views.demo_form_inline'),
    url(r'^formset$', 'demo_app.views.demo_formset', {}, "formset"),
    url(r'^tabs$', 'demo_app.views.demo_tabs', {}, "tabs"),
    url(r'^pagination$', 'demo_app.views.demo_pagination', {}, "pagination"),
    url(r'^widgets$', 'demo_app.views.demo_widgets', {}, "widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)