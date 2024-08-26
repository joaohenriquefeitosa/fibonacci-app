from rest_framework.response import Response
from .services.fibonacci import generate_fibonacci
from rest_framework.decorators import api_view


@api_view(['GET'])
def fibonacci(request):
    try:
        n = int(request.GET.get('n', ''))

        if n < 0:
            return Response({"error": "'n' must be a non-negative integer."}, status=400)
        
        return Response({"result": generate_fibonacci(n)})
    
    except ValueError:
        return Response({"error": "'n' must be an integer."}, status=400)
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)
