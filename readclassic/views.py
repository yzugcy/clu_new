import os
import time
from datetime import datetime
from random import random
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import Count, Q
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus
from cultch import settings
from readclassic import models
from readclassic.models import Classic, Comment


class ClassicsharingPagegameView(View):
    """ game view """
    template_name = 'readclassic/Classic_Sharing.html'

    def get(self, request, *args, **kwargs):
        obj = models.Comment.objects.filter(author_email=self.kwargs['email']).values('classicid')
        ob_ca=models.Classic.objects.filter(id__in= obj).values('category')
        print(ob_ca)
        classics = Classic.objects.all()
        classics_proposed = Classic.objects.filter(category__in= ob_ca)
        return render(request, self.template_name, {'classics': classics,'c_pr':classics_proposed})


    def post(self, request, *args, **kwargs):
        img_obj = request.FILES.get('img')
        # 保存文件
        new_name = getNewName('avatar')  # 具体实现在自己写的uploads.py下
        # 将要保存的地址和文件名称
        where = '%s/images/%s' % (settings.MEDIA_ROOT, new_name)
        # 分块保存image
        content = img_obj.chunks()
        with open(where, 'wb') as f:
            for i in content:
                f.write(i)
        author = request.POST.get('author')
        content = request.POST.get('content')
        title = request.POST.get('title')
        current_datetime = datetime.now()
        create_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        ca=request.POST.get('category')
        Classic.objects.create(title=title,content=content,create_time=create_time,category=ca,author=author,img=new_name)
        obj = models.Comment.objects.filter(author_email=self.kwargs['email']).values('classicid')
        ob_ca=models.Classic.objects.filter(id__in= obj).values('category')
        print(ob_ca)
        classics = Classic.objects.all()
        classics_proposed = Classic.objects.filter(category__in= ob_ca)
        return render(request, self.template_name, {'classics': classics,'c_pr':classics_proposed})


class LearnFamousPagesongsView(View):
    """ s view """
    template_name = 'readclassic/Learn_Famous_Sayings.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)




class SharingDetailsView(View):
    template_name = 'readclassic/class_sharing_details.html'

    def get(self, request, *args, **kwargs):
        # 根据ID查询c
        comment_list = Comment.objects.filter(classicid=self.kwargs['id'])
        c =get_object_or_404(Classic, id=self.kwargs['id'])
        context = {
                'classic': c,
                'comment_list':comment_list
            }
        print(comment_list)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
            email = request.POST.get('email_pcd')
            print("email",email)
            content = request.POST.get('content')
            classicid = request.POST.get('classicid')
            current_datetime = datetime.now()
            comment_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            Comment.objects.create(content=content,classicid=classicid,author_email=email,comment_time=comment_time)
            comment_list = Comment.objects.filter(classicid=self.kwargs['id'])
            print(comment_list)
            c = get_object_or_404(Classic, id=self.kwargs['id'])
            context = {
                'classic': c,
                'comment_list': comment_list
            }
            return render(request, self.template_name, context)
class SharingDetails_saveView(View):
    template_name = 'readclassic/class_sharing_details.html'

    def get(self, request, *args, **kwargs):
        # ID_>c
        Classic.objects.filter(id=self.kwargs['id']).update(likes=int(self.kwargs['likes'])+1)
        c = get_object_or_404(Classic, id=self.kwargs['id'])
        comment_list = Comment.objects.filter(classicid=self.kwargs['id'])
        print(comment_list)
        context = {
        'classic': c,
        'comment_list': comment_list
         }
        return render(request, self.template_name,context)


    def post(self, request, *args, **kwargs):

        email = request.POST.get('email_pcd')
        print("email1", email)
        content = request.POST.get('content')
        classicid = request.POST.get('classicid')
        current_datetime = datetime.now()
        comment_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        Comment.objects.create(content=content, classicid=classicid, author_email=email, comment_time=comment_time)
        comment_list = Comment.objects.filter(classicid=self.kwargs['id'])
        c = get_object_or_404(Classic, id=self.kwargs['id'])
        print(comment_list)
        context = {
            'comment_list': comment_list,
        'classic': c,
        }
        return render(request, self.template_name,context)

def getNewName(file_type):
     #this function is update image name
        new_name = time.strftime(file_type + '-%Y%m%d%H%M%S', time.localtime())
        ranlist = np.random.randint(0, 10, 5)
        for i in ranlist:
            new_name += str(i)
        new_name += '.jpg'
        return new_name

class SharingDetails_delete_commentView(View):
    template_name = 'readclassic/class_sharing_details.html'

    def get(self, request, *args, **kwargs):
        # ID_>c
        Comment.objects.filter(id=self.kwargs['id']).delete()
        c = get_object_or_404(Classic, id=self.kwargs['classicid'])
        comment_list = Comment.objects.filter(classicid=self.kwargs['classicid'])
        print(comment_list)
        context = {
        'classic': c,
        'comment_list': comment_list
         }
        return render(request, self.template_name,context)
class SharingDetails_delete_classicView(View):
    template_name = 'readclassic/Classic_Sharing.html'

    def get(self, request, *args, **kwargs):
        # 根据ID查询c
        Classic.objects.filter(id=self.kwargs['id']).delete()
        classics = Classic.objects.all()
        obj = models.Comment.objects.filter(author_email=self.kwargs['email']).values('classicid')
        ob_ca = models.Classic.objects.filter(id__in=obj).values('category')
        print(ob_ca)

        classics_proposed = Classic.objects.filter(category__in=ob_ca)

        context = {
                'classics': classics,
                 'c_pr': classics_proposed
            }
        return render(request, self.template_name, context)
