from rest_framework import serializers

from review.models import Review
from watchlist_app import models
from watchlist_app.models import WatchList, StreamPlatform


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"

#   https://stackoverflow.com/questions/67090526/the-create-method-does-not-support-writable-dotted-source-fields-by-default
    def create(self, validated_data):
        return models.WatchList.objects.create(**validated_data)


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
