from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('rocks/',views.rocks_index,name='rock-index'),
    path('rocks/<int:rock_id>/', views.rock_detail, name='rock-detail'),
    path('rocks/create/', views.RockCreate.as_view(), name='rock-create'),

]