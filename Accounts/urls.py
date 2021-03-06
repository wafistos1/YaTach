
from django.urls import path, include
from Accounts.views import signup_user, artisant_user, PortfoliosUpdate, UserUpdateView, profil, ArtisantUpdate, AddArtisantImages, artisant_job#Note that we are using UpdateView and not FormView


urlpatterns = [
    path('accounts/signup/user/', signup_user, name='signup_user'),
    path('accounts/signup/artisant_user/', artisant_user, name='artisant_user'),
    path('accounts/profil', profil, name='profil'), 
    path('accounts/user_update', UserUpdateView, name='user_update'), 
    path('accounts/profile_update', PortfoliosUpdate, name='profile_update'), 
    path('accounts/artisant_update', ArtisantUpdate, name='artisant_update'), 
    path('accounts/artisant_image_update', AddArtisantImages, name='artisant_image_update'), 
    path('accounts/artisant_job', artisant_job, name='artisant_job'), 
]