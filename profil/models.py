from django.db import models

class Profil(models.Model):
    username = models.CharField(max_length=150, unique=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default-user-avatar.jpg")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
