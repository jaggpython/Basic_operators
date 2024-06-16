from django.shortcuts import render

def home(request):
    result = None

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')

        if num1 and num2 and operation:
            try:
                num1 = float(num1)
                num2 = float(num2)

                if operation == 'addition':
                    result = num1 + num2
                elif operation == 'subtraction':
                    result = num1 - num2
                elif operation == 'multiplication':
                    result = num1 * num2
                elif operation == 'division':
                    if num2 != 0:
                        result = f"{num1 / num2:.2f}"
                    else:
                        result = "Division by zero"
                else:
                    result = "Invalid operation"
            except (ValueError, TypeError):
                result = "Invalid input"

    return render(request, "index.html", {'result': result})
