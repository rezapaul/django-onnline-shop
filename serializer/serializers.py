from products.models import Product
from order.models import Cart_Added ,Order_done
from accounts.models import Favorite 
from rest_framework import serializers





class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Added
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Favorite
        fields = '__all__' 

