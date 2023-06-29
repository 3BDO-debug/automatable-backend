from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=350, verbose_name="Phone number")
    gov_id = models.CharField(max_length=350, verbose_name="GOV ID")
    account_type = models.CharField(max_length=350, verbose_name="Account type")
    profile_pic = CloudinaryField(
        verbose_name="User Profile Pic", null=True, blank=True
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AllowedView(models.Model):
    name = models.CharField(max_length=350, verbose_name="Allowed View Name")
    slug = models.SlugField(verbose_name="Allowed view slug", blank=True, null=True)
    description = models.TextField(verbose_name="Allowed View Description")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Allowed view"
        verbose_name_plural = "Allowed views"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AllowedView, self).save(*args, **kwargs)
