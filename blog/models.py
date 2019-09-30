from django.db import models
from django.utils import timezone
from uuid import uuid4
import os


# def path_and_rename(instance, filename):
#     upload_to = 'post_imgs'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.pk:
#         filename = '{}.{}'.format(instance.pk, ext)
#     else:
#         # set filename as random string
#         filename = '{}.{}'.format(uuid4().hex, ext)
#     # return the whole path to the file
#     return os.path.join(upload_to, filename)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(
                                upload_to = "post_imgs",
                                max_length=255,
                                null=True,
                                blank=True
                                )

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title, filename)


class Comment(models.Model):
    post = models.ForeignKey(
                            'blog.Post',
                            on_delete=models.CASCADE,
                            related_name='comments'
                            )

    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1500)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
