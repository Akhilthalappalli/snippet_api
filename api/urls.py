from django.urls import path , include
from api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list',User.as_view(),name="user_list"),
    path('snippets/',Snippets.as_view({'get': 'list'}),name="snippets_list"),
    path('snippets/<int:pk>/',Snippets.as_view({'get': 'retrieve'}),name="snippet-detail"),
    path('tag/<int:pk>/',Tag.as_view({'get': 'retrieve'}),name="tag-detail"),
    path('<int:pk>',SnippetsDetail.as_view(),name="snippets_detail"),
]
