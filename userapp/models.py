from django.db import models
import uuid

UType=[
    ('OPERATOR','OPERATOR'),
    ('ADMIN','ADMIN'),
    ('FACULTY','FACULTY')
]


STATUS_CHOICES=[
    ('Active','Active'),
    ('Deactive','Deactive')
]

class userinfo(models.Model):
    UID=models.AutoField(primary_key=True)
    UName=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    UType=models.CharField(max_length=50, choices=UType,blank=True)
    Status=models.CharField(choices=STATUS_CHOICES, null=True, blank=True, max_length=50)
    Mobile=models.BigIntegerField()
    Email=models.EmailField(max_length=50)
    Cdatatime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UName
