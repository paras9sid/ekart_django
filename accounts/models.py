from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            # normalize email - if cap char is sued in email - it will convert it in small char
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        #in built funtion for settign password
        user.set_password(password)
        #save password in db
        user.save(using=self.db)
        return user
    
    # function for creating superuser
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name=last_name,
        )

        # giving permission to superuser - all true
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        #saving details in db
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)


    #required for custom user field
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # for login with email add not username - overriding
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # we are using MyAccountmanager
    objects = MyAccountManager()

    # name to be display on adminpanel
    def __str__(self):
        return self.email
    
    #providing superadmin all permission
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True