from rest_framework.permissions import AllowAny
from rest_framework import generics, response, status
from .serializers import UserProfileCreateSerializer

class UserSignUpView(generics.GenericAPIView):
    serializer_class   = UserProfileCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            data = request.data
            serializer = UserProfileCreateSerializer(data = data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                
                return response.Response({
                    'status':200,
                    'message':'registered succesfully check email',
                    'data':serializer.data,
                })
            
            return response.Response({
                'status':400,
                'message':'something went wrong',
                'data': serializer.errors
            })
        
        except Exception as e:
            return response.Response({'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        

