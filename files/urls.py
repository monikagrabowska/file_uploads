from django.conf.urls import url

from .views import MyView
from . import views 


urlpatterns = [
    url(r'^form/', MyView.as_view(), name='form'),
    url(r'^meta/', views.meta, name='meta'),
]





