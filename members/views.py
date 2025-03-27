# members/views.py

from rest_framework import viewsets, status  # Base class and HTTP status codes
from rest_framework.response import Response  # Standard DRF response class
from rest_framework.decorators import action  # Decorator for custom routes
from rest_framework.request import Request  # Type hint for DRF requests
from rest_framework.exceptions import ValidationError  # For invalid input
from django.http import Http404  # Exception for missing records
from .service import MemberService  # Business logic layer


class MemberViewSet(viewsets.ViewSet):
    """
    ViewSet for managing Member API endpoints.
    All business logic is delegated to the MemberService class.
    """

    def __init__(self, **kwargs):
        """
        Initialize the ViewSet and inject the service dependency.
        """
        super().__init__(**kwargs)
        self.service: MemberService = MemberService()  # Instantiate service layer

    def list(self, request: Request) -> Response:
        """
        GET /members/ — Return a list of all members.
        """
        members: list[dict] = self.service.list_members()  # Call service to fetch data
        return Response(members)  # Return data in response

    def create(self, request: Request) -> Response:
        """
        POST /members/ — Create a new member.
        """
        try:
            new_member: dict = self.service.create_member(request.data)  # Delegate creation
            return Response(new_member, status=status.HTTP_201_CREATED)  # Return 201 + new data
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)  # Return 400 if invalid

    def retrieve(self, request: Request, pk: str) -> Response:
        """
        GET /members/{pk}/ — Retrieve a specific member.
        """
        try:
            member: dict = self.service.get_member(int(pk))  # Fetch member by ID
            return Response(member)  # Return serialized member
        except Http404:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if missing

    def update(self, request: Request, pk: str) -> Response:
        """
        PUT /members/{pk}/ — Update an existing member.
        """
        try:
            updated: dict = self.service.update_member(int(pk), request.data)  # Update via service
            return Response(updated)  # Return updated data
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)  # Validation failed
        except Http404:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)  # Member not found

    def destroy(self, request: Request, pk: str) -> Response:
        """
        DELETE /members/{pk}/ — Delete a member.
        """
        try:
            self.service.delete_member(int(pk))  # Delete using service
            return Response(status=status.HTTP_204_NO_CONTENT)  # Success, no content
        except Http404:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)  # Member not found

    @action(detail=True, methods=['post'])
    def activate(self, request: Request, pk: str) -> Response:
        """
        POST /members/{pk}/activate/ — Custom action to activate a member.
        """
        try:
            self.service.activate_member(int(pk))  # Call custom business logic
            return Response({'status': 'member activated'})  # Return success message
        except Http404:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)  # Member not found
