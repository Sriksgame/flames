
from django.shortcuts import render

def index(request):
    return render(request, 'flames_app/index.html')

def flames_logic(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)

    count = len(name1 + name2)
    flames = list("FLAMES")
    i = 0
    while len(flames) > 1:
        i = (i + count - 1) % len(flames)
        flames.pop(i)
    return flames[0]

def result(request):
    if request.method == 'POST':
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        result_map = {
            'F': 'Friends 💛',
            'L': 'Love ❤️',
            'A': 'Affection 🧡',
            'M': 'Marriage 💍',
            'E': 'Enemies 💢',
            'S': 'Siblings 💖'
        }
        outcome = flames_logic(name1, name2)
        result_text = result_map.get(outcome, "Unknown")
        return render(request, 'flames_app/result.html', {
            'name1': name1,
            'name2': name2,
            'result': result_text
        })
    return render(request, 'flames_app/index.html')
