from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
class ProfilesApiView(APIView):
    """Testing APIView"""
    serializer_class = serializers.ProfilesSerializer
    def get(self,request,format=None,pk=None):
        if pk:
            serializedProfiles = self.serializer_class(data = models.UserProfile.objects.all().filter(id=pk),many=True)
            if serializedProfiles.is_valid():
                return Response({"Message":"Get all the profiles in the database","Profile":serializedProfiles.data})
            return Response(serializedProfiles.errors, status=status.HTTP_400_BAD_REQUEST)
        serializedProfiles = self.serializer_class(models.UserProfile.objects.all(),many=True)
        return Response({"Message":"Get all the profiles in the database","Profiles":serializedProfiles.data})
    
    
    def post(self,request):
        serializedProfile = self.serializer_class(data=request.data)
        if serializedProfile.is_valid():
            serializedProfile.save()
            return Response({"Message":"Add a profile and return it","Profile":serializedProfile.data})
        return Response(serializedProfile.errors, status=status.HTTP_400_BAD_REQUEST)
