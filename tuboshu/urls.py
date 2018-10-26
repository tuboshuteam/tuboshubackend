from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # django-restful-framework
    path('api-auth/', include('rest_framework.urls')),

    # api
    path('api/userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('api/post/', include('post.urls', namespace='post')),
    path('api/point/', include('point.urls', namespace='point')),
    path('api/comment/', include('comment.urls', namespace='comment')),
]

# 媒体文件地址
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)