from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from producerapp.views import getUserToken
schema_view = get_swagger_view(title='Book APIs')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', schema_view),
    url(r'^v1/', include('producerapp.urls')),
    path('tokeng/',getUserToken)
]