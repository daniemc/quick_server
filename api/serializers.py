from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import UnitMeasures, Vendors, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance


class MeasuresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UnitMeasures
        fields = ('id', 'name', 'description', 'level')


class VendorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendors
        fields = ('id', 'name', 'active')


class ProductsSerializer(serializers.ModelSerializer):
    purchase_unit_measure = serializers.StringRelatedField(many=False)
    sale_unit_measure = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'purchase_unit_measure',
            'purchase_qty',
            'sale_unit_measure',
            'sale_qty',
          ]

