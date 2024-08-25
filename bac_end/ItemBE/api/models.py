from django.db import models
from rest_framework import serializers
 
class Item(models.Model):
    #Sno = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=255)
    ItemCode = models.CharField(max_length=255)
    SKU = models.CharField(max_length=255)
    # ReferalCode = models.PositiveIntegerField()
    ReferralCode = models.CharField(max_length=255) 
 
    def __str__(self) -> str:
        return self.name

class ItemSerializer(serializers.Serializer):
    ReferralCode = serializers.CharField(max_length=255, required=False) 

    class Meta:
        model = Item
        fields = '__all__'