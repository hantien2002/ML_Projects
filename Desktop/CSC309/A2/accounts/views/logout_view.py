from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    # Django's logout function will handle both authenticated and unauthenticated users
    logout(request)
    # Redirect to the login page after logout
    return redirect('accounts:login')
