from rest_framework import serializers
from accounts.models import User, UserProfile
from slcd_logic.models import CustomerSupport


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_manager', 'is_support', 'is_customer']


class SignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2', 'is_manager', 'is_support', 'is_customer']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_manager= self.validated_data['is_manager']
        user.is_support= self.validated_data['is_support']
        user.is_customer= self.validated_data['is_customer'] 
        if user.is_manager == True:
            user.save()
            UserProfile.objects.create(user=user)
        if user.is_support == True:
            user.save()
            UserProfile.objects.create(user=user)
            CustomerSupport.objects.create(user=user)
        if user.is_customer == True:
            user.save()
            UserProfile.objects.create(user=user)
        return user

