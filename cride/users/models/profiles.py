""" Profile Model """

# Django 
from django.db import models


# Utilities 
from cride.utils.models import CRideModel

class Profile(CRideModel):
    """Profile Model
    
    
    A profile holds a user's peblic data like bigraphy, picture,
    and statistics
    """


    # Model Fiel References Relations 
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to= 'users/pictures/',
        blank = True,
        null = True
    )

    biography = models.TextField(max_length=500, blank=True)

    # Stats


    #Model field reference 
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on rides taken and offered"
    )

    def __str__(self) -> str:
        """Return profile's user representation"""
        return str(self.user)