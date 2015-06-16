from django.db import models
from django.contrib import auth
from django.core import validators


class Test(models.Model):
    owner = models.ForeignKey(auth.models.User)
    name = models.CharField(max_length=30, validators=[validators.validate_slug])
    description = models.CharField(max_length=200, blank=True)
    source = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for question in self.question_set.all():
            question.delete()

        for i, line in enumerate(self.source.splitlines()):
            index = i + 1
            self.question_set.create(test=self, name=line, index=index)


class Question(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=200)
    index = models.IntegerField()

    class Meta:
        ordering = ['index']

    def __str__(self):
        return '%s - %d. %s' % (self.test, self.index, self.name)
