#from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import License
from .serializers import *


@api_view(['GET', 'POST'])
def licenses_list(request):
    """
    List or create new customers
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        licenses = License.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(licenses, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = LicenseSerializer(data, context={'request':request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages':paginator.num_pages, 'nextlink': '/api/licenses/?page=' + str(nextPage), 'prevlink': 'api/licenses/?pages=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def licenses_detail(request, pk):
    """
    Retrieve, update or delete a customer by id/pk
    """
    try:
        license = License.objects.get(pk=pk)
    except License.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LicenseSerializer(license, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LicenseSerializer(license, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
            license.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)