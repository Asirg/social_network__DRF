from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model
# class SocialNetworkUser(AbstractUser):
#     first_login = models.DateTimeField(null=True)
#     phone = models.IntegerField()
#     avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)

# class Profile(models.Model):
#     user = models.ForeignKey(
#         to=SocialNetworkUser, 
#     )

#     biografia = models.TextField()
#     sex = models.CharField(max_length=1)
#     birthdat = models.DateField()
    
#     # contacts = models.ManyToManyField(
#     #   to=
#     # )
#     # skills = models.ManyToManyField(
#     #   to=
#     # )