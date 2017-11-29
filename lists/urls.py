from django.conf.urls import url


from .views import view_list, new_list, new_list2, my_lists


urlpatterns = [
    url(r'^new$', new_list2, name='new_list'),
    url(r'^(\d+)/$', view_list, name='view_list'),
    url(r'^users/(.+)/$', my_lists, name ='my_lists'),
]
