from django.db import models


class Author(models.Model):
    """
    Model representing the author of a bulletin board post.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model representing a bulletin board post.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title