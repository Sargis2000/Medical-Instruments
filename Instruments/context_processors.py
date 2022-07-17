from .models import Category


def get_categories(request):
    return {'categories': Category.objects.order_by('-date').filter(status='p')}
