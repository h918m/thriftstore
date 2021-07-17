import order.models as order_models
import order.serializers as order_serializers
from django.db.models.functions import Lower
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from store import models as store_models
from store import serializers as store_serializers
from store.models import Category, Favorite, Image, Product
from store.serializers import CategorySerializer, ImageNewSerializer, ProductSerializer

from .models import Friend, Vendor


class CurrentVendorSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    friends_products = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    order_requests = order_serializers.OrderSerializer(many=True)
    orders_made = order_serializers.OrderSerializer(many=True)

    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "products",
            "friends",
            "friends_products",
            "favorites",
            "order_requests",
            "orders_made",
        ]

    def get_friends(self, obj):
        try:
            friend = Friend.objects.get(current_vendor=obj)
            friends = friend.vendors.all()
        except:
            friends = None
            return []
        friends_serializer = VendorFriendSerializer(friends, many=True)
        return friends_serializer.data

    def get_products(self, obj):
        my_products = Product.objects.filter(vendor=obj.id).order_by(Lower("title"))
        product_serializer = ProductSerializer(my_products, many=True)
        return product_serializer.data

    def get_friends_products(self, obj):
        try:
            friend = Friend.objects.get(current_vendor=obj)
            friends = friend.vendors.all()
        except:
            friends = None
            return []
        friends_products = Product.objects.filter(vendor__in=friends).order_by("-created_at")
        product_serializer = ProductSerializer(friends_products, many=True)
        return product_serializer.data

    def get_favorites(self, obj):
        favorites, created = Favorite.objects.get_or_create(vendor=obj)
        favorite_products = obj.favorites.favorites.all()
        product_serializer = ProductSerializer(favorite_products, many=True)
        return product_serializer.data


class OtherVendorSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "products",
        ]

    def get_products(self, obj):
        their_products = Product.objects.filter(vendor=obj.id).order_by(Lower("title"))
        product_serializer = ProductSerializer(their_products, many=True)
        return product_serializer.data


class VendorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "slug", "created_by", "name"]


class VendorFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VendorFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    orders = order_serializers.OrderSerializer(read_only=True, many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Vendor
        fields = ["name", "products", "orders", "created_at", "created_by", "slug"]


class VendorAdminSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    order_requests = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = "__all__"
        # fields = ["name", "products", "orders", "created_at", "created_by", "slug"]

    # def get_products(self, obj):
    #     vendor_products, created = Product.objects.get_or_create(vendor=obj)
    #     all_products = obj.products.products.all()
    #     product_serializer = ProductSerializer(all_products, many=True)
    #     return product_serializer.data

    # def get_order_requests(self, obj):
    #     vendor_orders, created = order_models.Order.objects.get_or_create(vendor=obj)
    #     all_orders = obj.orders_requests.orders.all()

    #     for order in all_orders:
    #         order.vendor_amount = 0
    #         order.vendor_paid_amount = 0
    #         order.fully_paid = True

    #         for item in order.order_detail.all():
    #             if item.vendor == obj:
    #                 if item.vendor_paid:
    #                     order.vendor_paid_amount += item.get_total_price()
    #                 else:
    #                     order.vendor_amount += item.get_total_price()
    #                     order.fully_paid = False

    #     order_serializer = order_serializers.OrderSerializer(all_orders, many=True)
    #     return order_serializer.data


class VendorProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    vendor = VendorSerializer(read_only=True)
    product_images = ImageNewSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "category", "vendor", "title", "description", "slug", "regular_price", "product_image"]

    # def create(self, validated_data):
    #     images_data = validated_data.pop("product_image")
    #     category_data = validated_data.pop("category")
    #     product, created = Product.objects.get_or_create(**validated_data)
    #     if images_data:
    #         for image_data in images_data:
    #             Image.objects.create(product=product, **image_data)
    #     category, created = Category.objects.get_or_create(**category_data)
    #     return product
