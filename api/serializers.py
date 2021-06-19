from django.db.models import fields
from rest_framework import serializers
from .models import Blogs, Projects, Tag
class Projectsserializer(serializers.ModelSerializer):

    tags=serializers.SlugRelatedField(many=True,slug_field='name',queryset=Tag.objects.all())
    class Meta:
        model=Projects
        fields=('id','thumbnail','title','description','link','tags',)
class Blogsserializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=('id','title','description','content',)