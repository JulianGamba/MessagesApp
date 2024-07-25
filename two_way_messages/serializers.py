from rest_framework import serializers

from .models import Content, Platform, Result


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["entityId", "applicationId"]




class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["text", "cleanText", "type"]


class ResultSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        platform_data = validated_data.pop('platform')
        content_data = validated_data.pop('content')
        platform= Platform.objects.create(**platform_data)
        result = Result.objects.create(platform=platform, **validated_data)
        for content in content_data:
            content_instance = Content.objects.create(**content)
            result.content.add(content_instance)
        return result