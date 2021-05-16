from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    path('',views.home,name = 'home'),
    path('upload',views.upload, name='upload'),
    path('edit/<int:image_id>',views.edit, name='edit'),
    path('search_category',views.search_category, name='search_category'),
    path('filter_by_location',views.filter_by_location, name='filter_by_location'),
    path('copy_image_url/<int:image_id>',views.copy_image_url,name='copy_image_url'),
    path('delete_image/<int:image_id>',views.delete_image,name='delete_image'),
    path('get_image/<int:image_id>',views.get_image_by_id,name='get_image')

]