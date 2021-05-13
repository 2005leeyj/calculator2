from django.shortcuts import render

def firstpage(request):
    return render(request, "firstpage.html")

def result(request):
    input1 = int(request.GET['firstnum'])
    input2 = int(request.GET['secondnum'])
    calc = request.GET['operator']

    if calc == "add":
        result = input1 + input2
    elif calc == "sub":
        result = input1 - input2
    elif calc == "mul":
        result = input1 * input2
    elif calc == "div" and input2 == 0:
        result = "division by zero"
    else:
        result = input1 / input2

        return render(request, "result.html", {'result':result})