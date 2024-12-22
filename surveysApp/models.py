from django.db import models


class Questions(models.Model):
    question = models.CharField(max_length=120)

    def __str__(self):
        return self.question


class EmailAnswer(models.Model):
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email


class OpenAnswer(models.Model):
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Options(models.Model):
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    optionText = models.CharField(max_length=120)

    def __str__(self):
        return self.optionText
