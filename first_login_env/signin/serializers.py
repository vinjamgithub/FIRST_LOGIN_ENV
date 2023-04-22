
from rest_framework import serializers
from . models import userlogin


class userloginSerializer(serializers.ModelSerializer):    
    class Meta:
        model=userlogin
        fields='__all__'

        