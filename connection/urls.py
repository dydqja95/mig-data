from django.urls import path
from .views import connection_create, connection_list, connection_update, connection_delete


app_name = 'connection'

urlpatterns = [
    path('create/', connection_create, name='connection_create'),
    path('', connection_list, name='connection_list'),
    # path('update/<int:pk>/', connection_update, name='connection_update'), # admin 여부 확인 필요
    # path('delete/<int:pk>/', connection_delete, name='connection_delete'), # admin 여부 확인 필요
]
