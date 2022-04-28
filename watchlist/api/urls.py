from django.urls import path
from .views import WatchlistListView, WatchlistDetailView, StreamPlatformListView, StreamPlatformDetailView, ReviewListView, ReviewDetailView, ReviewCreateView

urlpatterns = [
    # ------------------STREAMING PLATFORMS----------#
    path('platform', StreamPlatformListView.as_view(), name="streamingplatform-list"),
    path('platform/<slug:slug>', StreamPlatformDetailView.as_view(), name="streamingplatform-details"),

    # ------------------Watch------------------------#
    path('watchlist', WatchlistListView.as_view(), name="watchlist-list"),
    path('watchlist/<slug:slug>', WatchlistDetailView.as_view(), name="watchlist-details"),

    # ------------------Review------------------------#
    path('watchlist/<slug:slug>/review-list', ReviewListView.as_view(), name="review-list"),
    path('watchlist/<slug:slug>/review-create', ReviewCreateView.as_view(), name="review-create"),
    path('review/<int:pk>', ReviewDetailView.as_view(), name="review-details"),
]
