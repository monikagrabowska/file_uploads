from django.shortcuts import render
from django.views.generic import FormView

from .forms import S3DirectUploadForm

from django.views.generic import TemplateView

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Meta

class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm

@login_required(redirect_field_name='/admin/login/')
def meta(request):
    
    if 'name' in request.POST:
      name = request.POST['name']
    
    if 'size' in request.POST:
      size = request.POST['size']

      md = Meta.objects.create(
        filename = name,
        size = size,
        upload_date = timezone.now()
      )
      md.save()
      
      response = {
        'status': 1,
        'message': 'Data saved'
      }
      return HttpResponse(response, content_type='application/json')

    else:
      name = False
      output = ''
      return HttpResponse(output)

