from django.db import models


class Platform(models.Model):
    entityId = models.CharField(max_length=255)
    applicationId = models.CharField(max_length=255)


class Content(models.Model):
    text = models.CharField(max_length=255)
    cleanText = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Result(models.Model):
    channel = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    content = models.ManyToManyField(Content, null=True)
    receivedAt = models.CharField(max_length=255)
    messageId = models.CharField(max_length=255)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
