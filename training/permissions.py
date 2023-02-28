# from rest_framework.permissions import BasePermission
#
#
#
# class ModeratorPermissionCourse(BasePermission):
#     """ пользователи, которые не входят в группу модераторов, могут видеть и редактировать только свои курсы """
#
#     def has_permission(self, request, view):
#
#         # Проверяем является ли курс созданным пользователем
#         if request.user == view.get_object().user_create:
#             return True
#         # Если пользователь из персонала
#         if request.user.is_staff:
#             # Если пользователь модератор
#             if request.method.upper() in ['DELETE', 'POST']:
#                 return request.user.has_perms([
#                     'training.add_course',
#                     'training.delete_course',
#                 ])
#             else:
#                 return True
#         return False
#
#
# class ModeratorPermissionLesson(BasePermission):
#     """ пользователи, которые не входят в группу модераторов, могут видеть и редактировать только свои уроки """
#
#     def has_permission(self, request, view):
#
#         # Проверяем является ли курс созданным пользователем
#         if request.user == view.get_object().user_create:
#             return True
#         # Если пользователь из персонала
#         if request.user.is_staff:
#             # Если пользователь модератор
#             if request.method.upper() in ['DELETE', 'POST']:
#                 return request.user.has_perms([
#                     'training.add_lesson',
#                     'training.delete_lesson',
#                 ])
#             else:
#                 return True
#         return False
#
#
# class ModeratorPermissionLessonCreate(BasePermission):
#     """Для группы модераторов отключим возможность добавлять и удалять уроки"""
#
#     def has_permission(self, request, view):
#         if request.method.upper() in ['DELETE', 'POST']:
#             return request.user.has_perms([
#                 'training.add_lesson',
#                 'training.delete_lesson',
#             ])
#         return True
#
#
# class ModeratorPermissionCourseCreate(BasePermission):
#     """Для группы модераторов отключим возможность добавлять и удалять курсы"""
#
#     def has_permission(self, request, view):
#         if request.method.upper() in ['DELETE', 'POST']:
#             return request.user.has_perms([
#                 'training.add_course',
#                 'training.delete_course',
#             ])
#         return True


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

