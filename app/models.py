from django.db import models

class topic(models.Model):
    tname=models.CharField(max_length=100,primary_key=True)
    def str(self):
        return self.tname
    
class webpage(models.Model):
    tname=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    url=models.URLField()
    def str(self):
        return self.name
    
class access(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def str(self):
        return self.author
# Create your models here.
