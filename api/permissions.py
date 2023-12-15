from rest_framework import permissions

from app.utils.helpers import is_pm, is_in_project, is_pm_or_stage_owner


class IsPM(permissions.BasePermission):
    def has_permission(self, request, view):
        project = view.kwargs.get("project_id")
        return is_pm(request.user, project)


class IsPMOrProjectMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            project = view.kwargs.get("project_id")
            return is_in_project(request.user, project)
        else:
            project = view.kwargs.get("project_id")
            return is_pm(request.user, project)


class IsPMOrStageOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        project = view.kwargs.get("project_id")
        stage = view.kwargs.get("stage_id")

        return is_pm_or_stage_owner(request.user, stage, project)
