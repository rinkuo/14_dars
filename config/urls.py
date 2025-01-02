from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from students.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', include('students.urls', namespace='students')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('subjects/', include('subjects.urls', namespace='subjects')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
