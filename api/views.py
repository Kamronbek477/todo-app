from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpRequest
from .models import Task
from django.contrib.auth.models import User
import json

from django.contrib.auth.hashers import make_password

def to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
        "created": task.created,
        "updated": task.updated,
        "user": task.user.username,
    }

def to_dict_user(user: User) -> dict:
    return {
        "id": user.id,
        "username": user.username,
        "password": user.password,
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

        task.title = data.get('title', task.title)
        # if data.get('title'):
        #     task.title = data['title']
        if data.get('description'):
            task.description = data['description']
       

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


class UserListView(View):
    def get(self, request: HttpRequest, id: int = None) -> JsonResponse:
        if id:
            try:
                user = User.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'object does not exist!'})
            return JsonResponse(to_dict_user(user), status=200)
        users = User.objects.all()
        return JsonResponse([to_dict_user(user) for user in users], safe=False, status=200)

    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = request.body.decode()
        data = json.loads(data)

        if data.get('username') == None:
            return JsonResponse({'status': 'username is required.'})
        
        if data.get('password') == None:
            return JsonResponse({'status': 'password is required.'})

        user = User.objects.create(
            username=data['username'],
            password=make_password(data['password'])
        )
        # user.set_password(data['password'])
        user.save()

        return JsonResponse(to_dict_user(user))
        