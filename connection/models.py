from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Connection(models.Model):

    CONNECTION_TYPE_CHOICES = [
        ('oracle', 'Oracle'),
        ('postgresql', 'Postgresql'),
    ]
    id = models.AutoField(primary_key=True)  # pk
    conn_name = models.CharField(max_length=255, unique=True, null=False)  # 커넥션명
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
    

class srcTableBas(models.Model):
    id = models.AutoField(primary_key=True)
    conn_id = models.ForeignKey(Connection, on_delete=models.CASCADE)
    owner = models.CharField(max_length=255, null=False)
    table_name = models.CharField(max_length=255, null=False)

class srcTableDtl(models.Model):
    id = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(srcTableBas, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=255, null=False)
    column_comment = models.CharField(max_length=255, null=False)
    column_type = models.CharField(max_length=255, null=False)
    column_column_rk = models.IntegerField()
    if_yn = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['table_id', 'if_yn'])
        ]
