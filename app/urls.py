from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project"),
    path("create", views.ProjectCreate.as_view(), name="create-project"),
    path("<int:pk>/update", views.ProjectUpdate.as_view(), name="update-project"),
    path("<int:pk>/delete", views.project_delete, name="delete-project"),
    path("tasks/", views.render_all_task, name="tasks"),
    path("stage/tasks/<int:stage_id>", views.render_task_by_stage, name="task-stage"),
    path("task/create", views.create_task, name="create_task"),
    path('signup/', views.signUp, name='signup'),
    path('verify/<uidb64>/<str:token>/', views.verify, name='verify'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/signin.html'), name='login'),
]
