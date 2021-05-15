from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    path('',views.home,name = 'home'),
    path('upload',views.upload, name='upload'),
    path('edit/<int:image_id>',views.edit, name='edit'),
    path('search_category',views.search_category, name='search_category')
]