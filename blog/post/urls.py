from . import views
from django.urls import path

urlpatterns = [
    path('', views.home ,name = 'home'),
    path('landing/', views.landing, name='landing'),
    path('chapters/<int:pk>', views.chapters, name='chapters'),
    path('learning/<int:key>', views.learning, name='learning'),
    path('lecture/<int:key>', views.lecture, name='lecture'),
    path('premium/', views.premium, name = 'premium')
]