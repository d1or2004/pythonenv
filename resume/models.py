from django.db import models


class Contact(models.Model):
    ism = models.TextField(null=True, blank=True)
    familiya = models.TextField(null=True, blank=True)
    massage = models.TextField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.familiya
