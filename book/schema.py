import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book
from graphql_jwt.decorators import login_required


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "desc", "author")


class BookQuery(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.Int())

    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())

    @login_required
    def resolve_authors(root, info):
        return Author.objects.all()

    @login_required
    def resolve_author(root, info, id):
        return Author.objects.get(pk=id)

    @login_required
    def resolve_books(root, info):
        return Book.objects.all()

    @login_required
    def resolve_book(root, info, id):
        return Book.objects.get(pk=id)


class AuthorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, name):
        author = Author(name=name)
        author.save()
        return AuthorMutation(author=author)


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, name, id):
        author = Author.objects.get(id=id)
        author.name = name
        author.save()
        return AuthorMutation(author=author)


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id):
        author = Author.objects.get(id=id)
        author.delete()
        return


# class CreateBookMutation(graphene.Mutation):
#     class Arguments:



class BookMutation(graphene.ObjectType):
    create_author = AuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
