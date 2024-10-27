from django.urls import path
from .views import connection_create, connection_list, ConnectionUpdateView, ConnectionDeleteView


app_name = 'connection'

urlpatterns = [
    path('create/', connection_create, name='connection_create'),
    path('', connection_list, name='connection_list'),
    path('update/<int:pk>/', ConnectionUpdateView.as_view(), name='connection_update'), # admin 여부 확인 필요
    path('delete/<int:pk>/', ConnectionDeleteView.as_view(), name='connection_delete'), # admin 여부 확인 필요
]
