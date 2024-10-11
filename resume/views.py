from django.views import View
from django.shortcuts import render, redirect
from .models import Contact


class IndexView(View):
    def get(self, request):
        return render(request, 'morex/index-3.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'morex/about-2.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'morex/services-2.html')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'morex/portfolio-2.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'morex/blog-2.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'morex/contact-2.html')

    def post(self, request):
        ism = request.POST['ism']
        familiya = request.POST['familiya']
        massage = request.POST['massage']
        contact = Contact(ism=ism, familiya=familiya, massage=massage)
        contact.save()
        return redirect('contact')
