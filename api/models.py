from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

    
class Projects(models.Model):
    thumbnail=models.ImageField(blank=True,null=True,upload_to="images/")
    title=models.CharField(max_length=150,blank=True,null=True)
    description=models.CharField(max_length=200,blank=True,null=True)
    link=models.URLField(max_length=200,blank=True,null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=False,blank=True,null=True)
    isactive=models.BooleanField(default=True,blank=True,null=True)
    isfeatured=models.BooleanField(default=False,blank=True,null=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.title



class Blogs(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    content=RichTextField()
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    active=models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.title

