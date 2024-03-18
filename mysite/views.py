from django.shortcuts import render

# Create your views here.
from .models import Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject
from .serializers import AuthorSerializer,BookSerializer,BookAuthorsSerializer,BookBookshelvesSerializer,BookLanguagesSerializer,BookSubjectsSerializer,BookshelfSerializer,FormatSerializer,LanguageSerializer,SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator


@api_view(['GET'])
def get_book_data(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book_shelf(request):
    books = BookBookshelves.objects.all()
    serializer = BookBookshelvesSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_shelf(request):
    books = BookBookshelves.objects.all()
    serializer = BookBookshelvesSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_format(request):
    books = Format.objects.all()
    serializer = FormatSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_language(request):
    books = Language.objects.all()
    serializer = LanguageSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_subject(request):
    books = Subject.objects.all()
    serializer = SubjectSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book_authors(request):
    books = Auther.objects.all()
    serializer = AuthorSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def filter_books(request):
    # title = request.data['title']
    # author_info = request.data['author_info']
    # genre = request.data['genre']
    # language = request.data['language']
    # subjects = request.data['subjects']
    # bookshelves = request.data['bookshelves']
    title = request.data.get('title', None)
    author_info = request.data.get('author_info', None)
    genre = request.data.get('genre', None)
    language_req = request.data.get('language', None)
    subjects = request.data.get('subjects', None)
    bookshelves = request.data.get('bookshelves', None)
    mimetype = request.data.get('mimetype', None)
    gutenberg_id = request.data.get('gutenberg_id', None)
    pageno = request.data.get('pageno', None)
    
    
    
    queryset = Book.objects.all()

    if title:
        queryset = queryset.filter(title__icontains=title)
        
    if mimetype:
        queryset = queryset.filter(media_type__icontains=mimetype)
    
    if gutenberg_id:
        queryset = queryset.filter(gutenberg_id__icontains=gutenberg_id)
    
    

    if author_info:
        queryset = queryset.filter(bookauthors__author__name__icontains=author_info)

   

    if language_req:
        lang_ids = list(Language.objects.filter(code=language_req).values_list('id', flat=True))
       
        queryset = queryset.filter(booklanguages__language_id__in=lang_ids)

    if subjects:
        subject_ids = list(Subject.objects.filter(name__icontains=subjects).values_list('id', flat=True))
        queryset = queryset.filter(booksubjects__subject_id__in=subject_ids)

    if bookshelves:
      
        # queryset = queryset.filter(bookbookshelves__bookshelf__name__icontains=bookshelves)
        bookshelf_ids = list(Bookshelf.objects.filter(name__icontains=bookshelves).values_list('id', flat=True))
        
        queryset = queryset.filter(bookbookshelves__bookshelf_id__in=bookshelf_ids)
    queryset = queryset.order_by('-download_count')
    count = queryset.count()
    paginator = Paginator(queryset,20)
    if pageno :
        page = paginator.get_page(pageno)
        if paginator.num_pages < pageno:
            return Response({"message":"No more pages"})
    else:
        page = queryset
    
    serializer = BookSerializer(page , many=True)
    return Response({"count":count,"data":serializer.data})






