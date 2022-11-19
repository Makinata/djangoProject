from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Query_broker
from .serializers import Query_broker_Serializer
import magic

# Create your views here.
class Query_broker_View(APIView):

    def get(self, request, req):
        query_broker = Query_broker(req, magic.magic(req))

        serializer_for_request = Query_broker_Serializer(instance=query_broker)

        return Response(serializer_for_request.data)
