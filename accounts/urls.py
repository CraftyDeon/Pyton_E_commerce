from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.index,name='acc'),
    path('signup/',views.register,name='list'),
    path('login/',views.ulogin,name='ulogin'),
    path('logout/',views.ulogout,name='ulogout'),
    path('profile/',views.profile,name='profile'),

]