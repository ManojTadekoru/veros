from rest_framework import serializers
from .models import details,transaction

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = '__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'
