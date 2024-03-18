from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True)
    death_year = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField()

    class Meta:
        db_table = 'books_book'

class BookAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_authors'

class BookBookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_bookshelves'

class BookLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_languages'

class BookSubjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_subjects'

class Bookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

class Format(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_format'

class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        db_table = 'books_language'

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'books_subject'