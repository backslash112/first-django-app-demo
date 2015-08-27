from django.conf.urls import url, include
from . import views
from .api import EntryResource, QuestionResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(EntryResource())

urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #ex : polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^blog/', include('polls.urls')),
    # ex: http://127.0.0.1:8000/polls/api/v1/question/?format=json
    url(r'^api/', include(v1_api.urls)),
]
