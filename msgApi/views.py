from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MsgSerializer

# Create your views here.
mes = {"msg": "Get Message And Post it On a Database"}

def viewErr(e):
    return Response(f"Error: {e}")

#views here
@api_view(['GET'])
def default(request):
    return Response("Getting messages for d_simple")


@api_view(['GET', 'POST', 'DELETE'])
def messages(request):
    msgs = Message.objects.all()
    serializedMsg = MsgSerializer(msgs, many=True)
    
    try:
        if request.method == "POST":
            data = request.data
            newMsg = Message(msg=data['msg'], day=data['day'])
            newMsg.save()
            print(f"{'#'*100}\n\n{str(newMsg)}\n\n{'#'*100}")
        if request.method == "GET":
            serializedMsg = MsgSerializer(msgs, many=True)
            if serializedMsg.is_valid():
                serializedMsg.save()
            
    except KeyError as k:
        return viewErr(k)
    except Exception as e:
        print(f"{'#'*100}\n\n{e}\n\n{'#'*100}")
    
    return Response(serializedMsg.data)