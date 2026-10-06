from rest_framework import serializers
from .models import Products
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
        def validate_category(self,value):
            if len(value)<=0:
                raise serializers.ValidationError("Please Enter The catgeory")
            return value
        