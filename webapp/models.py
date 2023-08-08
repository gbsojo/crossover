from django.db import models

class Playlist(models.Model):
    id: models.CharField(max_length=36)