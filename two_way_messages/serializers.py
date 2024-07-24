from rest_framework import serializers

from .models import Content, Platform, Result


class PlatformSerializer(serializers.Serializer):
    class Meta:
        model = Platform
        fields = ["entityId", "applicationId"]


class ContentSerializer(serializers.Serializer):
    class Meta:
        model = Content
        fields = ["text", "cleanText", "type"]


class ResultSerializer(serializers.Serializer):
    platform = PlatformSerializer()
    content = ContentSerializer(many=True)

    class Meta:
        model = Result
        fields = [
            "channel",
            "sender",
            "destination",
            "content",
            "receivedAt",
            "messageId",
            "platform",
            "event",
        ]
