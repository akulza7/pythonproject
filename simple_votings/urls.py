
from django.contrib import admin
from django.urls import path

from main import views

from main.views import get_menu_context
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('time/', views.time_page, name='time'),
    path('login/',views.LoginUser.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/<int:id>', views.profile_page_id),
    path('votings/', views.votings_page, name='votings'),
    path('voting/<int:id>', views.voting_page, name='voting'),
    path('add_vote/<int:id>', views.add_vote, name='add_vote'),
    path('add_comment/<int:id>', views.add_comment, name='add_comment'),
    path('create_voting/', main_views.create_voting_page, name='create_voting'),
    path('edit_voting/<int:id>', views.edit_voting_page, name='edit_voting'),
    path('delete_voting/<int:id>', views.delete_voting, name='edit_voting'),
    path('edit_profile/', views.edit_profile_page, name='edit_profile'),
    path('new_password/', views.change_password, name='change_password'),
    path('new_bio/', views.change_bio, name='change_bio'),
    path('new_logo/', views.change_logoimage, name='change_logo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
