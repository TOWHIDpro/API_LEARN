from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from . serializers import StreamPlatformSerializer, WatchlistSerializers, ReviewSerializers
from watchlist.models import StreamPlatform, Watchlist, Review
from . permissions import AdminOrReadonly, AuthorOrReadonly

# ------------------STREAMING PLATFORMS------------------------#
class StreamPlatformListView(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadonly]

class StreamPlatformDetailView(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform
    serializer_class = StreamPlatformSerializer
    lookup_field = 'slug'
    

# ------------------Watch------------------------#
class WatchlistListView(ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializers
    permission_classes = [AdminOrReadonly]

class WatchlistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Watchlist
    serializer_class = WatchlistSerializers
    lookup_field = 'slug'
    permission_classes = [AdminOrReadonly]

# ------------------Review------------------------#
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializers
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        author = self.request.user
        serializer.save(watchlist=watchlist, author=author)
    permission_classes = [permissions.IsAuthenticated]

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializers
    permission_classes = [AuthorOrReadonly]