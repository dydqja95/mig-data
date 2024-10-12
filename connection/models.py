from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Connection(models.Model):

    CONNECTION_TYPE_CHOICES = [
        ('oracle', 'Oracle'),
        ('postgresql', 'Postgresql'),
    ]
    id = models.AutoField(primary_key=True)  # pk
    conn_name = models.CharField(max_length=255, null=False)  # 커넥션명
    conn_type = models.CharField(max_length=255, choices=CONNECTION_TYPE_CHOICES, null=False)  # 커넥션 타입 (oracle, postgresql, bigquery)
    owner = models.CharField(max_length=255, null=False)
    ip = models.GenericIPAddressField(null=False)
    port = models.CharField(max_length=10, null=False)
    user = models.CharField(max_length=255, null=False)
    pwd = models.CharField(max_length=255, null=False)
    extra = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pwd = make_password(self.pwd)
        super(Connection, self).save(*args, **kwargs)

    def __str__(self):
        return self.conn_name