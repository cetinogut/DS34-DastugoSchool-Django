from django.db import models

# Create your models here.
class Contact(models.Model):
    """Model definition for ."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for ."""

        # verbose_name = ''
        # verbose_name_plural = ''

    def __str__(self):
        """Unicode representation of ."""
        return self.name
