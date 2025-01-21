from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    description = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
    last_update = serializers.DateTimeField(read_only=True)
    #collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())  # Allow input for collection
    #promotions = serializers.PrimaryKeyRelatedField(queryset=Promotion.objects.all(), many=True)  # Allow input for promotions
    collection = serializers.StringRelatedField()
    promotions = serializers.StringRelatedField()



    def create(self, validated_data):
        # Extract promotions from validated data
        promotions_data = validated_data.pop('promotions', [])
        # Create the Product instance
        product = Product.objects.create(**validated_data)
        # Add promotions to the ManyToMany field
        product.promotions.set(promotions_data)
        return product



# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField()
#     description = models.TextField()
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.IntegerField()
#     last_update = models.DateTimeField(auto_now=True)
#     collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
#     promotions = models.ManyToManyField(Promotion)