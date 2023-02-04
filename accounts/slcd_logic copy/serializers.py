from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields =('pk', 'first_name', 'last_name', 'age', 'license_type', 'organization', 'customer_support')
        