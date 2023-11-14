from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Article
from .forms import ArticleForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def index(request):
    return render(request, 'main/index1.html')

def about(request):
    return render(request, 'main/about.html')

def metod(request):
    return render(request, 'main/metod.html')

def postuser(request):

    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    height = request.POST.get("height")
    weight = request.POST.get("weight")
    ap_hi = request.POST.get("ap_hi")
    ap_lo = request.POST.get("ap_lo")
    cholesterol = request.POST.get("cholesterol")
    gluc = request.POST.get("gluc")
    smoke = request.POST.get("smoke")
    alco = request.POST.get("alco")
    active = request.POST.get("active")
    cardio = request.POST.get("cardio")

    df = pd.read_csv('main/templates/main/cardio_data_processed.csv')
    df = df.drop(['bp_category', 'id','age', 'bmi'], axis=1)
    df['bp_category_encoded'] = LabelEncoder().fit_transform(df['bp_category_encoded'])

    y = df['bp_category_encoded']
    X = df.drop(['bp_category_encoded'], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=987)

    pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
    pipe.fit(X_train, y_train)

    data = {'gender': [float(gender)],
            'height': [float(height)],
            'weight': [float(weight)],
            'ap_hi': [float(ap_hi)],
            'ap_lo': [float(ap_lo)],
            'cholesterol': [float(cholesterol)],
            'gluc': [float(gluc)],
            'smoke': [float(smoke)],
            'alco': [float(alco)],
            'active': [float(active)],
            'cardio': [float(cardio)],
            'age_years': [float(age)]}
    df_t = pd.DataFrame(data)
    new_predictions = pipe.predict(df_t)
    if new_predictions == 1: d = 'Гипертония 1 стадии'
    if new_predictions == 2: d = 'Гипертония 2 стадии'
    if new_predictions == 3: d = 'Норма'
    if new_predictions == 0: d = 'Повышенное давление'

    if gender == '1': genderout = 'женский'
    if gender == '2': genderout = 'мужской'

    person = Article( name = request.POST.get("name"),
    age = request.POST.get("age"),
    gender = request.POST.get("gender"),
    height = request.POST.get("height"),
    weight = request.POST.get("weight"),
    ap_hi = request.POST.get("ap_hi"),
    ap_lo = request.POST.get("ap_lo"),
    cholesterol = request.POST.get("cholesterol"),
    gluc = request.POST.get("gluc"),
    smoke = request.POST.get("smoke"),
    alco = request.POST.get("alco"),
    active = request.POST.get("active"),
    cardio = request.POST.get("cardio"),
    bp_category = new_predictions)
    person.save()



    output = f"""<div><h2>Имя: {name} </h2><div>
                <div><h2> Возраст:{age} </h2><div>
                <div><h2> Пол:{genderout} </h2><div>
                <div><h2> Диагноз:{d} </h2><div>
                <div> <a href='about'>Данные пациента</a> <div>
                """
    return HttpResponse(output)