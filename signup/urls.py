# Import the utility functions from the django urls library
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
      # Map the root URL / to be handled by
      # 'registration.views.registration_form' view
      url(r'^$', views.registration_form, name= 'signup'),

]