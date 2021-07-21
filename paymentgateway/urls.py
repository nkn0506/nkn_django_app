
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "NKN Admin"
admin.site.site_title = "NKN Admin Portal"
admin.site.index_title = "Welcome to NKN Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cover.urls'))
]
