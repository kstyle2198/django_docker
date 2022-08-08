from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name, self.code
    
    class Meta:
        verbose_name_plural = 'companies'
