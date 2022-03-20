
from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
]
handler404 = "store.views.error_404"
handler404 = "store.views.error_500"
handler404 = "store.views.error_403"
handler404 = "store.views.error_400"
