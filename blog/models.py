from django.db import models # type: ignore

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    is_validate=models.BooleanField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body}'    

