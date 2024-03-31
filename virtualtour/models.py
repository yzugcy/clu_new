from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Tour(models.Model):
    """ Virtual Tour model """
    title = models.CharField(_("Tour Title"), max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="tours/")
    duration = models.IntegerField(_("Duration in minutes"), default=0)
    scenes = models.IntegerField(_("Scenes"), default=0)
    location = models.CharField(_("Location"), max_length=255, null=True)
    latitude = models.CharField(_("Latitude"), max_length=255, null=True)
    longitude = models.CharField(_("Longitude"), max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="videos")
    video_file = models.FileField(_("Video"), upload_to="videos/")
    ordering = models.IntegerField(_("Ordering"), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.tour.title
