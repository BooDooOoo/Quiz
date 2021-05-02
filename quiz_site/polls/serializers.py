from rest_framework import serializers
from .models import *


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = Questions
        fields = ('id', 'text', 'type_question', 'choice')


class PollQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Polls
        fields = ('id', 'questions')


class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = ('id', 'title', 'description', 'date_start', 'date_stop')


class UserChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserChoices
        fields = ('user', 'question', 'text_choice')


class CompletedUserChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserChoices
        fields = ('question', 'text_choice')


class CompletedQuestionSerializer(serializers.ModelSerializer):
    user_choice = CompletedUserChoiceSerializer(many=True)

    class Meta:
        model = Questions
        fields = ('text', 'user_choice')


class CompletedPollsSerializer(serializers.ModelSerializer):
    questions = CompletedQuestionSerializer(many=True)

    class Meta:
        model = Polls
        fields = ('title', 'questions')