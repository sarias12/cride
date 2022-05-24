"""
Django models utilities
"""

#Django
from unicodedata import name
from django.db import models
from django.forms import CharField

class CRideModel(models.Model):

    #https://docs.djangoproject.com/en/2.0/topics/db/models/#model-inheritance
    """Share Ride base model

    CRideModel Acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every tables with the following attributes:
        + created (DateTime): Store the datetime the object was created
        + created (DateTime): Store the last  datetime the object was modified

    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text= ' Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text= ' Date time on which the object was  last modified.'
    )

    class Meta:
        """Meta option.
        """

        #https://docs.djangoproject.com/en/2.0/ref/models/options/

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
        

