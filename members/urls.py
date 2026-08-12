from django.urls import path
from .views import details, members, main

urlpatterns = [
    path('', main, name='main'),#landing page
    path('members/', members, name='members' ),
    path('members/<int:member_id>/', details, name='member_details'),
]