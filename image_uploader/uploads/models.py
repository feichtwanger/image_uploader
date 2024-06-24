# uploads/models.py
from django.db import models

class Image(models.Model):
    original = models.ImageField(upload_to='originals/')
    thumb = models.ImageField(upload_to='thumbs/', null=True, blank=True)
    big_thumb = models.ImageField(upload_to='big_thumbs/', null=True, blank=True)
    big_1920 = models.ImageField(upload_to='big_1920/', null=True, blank=True)
    d2500 = models.ImageField(upload_to='d2500/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
