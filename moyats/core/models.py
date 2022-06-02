from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class BaseContact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cell_number = models.CharField(validators=[phone_regex], max_length=17)
    work_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    home_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.cell_number)


class Color(models.Model):
    hex = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.hex


class Activity(models.Model):
    class ActivityType(models.TextChoices):
        MEETING = 'mt', _('Meeting')
        EMAIL = 'em', _('Email')
        CALL = 'ca', _('Call')
        OTHER = 'ot', _('Other')

    organization = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.BaseUser", on_delete=models.CASCADE)
    activity_type = models.CharField(
        max_length=2, choices=ActivityType.choices)
    # These are need for generic relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.__str__()} | {self.content_type} | {self.activity_type}"
