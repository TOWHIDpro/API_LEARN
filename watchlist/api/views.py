from django.forms import SlugField
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
    permission_classes = [AdminOrReadonly]
    lookup_field = 'slug'
    

# ------------------Watch------------------------#
class WatchlistListView(ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializers
    permission_classes = [AdminOrReadonly]

class WatchlistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Watchlist
    serializer_class = WatchlistSerializers
    permission_classes = [AdminOrReadonly]
    lookup_field = 'slug'
    

# ------------------Review------------------------#
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializers
    def get_queryset(self):
        watchlist = Watchlist.objects.get(slug=self.kwargs['slug'])
        return Review.objects.filter(watchlist=watchlist.id)

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Review
    def perform_create(self, serializer):
        watchlist = Watchlist.objects.get(slug=self.kwargs['slug'])
        author = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, author=author)
        if review_queryset.exists():
            raise ValidationError('You already review this')

        # AVG rating rating logic
        if watchlist.number_of_ratings == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating+serializer.validated_data['rating'])/2
        watchlist.number_of_ratings = Review.objects.filter(watchlist=watchlist.id).count()+1
        watchlist.save()
        # ---------------------------------------------------------
        serializer.save(watchlist=watchlist, author=author)
    
 
class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializers
    permission_classes = [AuthorOrReadonly]