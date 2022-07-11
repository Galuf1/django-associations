from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')


# 1 user - many posts *
# 1 user - many comments *
# 1 post - many comments *
# 1 post - 1 User
# 1 comment - 1 user
# 1 coment - 1 post
