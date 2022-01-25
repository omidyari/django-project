from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    creted_date = models.DateField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
