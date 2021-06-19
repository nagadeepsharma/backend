from api.serializers import Blogsserializer, Projectsserializer
from api.models import Blogs, Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def index(request):
    content={
        "Projects":"/projects",
        "Blogs":"/blogs"
    }
    return Response(content)

@api_view(['GET'])
def projects(request):
    projects=Projects.objects.filter(isfeatured=False)
    featuredproject=Projects.objects.filter(isfeatured=True)
    fps=Projectsserializer(featuredproject,many=True)
    projectserializer=Projectsserializer(projects,many=True)
    return Response({"active":projectserializer.data,"featured":fps.data})

@api_view(['GET'])
def blogs(request):
    blogs=Blogs.objects.filter(active=True)
    bs=Blogsserializer(blogs,many=True)
    return Response(bs.data)

@api_view(['GET'])
def blog(request,pk):
    blogs=Blogs.objects.get(pk=pk,active=True)
    bs=Blogsserializer(blogs,)
    return Response(bs.data)
