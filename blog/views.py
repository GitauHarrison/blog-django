from django.shortcuts import render


posts = [
    {
        'author': 'Harry',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'Dec 27, 2022'
    },
    {
        'author': 'Muthoni',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 26, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
