from django.urls import path
from . import views


urlpatterns = [
        path('register/', views.registerPage, name="register"),
        path('login/', views.loginPage, name="login"),
        path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk_one>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk_one>', views.deleteOrder, name="delete_order"),

]
