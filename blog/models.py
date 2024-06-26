# importing django models and users
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Publish"), (2, "Delete"))


# creating an django model class
class posts(models.Model):
    # title field using charfield constraint with unique constraint
    title = models.CharField(max_length=200, unique=True)
    # slug field auto populated using title with unique constraint
    slug = models.SlugField(max_length=200, unique=True)
    # author field populated using users database
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # and date time fields automatically populated using system time
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    # content field to store our post
    # content = models.TextField()
    content = RichTextField()
    # meta description for SEO benefits
    metades = models.CharField(max_length=300, default="new post")
    # status of post
    status = models.IntegerField(choices=STATUS, default=0)
    # URL field for storing the post's image
    image_url = models.URLField(blank=True, null=True)


class cricket(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    content = models.TextField()
    metades = models.CharField(max_length=300, default="new post")
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(blank=True, null=True)

    # meta for the class
    class Meta:
        ordering = ['-created_on']

    # used while managing models from terminal
    def __str__(self):
        return self.title
