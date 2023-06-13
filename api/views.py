from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpRequest
from .models import Task
import json

def to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
        "created": task.created,
        "updated": task.updated,
    }


class TaskListView(View):
    def get(self, request:HttpRequest):
        tasks = Task.objects.all()
        return JsonResponse([to_dict(task) for task in tasks], safe=False, status=200)
    def post(self,request:HttpRequest):
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data.get('title'):
            return JsonResponse({'status':"title yo'q"})
        elif not data.get('description'):
            return JsonResponse({'status':'description yo\'q'})
        
        task = Task.objects.create(
            title = data['title'],
            description = data['description']
        )

        task.save()

        return JsonResponse(to_dict(task),status=201)

class TaskIdView(View):
    def get(self,request:HttpRequest,id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        task = Task.objects.get(id=id)
        return JsonResponse(to_dict(task),status=200)
    def put(self,request:HttpRequest,id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('title'):
            task.name = data['title']
        if data.get('description'):
            task.website = data['description']
       

        task.save()

        return JsonResponse(to_dict(task),status=200)
    
    def delete(self,request:HttpRequest,id) -> JsonResponse:
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        task.delete()

        return JsonResponse({'status': 'ok'},status=204)
        
class TaskDoneView(View):
    def post(self,request:HttpRequest,id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        task.done = True
       

        task.save()

        return JsonResponse(to_dict(task),status=200)
    
class TaskUndoneView(View):
    def post(self,request:HttpRequest,id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        task.done = False
       

        task.save()

        return JsonResponse(to_dict(task),status=200)