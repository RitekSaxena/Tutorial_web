from django.db import models

# Create your models here.


class Course(models.Model):

    title = models.CharField(max_length=2000)
    desc = models.TextField(max_length=1000, default=None)
    def __str__(self):
        return self.title

class Chapters(models.Model):
    name = models.CharField(max_length=2000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Videos(models.Model):
    premium_status = models.BooleanField(default=False)
    description = models.TextField(null=True)
    title = models.CharField(max_length=2000)
    video_ss = models.FileField(upload_to='blog/staticfiles/', default = None)
    videofile = models.FileField(upload_to='blog/staticfiles/')
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Content(models.Model):
    premium_status = models.BooleanField(default=False)
    title = models.CharField(max_length=2000)
    docs = models.FileField(upload_to='blog/staticfiles/')
    chapter = models.ForeignKey(Videos, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


