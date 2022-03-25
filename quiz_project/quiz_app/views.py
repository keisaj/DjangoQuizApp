from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth import login, logout, authenticate

from .serializers import UserSerializer, QuestionSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.


class APIOverviewAPIView(APIView):

    def get(self, request):
        api_urls = {
            'Question List': '/question-list/',
            'Detail View': '/question-detail/<str:id>/',
        }
        return Response(api_urls)


class QuestionsAPIView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class QuestionDetailAPIView(APIView):


    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        question = self.get_object(id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, id):
        question = self.get_object(id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        question = self.get_object(id)
        question.delete()

        return Response('Question succsesfully deleted!')

