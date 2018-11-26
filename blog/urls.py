from . import views
from django.urls import path
from .views import (PostListView, PostCreateView,
                    PostUpdateView, PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/adopt/', views.adopt, name='adopt'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
