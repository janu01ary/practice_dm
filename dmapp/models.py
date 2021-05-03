from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dm(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender', default='', null=True) #발신자 
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver', default='', null=True) #수신자 
    content = models.CharField(max_length=500) #내용
    send_time = models.DateTimeField() #보낸 시간
    read = models.BooleanField(default=False) #확인했는지 (확인했으면 True, 아니면 False)

    def __str__(self):
        return self.content