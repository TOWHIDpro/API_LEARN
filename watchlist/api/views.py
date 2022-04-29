from django.forms import SlugField
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from . serializers import StreamPlatformSerializer, ShowSerializers, ReviewSerializers
from watchlist.models import StreamPlatform, Show, Review
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
class ShowListView(ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializers
    permission_classes = [AdminOrReadonly]

class ShowDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Show
    serializer_class = ShowSerializers
    permission_classes = [AdminOrReadonly]
    lookup_field = 'slug'
    

# ------------------Review------------------------#
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializers
    def get_queryset(self):
        show = show.objects.get(slug=self.kwargs['slug'])
        return Review.objects.filter(show=show.id)

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Review
    def perform_create(self, serializer):
        show = show.objects.get(slug=self.kwargs['slug'])
        author = self.request.user
        review_queryset = Review.objects.filter(show=show, author=author)
        if review_queryset.exists():
            raise ValidationError('You already review this')

        # AVG rating rating logic
        if show.number_of_ratings == 0:
            show.avg_rating = serializer.validated_data['rating']
        else:
            show.avg_rating = (show.avg_rating+serializer.validated_data['rating'])/2
        show.number_of_ratings = Review.objects.filter(show=show.id).count()+1
        show.save()
        # ---------------------------------------------------------
        serializer.save(show=show, author=author)
    
 
class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review
    serializer_class = ReviewSerializers
    permission_classes = [AuthorOrReadonly]