from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('view/<int:pk>/',views.view,name='view'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/',views.remove_from_cart, name='remove_from_cart'),
    path('remove-all-from-cart/<int:item_id>/',views.remove_all_from_cart, name='remove_all_from_cart'),
]