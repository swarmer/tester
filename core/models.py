from django.db import models
from django.contrib import auth


class Test(models.Model):
    owner = models.ForeignKey(auth.models.User)
    name = models.CharField(max_length=30)
    source = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for question in self.question_set.all():
            question.delete()

        for line in self.source.splitlines():
            self.question_set.create(test=self, name=line)


class Question(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s' % (self.test, self.name)
