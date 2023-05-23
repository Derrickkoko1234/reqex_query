import re
from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'POST':
        pattern = request.POST.get('pattern')
        text = request.POST.get('text')
        option = request.POST.get('option')

        matches = []

        if option == 'full_match':
            matches = re.findall(pattern, text)
        elif option == 'first_match':
            match = re.search(pattern, text)
            if match:
                matches.append(match.group())

        context = {
            'pattern': pattern,
            'text': text,
            'option': option,
            'matches': matches,
        }
        return render(request, 'result.html', context)

    return render(request, 'index.html')
