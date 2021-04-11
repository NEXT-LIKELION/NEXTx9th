from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')


def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(" ", ""))
    return render(request, 'result.html', {
        'total_len': total_len,
        'text': text,
        'no_blank_len':no_blank_len,
         })