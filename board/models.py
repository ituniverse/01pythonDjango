from django.db import models
from django.utils import timezone


#게시글
class Board(models.Model):
    writer = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    modify_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.modify_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# 댓글
class Comment(models.Model):
    board = models.ForeignKey('board.Board', related_name='comments')
    writer = models.CharField(max_length=200)
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.contents

