from django.urls import path
from .views import ConnectionListView, ConnectionCreateView, ConnectionUpdateView

urlpatterns = [
    path('connections/', ConnectionListView.as_view(), name='connection_list'),
    path('connections/create/', ConnectionCreateView.as_view(), name='connection_create'),
    path('connections/<int:pk>/update/', ConnectionUpdateView.as_view(), name='connection_update'),
]