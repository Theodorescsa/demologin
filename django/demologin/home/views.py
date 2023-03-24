from django.shortcuts import render
from home.models import department
from .models import Member
from .serializers import MemberSerializer, membernewSeriallizers
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def get_home(request):
    object_list=department.objects.all( )
    return render(request, 'task3.html', {
        'object_list': object_list
    })



class MemberList(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
# class MemberList(APIView):
    # def get(self, request):
    #     list_member = Member.objects.all()
    #     mydata = MemberSerializer(list_member, many = True)
    #     return Response(data=mydata.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        mydata = membernewSeriallizers(data=request.data)
        if not mydata.is_valid():
            return Response('Data failure',status=status.HTTP_400_BAD_REQUEST)
      
        User = mydata.data['User']
        Bookname = mydata.data['Bookname']
        respon = Member.objects.create(User=User, Bookname=Bookname)
        # return Response(data=respon.member_id, status=status.HTTP_200_OK)
        return Response(data={
    'member_id': respon.member_id,
    'User': respon.User,
    'Bookname': respon.Bookname
}, status=status.HTTP_200_OK)
