from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer
from .models import Food


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/food/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of food'
        },
        {
            'Endpoint': '/food/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/food/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new food with data sent in the post request'
        },
        {
            'Endpoint': '/food/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Return an array of notes'
        },
        {
            'Endpoint': '/food/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting food object'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getFoods(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFood(request, pk):
    foods = Food.objects.get(id=pk)
    serializer = FoodSerializer(foods, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createFood(request):
    data = request.data

    food = Food.objects.create(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        stars=data["stars"],
        image=data["image"],
        meal=data["meal"],
    )
    serializer = FoodSerializer(food, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateFood(request, pk):
    data = request.data

    food = Food.objects.get(id=pk)
    serializer = FoodSerializer(food, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteFood(request, pk):
    food = Food.objects.get(id=pk)
    food.delete()
    return Response("food was deleted!")
