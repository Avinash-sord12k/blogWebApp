from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_img = models.ImageField(blank=True, null=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=255, blank=True, null=True)
    insta_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon_class_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

def get_image_filename(instance, filename):
    """Return the filename for the uploaded image."""
    ext = filename.split('.')[-1]
    # Generate a unique slug from the Post title
    slug = instance.slug
    # Construct the file path and name
    file_path = f'images/blogs/{slug}/thumbnail.{ext}'
    return file_path

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    thumbnail_url = models.URLField(blank=True)
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, default="Awsome blog")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title + "|" + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blogPage', args=(self.slug,))

class FeaturedBlog(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.post.title} - {self.name}'