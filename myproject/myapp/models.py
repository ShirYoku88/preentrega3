from django.db import models

class JudoStudent(models.Model):
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class KarateStudent(models.Model):
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class AikidoStudent(models.Model):
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class KendoStudent(models.Model):
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class JujitsuStudent(models.Model):
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


