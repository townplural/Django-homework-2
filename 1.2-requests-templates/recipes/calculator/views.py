from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    # return HttpResponse('qq')
    context = {
        'recipe': {
            'яйца, шт': 2 * servings,
            'молоко, л': 0.1 * servings,
            'соль, ч.л.': 0.5 * servings
        }
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    # return HttpResponse('qq')
    context = {
        'recipe': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        }
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    # return HttpResponse('qq')
    context = {
        'recipe': {
            'хлеб, ломтик': 2 * servings,
            'колбаса, ломтик': 0.1 * servings,
            'сыр, ломтик': 0.5 * servings,
            'помидор, ломтик': 1,
        }
    }
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

