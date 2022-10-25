# from django.db import models
# from django.contrib.auth.models import AbstractUser


# # Create your models here.

# class User(AbstractUser):
#     is_seller = models.BooleanField(default=False, help_text='Designates whether this user is a seller', verbose_name='Seller')
#     # updated = models.DateTimeField(auto_now=True, null=True)
#     # created = models.DateTimeField(auto_now_add=True, null=True)

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# from cart.models import Cart

# from company.models import Product


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=20, verbose_name='first name', blank=False)
    last_name = models.CharField(max_length=20, verbose_name='last name', blank=False)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True, blank=True)
    is_seller = models.BooleanField(default=False, verbose_name='Is seller')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def make_seller(self):
        self.is_seller = True
        return self.seller