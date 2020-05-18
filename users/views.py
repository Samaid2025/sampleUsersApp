from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializer import UsersSerializer
import traceback


class Login(APIView):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({'status': 200, 'message':"login successful"})
        else:
            return Response({'status': 401, 'message':"could not login"})


class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        users = UsersSerializer(users, many=True)
        return Response({'status': 200, 'users':users.data})
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")

        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)
            user = UsersSerializer(user)
            return Response({'status': 200, 'message':"user added", "user": user.data})
        except:
            traceback.print_exc()
            return Response({'status': 500, 'message':"user could not be created"})

