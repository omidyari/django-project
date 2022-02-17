from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/defult.jpg')
    escriber = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    creted_date = models.DateField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    class Meta:
        ordering = ['-creted_date']
    def __str__(self):
        return self.title


