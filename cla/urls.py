from django.urls import path
from . import views

app_name="cla"
urlpatterns =[
    path('',views.index,name='index'),
    path("about",views.about,name= "about"),
    path("computer",views.computer,name= "computer"),
    path("laptop",views.laptop,name= "laptop"),
    path("product",views.product,name= "product"),
    path("contact",views.contact,name= "contact"),
    path('cart', views.cart,name = 'cart'),
    path('checkout' ,views.checkout,name= 'checkout'),
    path('updateItem',views.updateItem,name='updateItem'),
    path('detail/<int:product_id>',views.detail,name='detail'),
    path('add_to_checkout/<int:product_id>',views.add_to_checkout,name='add_to_checkout'),
]

