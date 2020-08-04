from django.urls import path
from winapp import views

app_name = 'winapp'

urlpatterns = [
    path('windows/casement/',views.casement,name='casement'),
    path('windows/sliding/',views.sliding,name='sliding'),
    path('specialised/lift/',views.lift,name='lift'),
    path('specialised/slide/',views.slide,name='slide'),
    path('specialised/tilt/',views.tilt,name='tilt'),
    path('slimline/slimline/',views.slimline,name='slimline'),
    path('curtain/curtain',views.curtain,name='curtain'),
]
