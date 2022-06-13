from django.contrib import admin
from django.db import router
from django.urls import path,include
from deserialize import views
from rest_framework.routers import DefaultRouter
from deserialize.views import *

#creating router obj
router=DefaultRouter()

#registering
# router.register('product',views.PetroleumProductView, basename='product')
# router.register('country',views.CountryView, basename='country')
# router.register('detail',views.DetailView, basename='detail'),
router.register(r'sale',views.ProductSaleViewSet, basename='sale'),
router.register(r'country-sale',views.CountryWiseSaleView, basename='country-sale')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create/', views.create, name='create'),
    path('',include(router.urls)),
    path('country-create/', CountryCreateView.as_view()),
    path('product-create/', ProductCreateView.as_view()),
    path('year-create/', YearCreateView.as_view()),
    path('detail-create/', DetailCreateView.as_view()),
]