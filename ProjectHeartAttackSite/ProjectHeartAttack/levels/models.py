from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Levels(models.Model):
    _EASY = "Easy"
    _NORMAL = "Normal"
    _HARD = "Hard"
    _EXPERT = "Expert"
    _EXPERTPLUS = "Expert+"

    _DIFFCULTY = [
        (_EASY, "Easy"),
        (_NORMAL, "Normal"),
        (_HARD, "Hard"),
        (_EXPERT, "Expert"),
        (_EXPERTPLUS, "Expert+"),
    ]

    name_level = models.CharField(max_length=20, verbose_name='Name levels')
    rating = models.IntegerField(default=0, verbose_name='Reating')
    author_level = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE) 
    diffculty = models.CharField(choices=_DIFFCULTY, max_length=20, verbose_name='Diffcuty')
    content = models.TextField(verbose_name='Content', max_length=1024)
    levels_file = models.FileField(upload_to='levels_file/%Y/%m/%d/', verbose_name="Levels file", blank=True) # не забыть поставить blank=false после дебага
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    preview = models.ImageField(upload_to='preview_levels/%Y/%m/%d/', verbose_name='Preview image', blank=True)
    level_by = models.CharField(max_length=150, verbose_name="Level By", null=True)
    url_getsong = models.CharField(max_length=1000, verbose_name="Song url", null=True, blank=True)
    url_steam_workshop_author = models.CharField(max_length=1000, verbose_name='Creator Workshop', null=True, blank=True)
    follow_artist = models.CharField(max_length=1000, verbose_name='Follow Artist', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    comments = GenericRelation('comment')

    def __str__(self):
        return self.name_level

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels database'
        ordering = ['-created_at']

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Author comment", on_delete=models.CASCADE)
    context = models.TextField(verbose_name='Text comment')
    parent = models.ForeignKey(
        'self',
        verbose_name='Parent comment',
        blank=True,
        null=True,
        related_name='comment_children',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    like_count = models.IntegerField(default=0, verbose_name="Like")
    Dislike_count = models.IntegerField(default=0, verbose_name="Dislike")
    heart_comments = models.BooleanField(default=False, verbose_name="Heart")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Date craeted comments")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


