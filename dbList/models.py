from django.db import models


class Connection(models.Model):
    CONNECTION_TYPES = [
        ('postgres', 'PostgreSQL'),
        ('mysql', 'MySQL'),
        ('redis', 'Redis'),
        # 필요에 따라 다른 연결 유형 추가
    ]

    name = models.CharField(max_length=200, unique=True)
    conn_type = models.CharField(max_length=50, choices=CONNECTION_TYPES)
    host = models.CharField(max_length=200)
    port = models.IntegerField()
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    extra = models.JSONField(blank=True, null=True)  # 추가 설정을 위한 필드

    def __str__(self):
        return self.name
