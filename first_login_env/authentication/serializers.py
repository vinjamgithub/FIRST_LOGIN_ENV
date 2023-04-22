from rest_framework import serializers
from .models import credentials

class credentialsSerializer(serializers.ModelSerializer):

    class Meta:
        db_table = 'credentials'
        model = credentials 
        fields = ['pk', 'guru', 'k', 'email' ,'pass1''pass2']
