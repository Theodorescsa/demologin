from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['User','Bookname']

class membernewSeriallizers(serializers.Serializer):

    User = serializers.CharField(max_length=100)
    Bookname = serializers.CharField(max_length=200)
    
