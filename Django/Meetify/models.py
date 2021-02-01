from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#columns default to "not null"

class User_Info(models.Model):
    User = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE) #can call User_Info.User to use auth_user columns
    DisplayName = models.CharField(max_length=50)
    SpotifyDisplayName = models.CharField(max_length=150, null=True)
    SpotifyUserId = models.CharField(max_length=150, unique=True, null=True)
    SpotifyAuthToken = models.CharField(max_length=200, null=True)
    ZipCode = models.CharField(max_length=10, null=True)
    ProfilePic = models.ImageField(null=True)

    META_StartDate = models.DateTimeField(default=timezone.now, blank=True)
    META_EndDate = models.DateTimeField(null=True)

class Matches(models.Model):
    MatchId = models.IntegerField(primary_key=True)
    User1 = models.ForeignKey(User_Info, related_name='User1', on_delete=models.CASCADE)
    User2 = models.ForeignKey(User_Info, related_name='User2', on_delete=models.CASCADE)
    AcceptedByUser1 = models.BooleanField(default=False)
    AcceptedByUser2 = models.BooleanField(default=False)

    META_StartDate = models.DateTimeField(default=timezone.now, blank=True)
    META_EndDate = models.DateTimeField(null=True)

    """ (compatibility scores)
		percentage of liked songs in common
		number of liked songs in common
		top genres
		top artists
		time of day you listen to music
		dance-ability/acoustic-ness/etc. alignment
	MatchScore (calculated from sub-compatibility scores) """

    def is_match_active(self):
        "Returns whether both users have accepted the match."
        if self.AcceptedByUser1 and self.AcceptedByUser2:
            return True
        else:
            return False
    
class Messages(models.Model):
    class Meta:
        unique_together = (('MatchId', 'MessageNumber'),)

    MatchId = models.ForeignKey(Matches, on_delete=models.CASCADE)
    MessageNumber = models.IntegerField(primary_key=True) #start at 0, increment by one, use this to display message order instead of StartDate?
    Text = models.CharField(max_length=300) #what should the message limit be?
    SenderUserId = models.ForeignKey(User, on_delete=models.CASCADE)
    
    META_StartDate = models.DateTimeField(default=timezone.now, blank=True)
    META_EndDate = models.DateTimeField(null=True)

class Liked_Songs(models.Model):
    class Meta:
        unique_together = (('userId', 'songUri'),) #https://stackoverflow.com/questions/28712848/composite-primary-key-in-django

    userId = models.ForeignKey(User_Info, on_delete=models.CASCADE)
    songUri = models.CharField(max_length=200)
    
    META_StartDate = models.DateTimeField(default=timezone.now, blank=True)
    META_EndDate = models.DateTimeField(null=True)