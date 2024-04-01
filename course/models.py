from django.db import models
from tinymce.models import HTMLField


class Course(models.Model):
    """ Course model """
    title = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField(upload_to="course/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_module(self):
        return self.course_module.all().count()


class CourseModule(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_module"
    )
    name = models.CharField(max_length=255)
    ordering = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_content(self):
        return self.course_content.all().count()


class CourseContent(models.Model):
    course_module = models.ForeignKey(
        CourseModule, on_delete=models.CASCADE, related_name="course_content"
    )
    name = models.CharField(max_length=255)
    content = HTMLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def read_status(self):
        content_read_status = CourseContentReadStatus.objects.get(content=self)
        return content_read_status.is_read


class CourseContentReadStatus(models.Model):
    user = models.ForeignKey(
        "customauth.User", on_delete=models.CASCADE,
        related_name="content_read_status"
    )
    content = models.ForeignKey(
        CourseContent, on_delete=models.CASCADE, related_name="content_read"
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
