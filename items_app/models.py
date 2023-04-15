from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Item(models.Model):
    # TODO: change fields (before we migrate)
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    # tags = models.JSONField(default=list, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
