from rest_framework import serializers
from .models import ChartView


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartView
        fields = ('start_at','end_at')


# class CreateCharterializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChartView
#         fields = ('guest_can_pause', 'votes_to_skip')