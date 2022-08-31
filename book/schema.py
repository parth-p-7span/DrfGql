import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "desc", "author")


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.Int())

    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())

    def resolve_authors(root, info):
        return Author.objects.all()

    def resolve_author(root, info, id):
        return Author.objects.get(pk=id)

    def resolve_books(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        return Book.objects.get(pk=id)


schema = graphene.Schema(query=Query)
