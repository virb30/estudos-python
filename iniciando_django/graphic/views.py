from django.shortcuts import render
from scipy.interpolate import interp1d
# import matplotlib.pyplot as plt

from .models import Bomba

# Create your views here.


def index(request):
    bombas = Bomba.objects.all()

    x = [0, 20, 24, 26, 28, 30, 34]
    y = [40.8, 33, 30.3, 28.2, 25.8, 23.2, 18.5]

    cubic = interp1d(x, y, kind='cubic')(29)
    quadratic = interp1d(x, y, kind='quadratic')(23)

    result = round(float(quadratic), 2)

    return render(
        request,
        'index.html',
        {
            'bombas': bombas,
            'cubic': cubic,
            'quadratic': result
        }
    )
