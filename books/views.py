from django.shortcuts import render
from books.models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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

     # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'languages_list': result,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

# scenerio one


def getCharges(request):
    """View function for calculating libraby charges"""
    books_loaned = BookInstance.objects.filter(borrower=request.user).filter(
        status__exact='o')

    book_charges = 0
    days = 0
    for b in books_loaned:
        dt = (b.due_back - b.borrowed)
        days += dt.days
        book_charges = days * 1
    return book_charges


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'books/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

    def get_context_data(self, **kwargs):
        context = super(LoanedBooksByUserListView,
                        self).get_context_data(**kwargs)
        context['book_charges'] = getCharges(self.request)
        return context

class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author