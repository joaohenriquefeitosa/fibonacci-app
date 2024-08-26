from rest_framework.response import Response
from .services.fibonacci import check_fibonacci
from rest_framework.decorators import api_view


@api_view(['GET'])
def fibonacci(request):
    try:
        n = int(request.GET.get('n', ''))

        if n <= 0:
            return Response({"error": "'n' must be a non-negative integer and greater than 0."}, status=400)
        
        return Response({"result": check_fibonacci(n)})
    
    except ValueError:
        return Response({"error": "'n' must be an integer."}, status=400)
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)
