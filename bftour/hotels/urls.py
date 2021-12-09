from django.urls import path
from . import views

# 이미지 URL 설정
from django.conf.urls.static import static
from django.conf import settings


app_name = "hotels"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("makehotel/", views.makehotels, name="makehotel"),
    path("index/<int:pk>/", views.viewhotel, name="viewhotel"),
    path("delete/<int:pk>", views.deletehotel, name="deletehotel"),
    path("update/<int:pk>", views.updatehotel, name="updatehotel"),
]

# 이미지 url 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
