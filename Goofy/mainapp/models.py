from django.db import models
from django.contrib.auth.models import User

class LikedSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=200)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'song_id'], name='unique_user_song')
        ]


    def __str__(self):
        return f"{self.user.username} likes song {self.song_id}"
