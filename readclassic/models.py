from django.db import models
class Classic(models.Model):
    id=models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.CharField(max_length=255)
    category =models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='1827316887@qq.com')
    likes=models.BigIntegerField(default=0)
    img = models.ImageField(upload_to='images', default='avatar-2024033113040001029.jpg')  # 本次使用的是这个
    class Meta:
        db_table = 'classic'



class Comment(models.Model):
    id=models.BigIntegerField(primary_key=True)
    content = models.TextField()
    comment_time = models.CharField(max_length=255)
    pre_id =models.BigIntegerField()

    author_email=models.CharField(max_length=255,default='1827316887@qq.com')
    classicid=models.BigIntegerField()

    class Meta:
        db_table = 'comment'

