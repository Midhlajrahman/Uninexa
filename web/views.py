from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'web/index.html')


def features(request):
    return render(request, 'web/features.html')


def pricing(request):
    return render(request, 'web/pricing.html')


def insights(request):
    return render(request, 'web/blog.html')


def industry(request):
    return render(request, 'web/industry.html')


def testimonial(request):
    return render(request, 'web/testimonial.html')


def contact(request):
    return render(request ,'web/contact.html')