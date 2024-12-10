from django.shortcuts import render,redirect
from .models import post
from .forms import PostForm
# Create your views here.
def home(request):
    vari=post.objects.all()
    return render(request,'home.html',{'vari':vari})


def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form=PostForm()
    return render(request,'add_post.html',{'form':form})
    

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import PostSerializer 


class PostList(APIView):
     def get(self,request):
          vari=post.objects.all()
          serializer=PostSerializer(vari,many=True)
          return Response(serializer.data)
     def post(self,request):
          serializer=PostSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     


          
