# Aqui criamos os metodos GET, POST, PUT e DELETE utilizado um decorator API_VIEW
from app.serializers import TodoSerializer
from app.models import Todo

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all() # pegar todos objetos contido no banco de dados e colocar nessa variavel.
        serializer = TodoSerializer(todo, many=True) #vai se utilizada na hora de dar um GET, vamos lidar com varios objs precisamos definir que serão varios objs
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data) # ele passa para nossa classe serializadora, se a requisição que foi feita está correta
        if serializer.is_valid(): #se for validado a requisição, ele save os dados no banco
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # senão ele apresenta o codigo de erro

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_change_and_delete(request, pk):
    try:
        todo=Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
