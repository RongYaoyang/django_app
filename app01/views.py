from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def questionnaire(request):
    if request.method == 'GET':
        questionnaires_list = models.QuestionPapers.objects.values('title','student_class__title',
                                                                   'student_class__id','num',
                                                                   'student_class__student_num','id')
        # print(questionnaires_list)
        return render(request, 'questionnaire.html',{'data':questionnaires_list})
    else:
        return HttpResponse('<h1>404 Not Found</h1>')



def edit_questionnaire(request,nid=None):
    if request.method == 'GET':
        # print(nid)
        if nid:
            questionnaire = models.QuestionPapers.objects.filter(id=nid)
            if questionnaire:
                questions = questionnaire.values('paper_question__title','paper_question__question_type__title')
                '''
                'paper_question__question_type__choice_type','paper_question__question_type__score_type',
                                                 'paper_question__question_type__text_type'
                '''
                select_type = models.Type.objects.all()
                select_single = models.Type_Choice.objects.all()
                # print(questions.first().get('paper_question__title'))
                if questions.first().get('paper_question__title'):
                    return render(request, 'edit.html',{'data':questions,'type':select_type,'select':select_single})
                else:
                    return render(request, 'edit.html')
        return HttpResponse('<h1>404 Not Found</h1>')

    else:
        return HttpResponse('<h1>404 Not Found</h1>')