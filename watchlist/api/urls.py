from django.urls import path
from .views import WatchlistListView, WatchlistDetailView, StreamPlatformListView, StreamPlatformDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    # ------------------STREAMING PLATFORMS------------------------#
    path('', StreamPlatformListView.as_view(), name="streamingplatform-list"),
    path('<int:pk>', StreamPlatformDetailView.as_view(), name="streamingplatform-details"),

    # ------------------Watch------------------------#
    path('watchlist', WatchlistListView.as_view(), name="watchlist-list"),
    path('watchlist/<int:pk>', WatchlistDetailView.as_view(), name="watchlist-details"),

    # ------------------Review------------------------#
    path('review', ReviewListView.as_view(), name="review-list"),
    path('platform/<int:pk>', ReviewDetailView.as_view(), name="review-details"),
]
