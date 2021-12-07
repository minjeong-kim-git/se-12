from django.urls import path
from . import views
from django.conf.urls import url

app_name = "reservations"

urlpatterns = [
    path('reservation_list/', views.ReservationListView, name='ReservationList')
]

