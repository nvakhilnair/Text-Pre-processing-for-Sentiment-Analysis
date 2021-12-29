from rest_framework import serializers

class Serializer(serializers.Serializer):
    text = serializers.CharField()
    corrector = serializers.CharField()