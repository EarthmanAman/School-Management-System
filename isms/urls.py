
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls.static import static
#from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls", namespace="main")),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('assessment/', include("assessment.urls", namespace="assessment")),
    path('institution/', include("institution.urls", namespace="institution")),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
