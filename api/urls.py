from django.urls import path
from . import views
from .views import BatGameViewSet, EventViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'api-games', BatGameViewSet, basename='api-games'),
router.register(r'api-events', EventViewSet, basename='api-events'),
urlpatterns = router.urls

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-list/', views.tasklist, name="api-list"),
    path('api-detail/<str:pk>/', views.taskDetail, name="api-detail"),
    path('', views.apiOverview, name="api-overview"),

]

