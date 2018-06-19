# from django.contrib.auth.models import User, Group

from rest_framework import serializers
from idols.models import Buyer

class BuyerSerializer(serializers.ModelSerializer):
    """Serializer for BuyerSerializer"""

    class Meta:
        model = Buyer
        fields = ('id', 'buyer_name', 'phone_no', 'address')

    # def read(self):
    #     return self


# class BuyerSerializer(serializers.Serializer):
#     """Serializer for BuyerSerializer"""
#     buyer_name = serializers.CharField(max_length=50)
#     phone_no   = serializers.CharField(max_length=14, allow_blank=True, default='')
#     address    = serializers.CharField(allow_blank=True, default='')
#
#     def read(self):
#         return self


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
