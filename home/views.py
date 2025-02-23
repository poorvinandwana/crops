from django.shortcuts import render
from .models import Crop

def recommend_crop(request):
    if request.method == "POST":
        
        nitrogen = float(request.POST.get("nitrogen"))
        phosphorus = float(request.POST.get("phosphorus"))
        potassium = float(request.POST.get("potassium"))
        ph = float(request.POST.get("ph"))
        temperature = float(request.POST.get("temperature"))
        soil_type = request.POST.get("soil_type") 
        moisture_content = request.POST.get("moisture")
        salinity = request.POST.get("salinity")

        crops = Crop.objects.filter(
        nitrogen_min__lte=nitrogen, nitrogen_max__gte=nitrogen,
        phosphorus_min__lte=phosphorus, phosphorus_max__gte=phosphorus,
        potassium_min__lte=potassium, potassium_max__gte=potassium,
        ph_min__lte=ph, ph_max__gte=ph,
        temperature_min__lte=temperature, temperature_max__gte=temperature,
        soil_type__iexact=soil_type,  
        moisture_content=moisture_content,
        salinity=salinity
    ).distinct()


        return render(request, "result.html", {"crops": crops})

    return render(request, "index.html")

