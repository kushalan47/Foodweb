from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',food_list,name='food_list'),
    path('detail/<int:id>',food_detail,name='detail'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('create/',ContactCreateView.as_view(),name='create'),
    path('update/<int:pk>/',ContactUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',ContactDeleteView.as_view(), name="delete"),
    # path('search/',search, name="search"),
    path('signup/',SignUpView.as_view(), name="signup"),
]
