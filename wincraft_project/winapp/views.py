from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages

class Homepage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
            form = request.POST
            name = form.get('name')
            email_phone = form.get('email_phone')
            query = form.get('query')

            if '@' in email_phone:
                new_query = models.Queries.objects.create(
                    name=name,
                    email=email_phone,
                    query=query
                )
                new_query.save()
                messages.success(request, "Your query has been successfully submitted. We will get back to you soon.")
                return redirect("index")

            else:
                new_query = models.Queries.objects.create(
                    name=name,
                    phone=email_phone,
                    query=query
                )
                new_query.save()
                messages.success(request, "Your query has been successfully submitted. We will get back to you soon.")
                return redirect("index")

class ProjectsPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'projects.html')

class AboutPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')

class ProductsPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'products.html')



def casement(request):
    return render(request, 'products/windows/casement.html')


def sliding(request):
    return render(request, 'products/windows/sliding.html')

def lift(request):
    return render(request, 'products/specialised/lift.html')


def slide(request):
    return render(request, 'products/specialised/slide.html')


def tilt(request):
    return render(request, 'products/specialised/tilt.html')


def slimline(request):
    return render(request, 'products/slimline/slimline.html')


def curtain(request):
    return render(request, 'products/curtain/curtain.html')
