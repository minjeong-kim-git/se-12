from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("hotels/", include("hotels.urls", namespace="hotels")),
    path("payments/", include("payments.urls", namespace="payments")),
    path("reservations/", include("reservations.urls", namespace="reservations")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path('', include('hotels.urls')),
]

