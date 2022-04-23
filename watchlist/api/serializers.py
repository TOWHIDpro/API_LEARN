from rest_framework import serializers
from watchlist.models import StreamPlatform, Watchlist, Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class WatchlistSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watchlist-details'
    )
    class Meta:
        model = StreamPlatform
        fields = '__all__'