from django.urls import include, path
from rest_framework import routers
from .views import UserProfileDetailView, UserProfileListCreateView
from .api import LeadViewSet, UserMetaDataSet, UserProfileSet, RoleSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/user', UserMetaDataSet, 'UsersDetails')
router.register('api/profile', UserProfileSet, 'Users')
router.register('api/role', RoleSet, 'Roles')



urlpatterns = router.urls
# [

    #gets all user profiles and create a new profile
#     path("all-profiles",views.UserProfileListCreateView.as_view(),name="all-profiles"),
#    # retrieves profile details of the currently logged in user
#     path("profile/<int:pk>",views.UserProfileDetailView.as_view(),name="profile"),
# ]