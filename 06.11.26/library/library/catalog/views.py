from datetime import datetime

from django.http import Http404
from django.shortcuts import render

BOOKS = [
    {
        'id': 1,
        'title': 'Колобок',
        'content': 'Сказка учит тому, что излишняя самоуверенность, хвастовство и доверчивость к лести могут привести к беде, а также напоминает о важности слушать старших.',
        'published_date': datetime(1844, 11, 6),
        'author': 'Народ',
    },
    {
        'id': 2,
        'title': 'Война и мир',
        'content': 'Историческая судьба русского народа, Отечественная война 1812 года и «мысль народная» (идея о том, что историю двигает не воля отдельных великих полководцев, а жизнь и поступки миллионов простых людей',
        'published_date': datetime(1869, 12, 16),
        'author': 'Роман, Лев Толстой',
    },
]


def book_list(request):
    """Список книг каталога."""
    return render(request, 'catalog/book_list.html', {'books': BOOKS})


def book_detail(request, book_id):
    """Детальная страница книги."""
    book = next((item for item in BOOKS if item['id'] == book_id), None)
    if book is None:
        raise Http404('Книга не найдена')
    return render(request, 'catalog/book_detail.html', {'book': book})


def about(request):
    return render(request, 'catalog/about.html')
