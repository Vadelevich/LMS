from rest_framework import permissions
from rest_framework.permissions import BasePermission


#Todo: Переделать на один permission(self.request.user.has_perms(perm_list=['change_course','view_course','change_lesson','view_lesson'])

class ManagerOrOwnerPermissionsAll(BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().user_create:
            return True
        elif request.user.is_staff:
            return True
        return False

class ManagerPermissionCreateDestroy(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return False
        return True


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        if request.user == view.get_object().user_create:
            return True
