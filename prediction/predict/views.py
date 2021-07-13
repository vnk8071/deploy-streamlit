from django.shortcuts import render
import os
from django.http import JsonResponse
from .models import PredResults

# Create your views here.
def predict(request):
    return render(request, 'pages/predict.html')

def predict_chances(request):
    if request.POST.get('action') == 'post':
        age = float(request.POST.get('age'))
        bmi = float(request.POST.get('bmi'))
        glucose = float(request.POST.get('glucose'))

        model = os.joblib.load('./model/Logimodel.pkl')
        result = model.predict([[0, age, 0, 0, 0, 0, bmi, glucose]])

        return result
