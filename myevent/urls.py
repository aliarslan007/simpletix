from django.urls import path,  include
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('create/step1', views.create_event_step1, name='create_event_step1'),
path('create/step2', views.create_event_step2, name='create_event_step2'),
path('eventdetail/<int:event_id>/', views.event_detail, name='event_detail'),
path('eventdetailall', views.event_detail_all, name='event_detail_all'),
]