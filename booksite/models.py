from django.db import models
# Create your models here.

class Contact(models.Model):
    name  = models.CharField(max_length=100, blank = False, null = False, help_text="Enter YOUR NAME")
    email = models.CharField(max_length=50, unique=False, blank = False, null = False)
    phone = models.CharField(max_length=20, blank = False, null = False)
    desc  = models.TextField()
    date = models.DateField()

    def __str__(self):
       return self.name


class myuploadfile(models.Model):
    file = models.FileField(upload_to='')
    description = models.TextField(max_length=50, unique=False, blank = False, null = False)
    file_name=models.TextField(max_length=50, unique=False, blank = False, null = False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.description