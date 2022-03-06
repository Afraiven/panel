from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiPesel, name="api-pesel"),
    path('pesel-list/', views.peselList, name="pesel-list"),
    path('pesel/', views.peselCreate, name="pesel-create"),
    # path('pesel-delete/<str:pk>/', views.peselDelete, name="pesel-delete"),
    # path('pesel-delete/<str:pk>/', views.peselDelete, name="pesel-delete"),

]