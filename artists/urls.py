from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('new/', views.artist_new, name='artist_new'),
    path('all/', views.all_artists, name='artists'),
    path('artist-<int:artist_id>/', views.artist, name="artist_show"),
    path('update-artist-<int:artist_id>/', views.update_artist, name="artist_update"),
    path('upload-csv/', views.artist_upload, name="artist_upload"),
]

