from django.db import models

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

    name_level = models.CharField(max_length=120, verbose_name='Name levels')
    rating = models.IntegerField(default=0, verbose_name='Reating')
    autthor_level = models.CharField(max_length=80, verbose_name='Author') # Времмено побудет charfield
    diffculty = models.CharField(choices=_DIFFCULTY, max_length=20, verbose_name='Diffcuty')
    content = models.TextField(verbose_name='Content')
    levels_file = models.FileField(upload_to='levels_file/%Y/%m/%d/', verbose_name="Levels file")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    preview = models.ImageField(upload_to='preview_levels/%Y/%m/%d/', verbose_name='Preview image', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.name_level

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels database'
        ordering = ['-created_at']


# id - INT
# level_name - Varchar
# rating - int
# autthor_level - varchar
# diffculty - charField
# content - Text
# file - file
# created_at - datatime
# update_at - datatime
# preview - Image
# is_published - Boolean
