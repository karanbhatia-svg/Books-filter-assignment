from rest_framework import serializers
from .models import Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthors
        fields = '__all__'

class BookBookshelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBookshelves
        fields = '__all__'

class BookLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLanguages
        fields = '__all__'

class BookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubjects
        fields = '__all__'

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = '__all__'

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
