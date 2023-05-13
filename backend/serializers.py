from rest_framework import serializers

from .models import ClientModel, Message, Distribution


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModel
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class DistributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distribution
        fields = '__all__'
