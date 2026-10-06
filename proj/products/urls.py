from django.urls import path,include
from products import views
urlpatterns = [
    path('',views.products.as_view()),
    path('<int:id>/',views.Products.as_view())
]
