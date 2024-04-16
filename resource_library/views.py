import requests
from django.shortcuts import render


# Create your views here.

def resources(request):
    pass


def dictionary(request):
    if request.method == "POST":
        word = request.POST['word']
        print(word)
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        data = response.json()
        word_json = data.get('word', [])
        if word_json:
            meanings = word_json.get('meanings', [])
            for meaning in meanings:
                print(meaning)
    return None
