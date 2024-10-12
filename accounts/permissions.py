from rest_framework.permissions import BasePermission
from .models import *


class IsLibrarian(BasePermission):

    def has_permission(self, request, view):

        return request.user.role == "librarian" and request.user.is_authenticated
