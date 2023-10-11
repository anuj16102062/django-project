from django.urls import path
from .views import register_user, mark_cellular_spam,search_user_by_name,search_user_by_phone,get_user_details,get_all_users

urlpatterns = [
    path('register', register_user),
    path('mark-spam', mark_cellular_spam),
    path('search/name', search_user_by_name),
    path('search/mob_number', search_user_by_phone),
    path('user-details', get_user_details),
    path('all-users-details', get_all_users),
]
