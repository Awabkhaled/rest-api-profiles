from rest_framework.serializers import ModelSerializer
from . import models
class ProfilesSerializer(ModelSerializer):
    class Meta:
        model =  models.UserProfile
        fields = ('email','name','password')
