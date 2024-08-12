from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Product, Order
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the online store!")


# User registration view for clients
class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    @api_view(['POST'])
    def register(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user=User.objects.get(username=serializer.data['username'])
            user.set_password(serializer.data['password'])

            user.save()
            token = Token.objects.create(user=user) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User login view to get tokens
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Product views for clients
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  # Clients must be authenticated to view products

# Order views for clients
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Clients must be authenticated to create orders

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Clients must be authenticated to view orders

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
