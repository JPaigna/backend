from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('fetch/', TodoListView.as_view(), name='todo-list'),         # GET list of todos
    path('create/', TodoCreateView.as_view(), name='todo-create'),    # POST new todo
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),  # PUT/PATCH todo
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),  # DELETE todo

    # JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access & refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]
