from django.shortcuts import render
from blog.models import BlogArticles
# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'titles.html', {"blogs": blogs})