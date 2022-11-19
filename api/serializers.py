from rest_framework import serializers

class Query_broker_Serializer(serializers.Serializer):
    req = serializers.CharField()
    resp = serializers.CharField()