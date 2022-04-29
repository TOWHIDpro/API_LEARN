from rest_framework import serializers
from watchlist.models import StreamPlatform, Show, Review

 # ------------------Review------------------------#
class ReviewSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    Show = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

# ------------------Watch------------------------#
class ShowSerializers(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review-details'
    )
    class Meta:
        model = Show
        fields = '__all__'

# ------------------STREAMING PLATFORMS----------#
class StreamPlatformSerializer(serializers.ModelSerializer):
    show = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field = 'slug',
        view_name='show-details'
    )
    class Meta:
        model = StreamPlatform
        fields = '__all__'
