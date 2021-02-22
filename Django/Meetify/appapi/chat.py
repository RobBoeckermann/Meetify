import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

from ..models import Matches, Messages
from ..serializers import MessagesSerializer


def get_messages(request):
    messages = Messages.objects.filter(MatchId__in=(Matches.objects.filter(User1_id=request.user.pk) | Matches.objects.filter(User2_id=request.user.pk)))
    ser = MessagesSerializer(messages, many=True)
    return JsonResponse(ser.data, safe=False)

def send_message(request):
    body = json.loads(request.body)

    user = User.objects.filter(pk=body['ToUserID'])
    if not user:
        return HttpResponse(status=404, reason="Target user not found")
        
    match = (Matches.objects.filter(User1_id=request.user.pk, User2_id=body['ToUserID'], META_EndDate__isnull=True) | 
            Matches.objects.filter(User1_id=body['ToUserID'], User2_id=request.user.pk, META_EndDate__isnull=True)).first()

    if not match:
        return HttpResponse(status=403, reason="Users must be matched to send messages")

    if not match.AcceptedByUser1 or not match.AcceptedByUser2:
        return HttpResponse(status=403, reason="Both users must accept the match to send messages")

    message = Messages(Text=body['Text'], MatchId=match, SenderUserId=request.user)
    message.save()

    ser = MessagesSerializer(message)
    return JsonResponse(ser.data)

    


    
