from django.db import models

# Create your models here.
class Dm(models.Model):
    sender_id = models.IntegerField() #발신자 id, user에서 아이디 외래키로 받아와야
    receiver_id = models.IntegerField() #수신자 id, user에서 아이디 외래키로 받아와야
    content = models.CharField(max_length=500) #내용
    send_time = models.DateTimeField() #보낸 시간

    def __str__(self):
        return self.content