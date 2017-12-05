from django.db import models

# Create your models here.


class Person(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    _type = models.IntegerField(verbose_name='身份')#1老师2学生


class Teacher(Person):
    name = models.CharField(max_length=64,verbose_name='姓名')


class Student_Class(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=64,verbose_name='班级名')
    student_num = models.IntegerField(verbose_name='学生数')
    teacher = models.ForeignKey(verbose_name='班主任',to='Teacher')


class Student(Person):
    '''
    学生表
    '''
    name = models.CharField(max_length=32,verbose_name='姓名')
    _class = models.ForeignKey(to='Student_Class',verbose_name='对应班级')
    questions = models.ManyToManyField(verbose_name='关联问卷',to='QuestionPapers',related_name='QuestionPapers_student')


class QuestionPapers(models.Model):
    '''
    问卷表
    '''
    title = models.CharField(max_length=64,verbose_name='问卷名')
    _class = models.ForeignKey(verbose_name='关联班级',to='Student_Class',related_name='QuestionPapers_class')
    num = models.IntegerField(verbose_name='参与人数',default=0)
    url = models.CharField(max_length=64, verbose_name='学生填写问卷地址')


# class QuestionPapers_To_Student(models.Model):
#     '''
#     中介模型    问卷-----学生表  联合唯一
#     '''
#     question_paper_id = models.ForeignKey(to='QuestionPapers')
#     student_id = models.ForeignKey(to='Student')
#
#     class Meta:
#         unique_together = [
#             ('question_paper_id','student_id',),
#         ]


class Type_Score(models.Model):
    '''
    类型表中  分数表
    '''
    score = models.IntegerField(verbose_name='分数')


class Type_Choice(models.Model):
    '''
    类型表中   单选表
    '''
    title = models.CharField(max_length=32,verbose_name='选项')
    score = models.IntegerField(verbose_name='分数')


class Type_Text(models.Model):
    '''
    类型表中   评价表
    '''
    title = models.TextField(verbose_name='内容')


class Type(models.Model):
    '''
    类型表
    '''
    title = models.CharField(max_length=32,verbose_name='问题类型')
    type_score = models.OneToOneField(to='Type_Score',null=True,blank=True,related_name='score_type')
    type_choice = models.OneToOneField(to='Type_Choice',null=True,blank=True, related_name='choice_type')
    type_text = models.OneToOneField(to='Type_Text',null=True,blank=True, related_name='text_type')


class Questions(models.Model):
    '''
    问题表
    '''
    title = models.CharField(max_length=64,verbose_name='问题')
    _type = models.OneToOneField(to='Type',related_name='type_question')
    question_paper = models.ForeignKey(to='QuestionPapers', related_name='paper_question')


class Answer(models.Model):
    student = models.ForeignKey(verbose_name='关联学生', to='Student',related_name='answer_student')
    question = models.ForeignKey(verbose_name='关联试题',to='Questions',related_name='answer_question')
    score = models.IntegerField(verbose_name='分数', null=True,blank=True)
    choice = models.ForeignKey(verbose_name='单选',to='Type_Choice',related_name='answer_choice',null=True,blank=True)
    content = models.ForeignKey(verbose_name='评价',to='Type_Text',related_name='answer_content',null=True,blank=True)