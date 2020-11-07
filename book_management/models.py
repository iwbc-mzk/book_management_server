from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=1000)
    author_id = models.ForeignKey('Author',
                                  to_field='author_id',
                                  related_name='author',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    series_id = models.ForeignKey('Series',
                                  to_field='series_id',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    publisher_id = models.ForeignKey('Publisher',
                                     to_field='publisher_id',
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True)
    label_id = models.ForeignKey('Label',
                                 on_delete=models.SET_NULL,
                                 to_field='label_id',
                                 null=True,
                                 blank=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name


class Series(models.Model):
    series_id = models.AutoField(primary_key=True)
    series_name = models.CharField(max_length=1000)
    author_id = models.ForeignKey('Author',
                                  to_field='author_id',
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
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.publisher_name


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=1000)
    publisher_id = models.ForeignKey('Publisher',
                                     to_field='publisher_id',
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
