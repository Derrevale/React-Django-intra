from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


class ActiveDirectoryView(APIView):
    """
    View to import users from Active Directory.
    """

    # Only admins can import users from Active Directory
    permission_classes = [IsAdminUser]

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
