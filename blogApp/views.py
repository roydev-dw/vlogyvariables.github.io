from django.shortcuts import render
from django.views.generic import View

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home-blog.html', context={})
