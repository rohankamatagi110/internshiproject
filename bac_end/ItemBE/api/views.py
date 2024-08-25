from rest_framework.decorators import api_view  # Import the api_view decorator
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item
from .generate_referral_code import generate_referral_code
from .unique_SKU import is_sku_unique

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['POST'])
def add_items(request):
    item_data = request.data

    # Use .filter() to retrieve all items with the same SKU
    existing_items = Item.objects.filter(SKU=item_data['SKU'])
    
    if existing_items.exists():
        # Handle the case where multiple items with the same SKU were found
        # You might want to log this and decide how to handle it
        return Response({"message": "Multiple items with the same SKU found."})

    item_serializer = ItemSerializer(data=item_data)
    
    if item_serializer.is_valid():
        item = item_serializer.save()
        # Generate referral code
        generate_referral_code(item)
        return Response(item_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def add_items(request):
#     item_data = request.data
#     # Remove spaces from SKU and convert it to lowercase
#     item_data['SKU'] = item_data['SKU'].replace(" ", "").lower()

#     existing_item = is_sku_unique(item_data)

#     if existing_item:
#         return Response({"message": "Item with the same SKU already exists."}, status=status.HTTP_409_CONFLICT)
    
    

#     item_serializer = ItemSerializer(data=item_data)
#     if item_serializer.is_valid():
#         item = item_serializer.save()
#         generate_referral_code(item)
#         return Response(item_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_items(request):
     
     
    
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
 
   
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
        print(items)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['PUT'])
# def update_items(request, pk):
#     try:
#         item = Item.objects.get(pk=pk)
#     except Item.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

    
#     if request.method == 'PUT':
#         # Handle PUT request (update amount)
#         item_data = request.data

#     serializer = ItemSerializer(instance=item, data=item_data)

#     if serializer.is_valid():
#         item = serializer.save()
#         generate_referral_code(item)

#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_items(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Handle PUT request (update item)
        item_data = request.data

    # Use .filter() to check for existing items with the same SKU
    existing_items = Item.objects.filter(SKU=item_data['SKU']).exclude(pk=pk)

    if existing_items.exists():
        return Response({"message": "Item with the same SKU already exists."})

    serializer = ItemSerializer(instance=item, data=item_data, partial=True)

    if serializer.is_valid():
        # Data is different, update the item
        item = serializer.save()
        generate_referral_code(item)

        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_items(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)