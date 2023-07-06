from rest_framework.serializers import ModelSerializer, BaseSerializer
from rest_framework import serializers
from .models import ExtensionData, Payload

class ExtensionDataSerializer(serializers.BaseSerializer):
    option_name = serializers.CharField(max_length=255, null=True, blank=True)
    option_value = serializers.IntegerField()
    display_index = serializers.IntegerField()

class PayloadSerializer(serializers.BaseSerializer):
    product_id = serializers.IntegerField()
    category_code = serializers.CharField()
    provider_id = serializers.CharField()
    name = serializers.CharField()
    short_description = serializers.CharField()
    is_balloon = serializers.BooleanField()
    cost_markup_type = serializers.CharField()
    is_finance = serializers.BooleanField()
    extension_data = ExtensionDataSerializer(many=True)

