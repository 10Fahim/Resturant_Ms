from django.shortcuts import render, redirect

from RestaurantAPP.models import Food_items, Cuisine


# Create your views here.
def home(request):
      return render(request, 'Demo.html')


def list(request):
        foods = Food_items.objects.all()
        return render(request, 'Food_list.html', {"foods": foods})


def additems(request):
    if request.method == "POST":
        f = Food_items()
        f.item_name = request.POST["text1"]
        f.type = request.POST["radio1"]
        f.timing = request.POST["select2"]
        f.price = request.POST["num1"]
        f.cuisine_name = Cuisine.objects.get(cuisine_name=request.POST["select1"])
        f.save()
        return redirect(list)
    else:
        cuisines = Cuisine.objects.all()
        data = {'cuisine': cuisines}
        return render(request, "add_item.html", data)


def updatefooddetails(request, id):
    f = Food_items.objects.get(id=id)
    if request.method == "POST":
        f.item_name = request.POST["text1"]
        f.type = request.POST["radio1"]
        f.timing = request.POST["select2"]
        f.price = request.POST["num1"]
        f.cuisine_name = Cuisine.objects.get(cuisine_name=request.POST["select1"])
        f.save()
        return redirect(list)
    else:
        c = Cuisine.objects.all()
        data = {'food': f, 'cuisine': c}
        return render(request, "update_details.html", data)


def delete_item(request, id):
    f = Food_items.objects.get(id=id)
    f.delete()
    return redirect(list)


def displayfun(request):
    if request.method == "GET":
        cuisine_name = request.GET.get("name")
        if "name":
            data = Food_items.objects.filter(cuisine_name=cuisine_name).exists()
            return render(request, 'display.html', {'data': data})
        else:
            return render(request, 'display.html', {'msg': "No Items now!"})
    return render(request, 'Demo.html')
