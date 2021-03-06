import uuid
from django.db import models
from accounts.models import Address
from core.models import BaseContact
from django.utils.translation import gettext_lazy as _
from core.models import Attachment


class CandidateSource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class SocialMedia(models.Model):
    class SocialMedias(models.TextChoices):
        LINKEDIN = 'ln', _('LinkedIn')
        FACEBOOK = 'fb', _('Facebook')
        INSTAGRAM = 'is', _('Instragram')
        TWITTER = 'tw', _('Twitter')
        GITHUB = 'gi', _('Github')
        TIKTOK = 'tk', _('TikTok')

    type = models.CharField(max_length=2, choices=SocialMedias.choices)
    link = models.URLField()
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.link


class CandidateProfile(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class WorkHistory(models.Model):
    title = models.TextField()
    employeer = models.TextField()
    currently_working = models.BooleanField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.ForeignKey("accounts.Address", on_delete=models.CASCADE, null=True)
    verified = models.BooleanField(default=False)
    summary = models.TextField(null=True, blank=True)
    reason_for_leaving = models.TextField(null=True, blank=True)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class QualificationChecklist(models.Model):
    # Pre defined qualificatoins to pick from
    title = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class CandidateQualification(models.Model):
    qualification = models.ForeignKey(
        QualificationChecklist, on_delete=models.CASCADE)
    value = models.BooleanField()

    def __str__(self) -> str:
        return self.qualification.title


class Candidate(models.Model):
    candidate_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    candidate_profile = models.ForeignKey(
        CandidateProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE,
        null=True
    )
    phones = models.ForeignKey(
        BaseContact, on_delete=models.CASCADE, null=True)
    social_medias = models.ManyToManyField(SocialMedia)
    address = models.ForeignKey("accounts.Address", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    source = models.ForeignKey(CandidateSource, on_delete=models.CASCADE)
    key_skills = models.TextField(null=True, blank=True)
    current_employeer = models.TextField(null=True, blank=True)
    date_available = models.DateField(null=True, blank=True)
    current_pay = models.CharField(max_length=200, null=True, blank=True)
    desired_pay = models.CharField(max_length=200, null=True, blank=True)
    best_contact_time = models.DateTimeField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    work_history = models.ManyToManyField(WorkHistory, null=True, blank=True)
    qualifications = models.ManyToManyField(CandidateQualification, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, null=True, blank=True)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.candidate_profile.first_name