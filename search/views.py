from django.shortcuts import render
from .lookup import perform_lookup

def search_view(request):
    query_params = request.GET
    q = query_params.get('q')
    context = {}
    if q is not None:
        results = perform_lookup(q, internal_sort=True)
        context['results'] = results
        context['query'] = q
    return render(request, 'search.html', context)