from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfileManager(BaseUserManager):
    """Manager: Para perfiles de usuarios"""

    def create_user(self, email, name, role, password):
        """Crear nuevo useario"""
        if not email:
            raise ValueError('El usuario debe tener un email')
        
        if not password:
            raise ValueError('El usuario debe tener una constraseña')
        
        email = self.normalize_email(email)
        role = Role.objects.filter(name=role).first()
        user = self.model(email=email, name=name, role=role)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        role = "ADMIN"
        user = self.create_user(email, name, role, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuarios"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name