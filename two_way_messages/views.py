from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Content, Platform, Result
from .serializers import ContentSerializer, PlatformSerializer, ResultSerializer


class ResultListCreateView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

@api_view(['GET', 'POST'])
def message_list_recieve(request):
    if request.method == 'GET':
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data.get('results', [])
        
        received_data = []
        for result_data in data:
            result_serializer = ResultSerializer(data=result_data)
           
            if result_serializer.is_valid():

                result_serializer.save()


                received_data.append(result_serializer.data)
            else:
                return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'message': 'La información del mensaje devuelto ha llegado',
            'data': received_data
        }, status=status.HTTP_201_CREATED)