from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AnnounceCreateView,
    AnnounceListView,
    EngineersListView,
    EntrepreneurListView,
    AcademicianListView,
    ResearchersListView,
    DoctorsListView,
)
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    
    path('home', PostListView.as_view(), name='blog-home'),
    path('profiles/', views.profiles, name='blog-profiles'),
    path('', views.home1, name='blog-home1'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('EngineersList/',EngineersListView.as_view() , name='EngineersList'),
    path('announement/',AnnounceCreateView.as_view(), name='announement'),
    path('announementlist/',AnnounceListView.as_view(), name='announementlist'),
    path('DoctorsList/',DoctorsListView.as_view(),name='DoctorsList'),
    path('EntrepreneurList/',EntrepreneurListView.as_view(),name='EntrepreneurList'),
    path('ResearchersList/',ResearchersListView.as_view(),name='ResearchersList'),
    path('AcademicianList/',AcademicianListView.as_view(),name='AcademicianList'),


   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)