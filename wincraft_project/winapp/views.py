from django.shortcuts import render
from django.views.generic import View

class Homepage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')

class ProjectsPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'projects.html')
    
class AboutPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')    
