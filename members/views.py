# members/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def member_list(request):
    """
    /api/members
    """
    # get all members
    if request.method == 'GET':
        # get list of all members
        members = Member.objects.all()
        # serialize, return list as valid http response
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    # create member
    elif request.method == 'POST':
        # serialise member data from request
        serializer = MemberSerializer(data=request.data)
        # if valid, save and return as 201 created http response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # error, return http 400 with errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, pk):
    """
    /api/members/<id>
    """
    # find and assign member with given ID or return 404 error
    member = get_object_or_404(Member, pk=pk)

    # get member
    if request.method == 'GET':
        # serialize found member object and return as valid http response
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    # update
    elif request.method == 'PUT':
        # create serializer with data from request mapped onto existing member object
        serializer = MemberSerializer(member, data=request.data)
        # if valid save to DB, return saved data as body in valid http response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # wasn't valid, return http 400 error response with errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete member
    elif request.method == 'DELETE':
        # delete given member, return as valid http response with no content
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
