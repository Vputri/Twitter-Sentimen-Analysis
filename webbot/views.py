from django.shortcuts import render
import joblib
import os

my_dir = os.path.dirname(__file__)
vector_file_path = os.path.join(my_dir, 'vektor.sav')
mnb_file_path = os.path.join(my_dir, 'MNB.sav')

def index(request):
    return render(request, 'webbot/index.htm')

def bot_search(request):
    query = request.GET.get('query')
    vektor = joblib.load(vector_file_path)
    model = joblib.load(mnb_file_path)
    result = model.predict(vektor.transform([query]))
    if (result == [2]) :
        ans = "negatif"
    elif (result == [1]) :
        ans = "positif"
    else:
        ans = 'Nothing'

    return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
