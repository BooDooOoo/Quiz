from django.db import models


class Polls(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название опроса')
    description = models.CharField(max_length=300, verbose_name='Описание опроса')
    date_start = models.DateField(verbose_name='Дата старта')
    date_stop = models.DateField(verbose_name='Дата окночания')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Questions(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст вопроса')

    TYPE_QUESTION_LIST = ((None, 'Выберите тип вопроса'),
                          ('text', 'Ответ текстом'),
                          ('one_choice', 'Ответ с выбором одного варианта'),
                          ('many_choice', 'Ответ с выбором нескольких вариантов'))
    type_question = models.CharField(max_length=11, choices=TYPE_QUESTION_LIST, verbose_name='Тип вопроса')

    polls = models.ForeignKey(to=Polls, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст ответа')
    questions = models.ForeignKey(to=Questions, on_delete=models.CASCADE, related_name='choice')


class Users(models.Model):
    last_date_login = models.DateField(auto_now=True)


class UserChoices(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='choice')
    question = models.ForeignKey(to=Questions, on_delete=models.CASCADE, related_name='user_choice')
    text_choice = models.CharField(max_length=200)

