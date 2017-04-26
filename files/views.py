from django.shortcuts import render
from django.views.generic import FormView
from .forms import S3DirectUploadForm, UserForm
from django.contrib.auth.models import User

from django.views.generic import TemplateView

from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Meta, Data

from django.contrib.auth import logout

from PyPDF2 import PdfFileReader
import codecs

class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request,
            'files/register.html',
            {'user_form': user_form, 'registered': registered} )

@login_required(redirect_field_name='/login/')
def meta(request):
    current_user = User.objects.get(username=request.user.username),
 
    if 'name' in request.POST:
      name = request.POST['name']
    
    if 'size' in request.POST:
      size = request.POST['size']

      md = Meta.objects.create(
        filename = name,
        size = size,
        upload_date = timezone.now(),
        user = current_user,
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

def extract_data(request):
         
      if request.FILES:
        
        file = request.FILES['file']
        input = PdfFileReader(file)
        if input.isEncrypted:
          input.decrypt('')

        
        info = input.getDocumentInfo()
        title = info.title
        author = info.author

        d = Data.objects.create(
          title = title,
          author = author
        )
        d.save()
         
        response = {
          'status': 1,
          'message': 'Data saved'
        }
        return HttpResponse(response, content_type='application/json')

      else:
        output = ''
        return HttpResponse(output)
     
