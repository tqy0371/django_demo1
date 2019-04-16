from django.db import models

# Create your models here.
class BookInfo(models.Model):
    bittle=models.CharField(max_length=20)
    bpud_date=models.DateTimeField()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=100)
    hBook=models.ForeignKey("BookInfo",on_delete=models.CASCADE)
