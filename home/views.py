from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    print("Request: ", request)
    return render(
        request,
        "index.html",
        context={
            "list": [1, 2, 3],
            "information": [
                {"name": "ram", "rank": 1, "first": True, "grade": 85.4546468},
                {"name": "harry", "rank": 2, "first": False, "grade": 75.4546468},
                {"name": "shayam", "rank": 3, "first": False, "grade": 65.4546468},
                {"name": "Ravan", "rank": 4, "first": False, "grade": 55.4546468},
                {"name": "lucy", "rank": 5, "first": False, "grade": 45.4546468},
            ],
            "show": True,
            "sorted": True,
        },
    )


def calculation_view(request):
    print("request method: ", request.method)
    if request.method == "GET":
        return render(request, "calc.html")
    else:
        print("form datas: ", request.POST)
        result = int(request.POST.get("num1")) + int(request.POST.get("num2"))
        return render(request, "calc.html", context={"result": result})
