from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    UserProjectViewSet,
    DomainViewSet,
    DefectViewSet,
    CommentViewSet,
    AttachmentViewSet,
)

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"user-projects", UserProjectViewSet)
router.register(r"domains", DomainViewSet)
router.register(r"defects", DefectViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"attachments", AttachmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

