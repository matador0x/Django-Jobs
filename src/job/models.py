from django.db import models
from django.utils.text import slugify
# Create your models here.



job_choices = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)

def image_upload(instance, filename):
    imageName, exetention = filename.split(".")
    return "jobsUsersImages/%s.%s"%(instance.id, exetention)

class Job(models.Model):

    title           = models.CharField(max_length=100,null=True)
    jobT            = models.CharField(max_length=15, choices=job_choices,null=True)
    description     = models.TextField(max_length=1000,null=True)
    date_Created    = models.DateTimeField(auto_now=True,null=True)
    open_positions  = models.IntegerField(default=1,null=True)
    salary          = models.IntegerField(default=0,null=True)
    experience      = models.IntegerField(default=0,null=True)
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    images          = models.ImageField(upload_to=image_upload, null=True)
    slug            = models.SlugField(blank=True, null=True)


    ## Over wirte save botton to add slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name