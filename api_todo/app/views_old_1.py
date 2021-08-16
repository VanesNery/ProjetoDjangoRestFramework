#Aqui separamos os metodos por pagina para cada class

from app.serializers import TodoSerializer
from app.models import Todo

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoListAndCreate(APIView):

    def get(self, request):
        todo = Todo.objects.all() # pegar todos objetos contido no banco de dados e colocar nessa variavel.
        serializer = TodoSerializer(todo, many=True) #vai se utilizada na hora de dar um GET, vamos lidar com varios objs precisamos definir que serão varios objs
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data) # ele passa para nossa classe serializadora, se a requisição que foi feita está correta
        if serializer.is_valid(): #se for validado a requisição, ele save os dados no banco
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # senão ele apresenta o codigo de erro

class TodoDetailChangeAndDelete(APIView):

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
