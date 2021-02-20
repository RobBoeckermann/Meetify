import json
from django.http import HttpResponse
from django.http import JsonResponse

from ..models import Matches, Messages
from ..serializers import MessagesSerializer


def get_messages(request, user_id):
    if user_id != request.user.pk:
        return HttpResponse(status=401, reason="User must be logged in to view messages")
        
    messages = Messages.objects.filter(MatchId__in=(Matches.objects.filter(User1_id=user_id) | Matches.objects.filter(User2_id=user_id)))
    ser = MessagesSerializer(messages, many=True)
    return JsonResponse(ser.data, safe=False)

def send_message(request, user_id):
    if user_id != request.user.pk:
        return HttpResponse(status=401, reason="User must be logged in to send messages")

    body = json.loads(request.body)
    match = (Matches.objects.filter(User1_id=user_id, User2_id=body['ToUserID'], META_EndDate__isnull=True) | 
            Matches.objects.filter(User1_id=body['ToUserID'], User2_id=user_id, META_EndDate__isnull=True)).first()

    if not match:
        return HttpResponse(status=403, reason="Users must be matched to send messages")

    if not match.AcceptedByUser1 or not match.AcceptedByUser2:
        return HttpResponse(status=403, reason="Both users must accept the match to send messages")

    message = Messages(Text=body['Text'], MatchId=match, SenderUserId=request.user)
    message.save()

    ser = MessagesSerializer(message)
    return JsonResponse(ser.data)

    


    
