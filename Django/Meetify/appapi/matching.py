import json
from django.utils import timezone
from django.http import JsonResponse
import spotipy

from ..models import User_Info, Liked_Songs, Matches
from ..serializers import MatchesSerializer


# returns a list of songsUris found on both the current user's liked songs AND the target user's liked songs.
def get_liked_songs_intersection(request):
    user_id = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    target_user_id = body['target_user_id']

    user1_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user_id)])
    user2_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=target_user_id)])
    intersection = list(set(user1_songs) & set(user2_songs))

    return intersection

def accept_match(request):
    user = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    match_id = body['match_id']
    match = Matches.objects.get(id=match_id)
    if (match.User1.User_id==user.User_id):
        match.AcceptedByUser1=True
    elif(match.User2.User_id==user.User_id):
        match.AcceptedByUser2=True
    else:
        return False
    match.save()    
    return True

def reject_match(request):
    user = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    match_id = body['match_id']
    match = Matches.objects.get(id=match_id)
    end_date=timezone.now()
    match.META_EndDate=end_date
    match.save()    
    return True
    
def get_potential_matches(request):
    matches = (Matches.objects.filter(User1_id=request.user.pk, AcceptedByUser1=False, META_EndDate=None) | 
                Matches.objects.filter(User2_id=request.user.pk, AcceptedByUser2=False, META_EndDate=None))
    
    ser = MatchesSerializer(matches, many=True)
    return JsonResponse(ser.data, safe=False)

def get_accepted_matches(request):
    matches = (Matches.objects.filter(User1_id=request.user.pk, AcceptedByUser1=True, AcceptedByUser2=True, META_EndDate=None) | 
                Matches.objects.filter(User2_id=request.user.pk, AcceptedByUser1=True, AcceptedByUser2=True, META_EndDate=None))

    ser = MatchesSerializer(matches, many=True)
    return JsonResponse(ser.data, safe=False)
