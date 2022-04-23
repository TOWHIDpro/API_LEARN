from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . serializers import StreamPlatformSerializer, WatchlistSerializers, ReviewSerializers
from watchlist.models import StreamPlatform, Watchlist, Review

# ------------------STREAMING PLATFORMS------------------------#
class StreamPlatformListView(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class StreamPlatformDetailView(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform
    serializer_class = StreamPlatformSerializer

# ------------------Watch------------------------#
class WatchlistListView(ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializers

class WatchlistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Watchlist
    serializer_class = WatchlistSerializers

# ------------------Review------------------------#
class ReviewListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializers