
from . import views
from django.urls import path

urlpatterns = [
    # Index Path of a Root element (Metrics)
    path('', views.index, name='index'),
    path('<id>/<int:definition>/<aggregation>/', views.detail, name='detail'),
    # Detail Web Page
    path('<id>/', views.detail, name='detail'),
]
