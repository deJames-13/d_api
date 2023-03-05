from . import models
from rest_framework.serializers import ModelSerializer

class MsgSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"