from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from import_ad.models import SilvaUser
from import_ad.serializers import SilvaUserSerializer


class ActiveDirectoryView(APIView):
    """
    View to import users from Active Directory.
    """

    # Only admins can import users from Active Directory
    # permission_classes = [IsAdminUser]

    @staticmethod
    def get(request, format=None):
        """
        Handle the HTTP GET request.
        """

        # Import the service
        from import_ad import services

        # Import the users
        results = services.import_ldap_users()

        # Return the results
        return Response(results)


class SearchUserView(APIView):
    """
    View to search users.
    """

    QUERY_PARAM = 'q'

    def __init__(self):
        """
        Constructor.
        """

        # Call the parent constructor.
        super().__init__()
        # Set the serializer class.
        self.serializer_class = SilvaUserSerializer

    def get(self, request):
        """
        Handles GET requests.
        :param request: the request.
        """

        if 'q' not in request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        q = request.GET.get(self.QUERY_PARAM)

        # Search on the documents
        users = list(SilvaUser.objects.filter(
            Q(last_name__icontains=q) | Q(first_name__icontains=q) | Q(email__icontains=q)).all())
        # Serialize the found documents
        serialized_users = self.serializer_class(users, many=True).data

        return Response(serialized_users)
