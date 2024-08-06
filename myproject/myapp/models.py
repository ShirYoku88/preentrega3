from django.db import models

class MartialArtsStudent(models.Model):
    DISCIPLINE_CHOICES = [
        ('Judo', 'Judo'),
        ('Karate', 'Karate'),
        ('Aikido', 'Aikido'),
        ('Kendo', 'Kendo'),
        ('Jujitsu', 'Jujitsu')
    ]
    
    name = models.CharField(max_length=100)
    belt_color = models.CharField(max_length=50)
    age = models.IntegerField()
    discipline = models.CharField(max_length=50, choices=DISCIPLINE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.discipline})"
