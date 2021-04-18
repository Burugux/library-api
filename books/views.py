from django.shortcuts import render
from books.models import Book, Author, BookInstance, Genre, Language
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Get all languages supported and display as list

    dbQuery = Language.objects.all()
    result = dbQuery[0]

    for word in dbQuery[1:]:
        result = "%s-%s" % (result, word)

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'languages_list': result,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
