from django.urls import path
from .views import profile_edit_view, register_view, login_view, logout_view, profile_view_view 

app_name='accounts'
urlpatterns = [
    path('register/', register_view.RegisterView.as_view(), name='register'),
    path('login/', login_view.LoginView.as_view(), name='login'),
    path('profile/edit/', profile_edit_view.ProfileEditView.as_view(), name='profile_edit'),
    path('logout/', logout_view.logout_view, name='logout'),
    path('profile/view/', profile_view_view.ViewProfileView.as_view(), name='profile_view'),
]
