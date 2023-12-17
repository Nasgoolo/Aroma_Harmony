from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'page'

    def __str__(self):
        return self.title
