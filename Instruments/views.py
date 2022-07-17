from django.shortcuts import render, redirect
from .models import BannerItems, Category, Partner, Instrument, InstrumentModel
from django.views.generic import ListView, DetailView
from .forms import SearchForm


def about(request):
    return render(request, 'Instruments/about.html', {'partners': Partner.objects.filter(status='p')})


class HomeListView(ListView):
    template_name = 'Instruments/home.html'
    queryset = BannerItems.objects.order_by('-date').filter(status='p')
    context_object_name = 'BannerItems'


class ProductView(ListView):
    template_name = 'Instruments/products.html'
    queryset = Instrument.objects.filter(status='p')
    context_object_name = 'instruments'


class CategoryView(ListView):
    template_name = 'Instruments/products.html'
    context_object_name = 'filtred_Instruments'

    def get_queryset(self):
        queryset = Instrument.objects.filter(instrument_category__slug=self.kwargs['slug'],
                                             status='p').order_by('created_at')
        return queryset


class InstrumentView(DetailView):
    queryset = Instrument.objects.filter(status='p')
    context_object_name = 'instruments'
    template_name = 'Instruments/InstrumentView.html'


class ModelDetailView(DetailView):
    queryset = InstrumentModel.objects.all()
    context_object_name = 'models'
    template_name = 'Instruments/modelview.html'


class AllModelsDetailView(DetailView):
    queryset = Instrument.objects.all()
    context_object_name = 'instruments'
    template_name = 'Instruments/models_all.html'


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return render(request, 'Instruments/products.html', {
                'instruments': [i for i in Instrument.objects.all() if
                                request.POST['search'].lower() in i.name.lower()]
            })
    return redirect('products')
