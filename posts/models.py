from django.db import models
from django.contrib.auth import get_user_model


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-published',)


    def __str__(self):
        return self.title