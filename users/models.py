from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Manager (BaseUserManager) : 
    
    def create_user(self, password, **fields) : 
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **fields) : 
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(**fields)


class User (AbstractUser) : 
    objects = Manager()

    first_name = None
    last_name = None
    username = None
    groups = None

    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ('full_name',)
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.full_name
    

