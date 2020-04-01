from django.db import models
from django.utils import timezone

# Create your models here.

def number():
    no = Post.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Post(models.Model):
    URGENCY = (('1', 'Most Important'),
               ('2', 'Priority 2'),
               ('3', 'Last Priority'),
               )

  
    name = models.CharField(max_length=200)
    id_number = models.IntegerField(primary_key=True,default=number)
    description = models.TextField(default="")
    header = models.TextField(max_length=200, default="")
    tester = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    urgency = models.IntegerField(choices=URGENCY)
    types = models.CharField(name="types", max_length=100)
    test_object = models.CharField(name="test_object", max_length=100)
    version = models.CharField(max_length=200)
    remarks = models.TextField(default="")

    def publish(self):
        self.save()

    def __str__(self):
        return (str(self.name) + "\n" + str(self.id_number) + "\n" +  str(self.description) + "\n" +  str(self.header) + "\n" 
         +  str(self.tester) + "\n" +  str(self.date) + "\n" +  str(self.urgency) + "\n" +  str(self.types)
          + "\n" +  str(self.test_object) + "\n" +  str(self.version))

class Requirements(models.Model):

    id_number = models.IntegerField(primary_key=True,default=number)
    description = models.TextField(default="")

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id_number) + str(self.description)
