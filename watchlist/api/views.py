from rest_framework import permissions
from rest_framework.exceptions import ValidationError
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
    permission_classes = [permissions.IsAuthenticated]

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        author = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, author=author)
        if review_queryset.exists():
            raise ValidationError('You already review this')

        # AVG rating rating logic
        if watchlist.number_of_ratings == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
            print(watchlist.storyline)
        else:
            watchlist.avg_rating = (watchlist.avg_rating+serializer.validated_data['rating'])/2
        watchlist.number_of_ratings = watchlist.number_of_ratings+1
        watchlist.save()
        # ---------------------------------------------------------
        serializer.save(watchlist=watchlist, author=author)
    
 
class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializers
    permission_classes = [AuthorOrReadonly]