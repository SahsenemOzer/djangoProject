from django.urls import path

from . import views

urlpatterns = (

    # ex:/deneme1/
    path('', views.index, name='index'),
    # ex:/deneme1/5/
    # path('<int:question_id>/',views.detail,name='detail'),
    # ex:/deneme1/5/result/
    # path('<int:question_id>/result/',views.results,name='results'),
    # ex:/deneme1/5/vote/
    # path('<int:question_id>/vote/',views.vote,name='vote'),

)