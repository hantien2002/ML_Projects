from django.http import JsonResponse, HttpResponse
from django.views import View

class ViewProfileView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        
        # Assuming request.user is the instance of the authenticated user
        user_data = {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name
        }
        return JsonResponse(user_data)
