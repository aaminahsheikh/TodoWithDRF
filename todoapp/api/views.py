from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Task
from . serializers import TaskSerializer

from rest_framework.views import APIView


@api_view(['GET'])
def get_api(request):
    routes = {
        'Tasks': '/tasks',
        'Get Task': '/tasks/<pk>',
        'update': 'tasks-update/<pk>/',
        
    }

    return Response(routes)

class TaskAPI(APIView):
    
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors})
        
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is saved.'})
    
    def put(self, request):
        try:
            task = Task.objects.get(id=request.data['id'])
            serializer = TaskSerializer(task, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.data})
            
            serializer.save()
            return Response({'status': 200, 'payload': 'Your data is uploaded.'})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid id'})
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            task_obj = Task.objects.get(id=id)
            task_obj.delete()
            return Response({'status': 200, 'message': 'Task is deleted.'})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid id.'})
        



