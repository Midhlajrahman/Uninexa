from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path("",views.index,name="index"), 
    path("features/",views.features,name="features"),
    path("pricing/",views.pricing,name="pricing"),
    path("insights/",views.insights,name="insights"),
    path("industry/",views.industry,name="industry"),
    path("testimonial/",views.testimonial,name="testimonial"),
    path("contact/",views.contact,name="contact"),
]
