from django.db import models

# Create your models here.
class Note(models.Model):
    note_id = models.AutoField
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
