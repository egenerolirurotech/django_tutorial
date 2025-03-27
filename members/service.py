# members/services.py

from typing import Any
from .models import Member
from .serializers import MemberSerializer
from django.shortcuts import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework.exceptions import ValidationError


class MemberService:
    """
    A class to encapsulate all business logic related to Member objects.
    """

    def list_members(self) -> ReturnList:
        """
        Retrieve all members from the database and serialize them.
        """
        members: list[Member] = Member.objects.all()  # Query all members from the DB
        serializer: MemberSerializer = MemberSerializer(members, many=True)  # Serialize list of members
        return serializer.data  # Return serialized data

    def create_member(self, data: Any) -> ReturnDict:
        """ raises HTTP404
        Create and return a new member from input data.
        """
        serializer: MemberSerializer = MemberSerializer(data=data)  # Initialize serializer with input data
        if not serializer.is_valid():  # Validate data
            raise ValidationError(serializer.errors)  # Raise error if data is invalid
        serializer.save()  # Save the new member instance to the DB
        return serializer.data  # Return the created member's data

    def get_member(self, pk: int) -> ReturnDict:
        """ raises HTTP404
        Retrieve a single member by ID and serialize it.
        """
        member: Member = get_object_or_404(Member, pk=pk)  # Fetch the member or raise 404
        serializer: MemberSerializer = MemberSerializer(member)  # Serialize the member
        return serializer.data  # Return the serialized data

    def update_member(self, pk: int, data: Any) -> ReturnDict:
        """ raises HTTP404, ValidationError
        Update an existing member with new data.
        """
        member: Member = get_object_or_404(Member, pk=pk)  # Get the existing member object
        serializer: MemberSerializer = MemberSerializer(member, data=data)  # Re-initialize serializer with new data
        if not serializer.is_valid():  # Validate new data
            raise ValidationError(serializer.errors)  # Raise error if invalid
        serializer.save()  # Save updates to the database
        return serializer.data  # Return updated data

    def delete_member(self, pk: int) -> None:
        """ raises HTTP404
        Delete a member by ID.
        """
        member: Member = get_object_or_404(Member, pk=pk)  # Retrieve the member or raise 404
        member.delete()  # Delete the member from the database

    def activate_member(self, pk: int) -> None:
        """ raises HTTP404
        Activate a member by setting `is_active` to True.
        """
        member: Member = get_object_or_404(Member, pk=pk)  # Fetch the member
        member.is_active = True  # Set the flag
        member.save()  # Save changes to the database
