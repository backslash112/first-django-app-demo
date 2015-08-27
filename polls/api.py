__author__ = 'carl'

from tastypie.resources import ModelResource
from .models import Question
from tastypie import fields

class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'

class EntryResource(ModelResource):
    question = fields.ForeignKey(QuestionResource, 'question')

    class Meta:
        querySet = Question.objects.all()
        resource_name = 'entry'
