from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.country})"
