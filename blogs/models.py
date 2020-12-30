from django.db import models

class BlogPost(models.Model):
    """A Blog user post"""
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     """Return a string represention of the model."""
    #     return f"{self.title}  --  {self.text}"

    def __str__(self):
        """"""
        return self.title
