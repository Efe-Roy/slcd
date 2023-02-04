from django.db import models
from accounts.models import UserProfile
from django.conf import settings


LICENSE_TYPE = (
    ('BP', 'BUILDING PERMIT'),
    ('RL', 'RECOGNITION LICENSE'),
    ('SL', 'SUBDIVISION LICENSE'),
    ('EL', 'EXTENSION LICENSE'),
    ('LP', 'LAND MOVEMENT AND PARCEL LICENSE'),
    ('DC', 'DEMOLITION AND CONSTRUCRION LICENSE'),
    ('SR', 'Structural Reinforcement')
)


class License(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    license_type = models.CharField(choices=LICENSE_TYPE, max_length=2)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    customer_support = models.ForeignKey("CustomerSupport", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerSupport(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    organization = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
