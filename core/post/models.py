from django.db import models

# Create your models here.
from core.abstract.models import AbstractManager,AbstractModel

class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    author = models.ForeignKey(to='core_user.User',on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self) -> str:
        return f'{self.author.name}'


    class Meta:
        db_table = "'core.post'" 