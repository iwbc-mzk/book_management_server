from django.db import models
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey('Author',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    series = models.ForeignKey('Series',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    publisher = models.ForeignKey('Publisher',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    label = models.ForeignKey('Label',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    medium = models.ForeignKey('Medium',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    already_read = models.BooleanField(default=False)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_by')
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created_at:
            self.created_at = now

        self.updated_at = now

        super(Book, self).save(*args, **kwargs)


class Author(models.Model):
    author_name = models.CharField(max_length=1000)
    how_to_read = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name


class Series(models.Model):
    series_name = models.CharField(max_length=1000)
    author = models.ForeignKey('Author',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.series_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.publisher_name


class Label(models.Model):
    label_name = models.CharField(max_length=1000)
    publisher = models.ForeignKey('Publisher',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.label_name


class Medium(models.Model):
    medium_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)
