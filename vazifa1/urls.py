from django.urls import path
from .views import index,about,blog,contact,service,detail,feature,price,quote,team,testimonial

urlpatterns = [
path('',index,name="index-page"),
path('about/',about,name= "about-page"),
path('blog/',blog,name= "blog-page"),
path('contact/',contact,name= "contact-page"),
path('service/',service,name= "service-page"),
path('detail/',detail,name= "detail-page"),
path('feature/',feature,name= "feature-page"),
path('price/',price,name= "price-page"),
path('quote/',quote,name= "quote-page"),
path('team/',team,name= "team-page"),
path('testimonial/',testimonial,name= "testimonial-page"),

]