from django.urls import path     
from . import views
urlpatterns = [
    # RENDER PAGES
    path('', views.index),
    path('book/<int:book_id>', views.book_id),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.author_id),
    # REDIRECT PAGES
    path('create_book', views.create_book),
    path('create_author', views.create_author),
    path('adding_book_to_author', views.adding_book_to_author),
]
