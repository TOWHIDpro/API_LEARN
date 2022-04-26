from rest_framework import serializers
from watchlist.models import StreamPlatform, Watchlist, Review

 # ------------------Review------------------------#
class ReviewSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'

# ------------------Watch------------------------#
class WatchlistSerializers(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review-details'
    )
    class Meta:
        model = Watchlist
        fields = '__all__'

# ------------------STREAMING PLATFORMS----------#
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field = 'slug',
        view_name='watchlist-details'
    )
    class Meta:
        model = StreamPlatform
        fields = '__all__'
