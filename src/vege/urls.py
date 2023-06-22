from django.urls import path
from .views import *

urlpatterns = [
    path('receipes/', receipe , name = 'receipe'),
    path('delete-receipe/<id>', delete_receipe, name = 'delete_receipe'),
    path('update-receipe/<id>', update_receipe, name = 'update_receipe'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register, name='register')

]