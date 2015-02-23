from django.db import models

class Blog(models.Model):
    """
        The model for blogs.  This is the docstring for it.
        Automatic PEP8 checking can be annoying for
        something this simple.
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    class Meta:
        """
            Blogs should be ordered by date published
        """
        ordering = ('title',)

class Tag(models.Model):
    """
        Categories that Blog Posts can be in
    """
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Blog)

    def __unicode__(self):
        return self.name

    class Meta:
        """
            Sort Tags By Name.
        """
        ordering = ('name',)
