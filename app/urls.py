from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .froms import LoginForm
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
   
     path('accounts/login/',auth_views.LoginView.as_view(template_name='app/Login.html', authentication_form=LoginForm,next_page='home'), name='login'),
    path("registretion/", views.Registreton.as_view(), name="registretion"),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),





    path("create/", views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),



    path("category/", views.CategoryView.as_view(), name="category"),
    path("subcategory/", views.subcategory, name="subcategory"),


    # get subcategory data by  category
    path("fatch-subcatgeory/<int:id>", views.fatchsubcatgeory, name="fatch-subcatgeory")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
