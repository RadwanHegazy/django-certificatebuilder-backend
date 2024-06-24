from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError


class TokenClass :
    @property
    def tokens (self) :
        user = self.user
        tokens = RefreshToken.for_user(user)
        return {
            'token' : str(tokens.access_token)
        }

class LoginSerializer (serializers.Serializer, TokenClass) : 
    email = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid email"
            })
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : "invalid password"
            })

        return attrs
    
class RegisterSerializer(serializers.ModelSerializer, TokenClass) :
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', )

    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        return self.user