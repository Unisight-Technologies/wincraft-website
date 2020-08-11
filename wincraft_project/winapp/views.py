from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages
from django.core.mail import send_mail

def sendMailToUser(name, send_to):
    subject = "Regarding query sent on Wincraft Buildmat's Website"
    message = "Hello "+name+"! \n\nWe have successfully received your query.\nWe are glad that you tried to connect with us.\n\nWe will get back to you as soon as possible.\n\nRegards\n-Team Wincraft Buildmat"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        [send_to],
        fail_silently = False,
    )

def sendMailToWincraft(name, email_phone, query):
    message = ""
    if '@' in email_phone:
        message = "The following query has been received on our website:\n\nName: "+name+"\nEmail Id: "+email_phone+"\nQuery: "+query+"\n\nRegards"
    else:
        message = "The following query has been received on our website:\n\nName: "+name+"\nPhone number: "+email_phone+"\nQuery: "+query+"\n\nRegards"
    subject = "A query has been received on Wincraft Buildmat"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        ['wincraftbuildmat@gmail.com'],
        fail_silently = False,

    )


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
                sendMailToUser(name, email_phone)
                sendMailToWincraft(name, email_phone, query)
                messages.success(request, "Your query has been successfully submitted. We will get back to you soon.")
                return redirect("index")

            else:
                new_query = models.Queries.objects.create(
                    name=name,
                    phone=email_phone,
                    query=query
                )
                new_query.save()
                sendMailToWincraft(name, email_phone, query)
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
