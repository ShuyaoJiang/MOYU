from django.urls import path

from . import views

app_name = "moyuweb"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('login_auth', views.login_auth, name="login_auth"),
    path('logout/', views.logout, name="logout"),
    path('issue/', views.issue, name="issue"),
    path('me/sale/', views.me_sale, name="me_sale"),
    path('me/transaction/', views.me_transaction, name="me_transaction"),
    path('me/favorites/', views.me_favorites, name="me_favorites"),
    path('myInfo/base/', views.myInfo_base, name="myInfo_base"),
    path('myInfo/contact/', views.myInfo_contact, name="myInfo_contact"),
    path('myInfo/changePwd/', views.myInfo_changePwd, name="myInfo_changePwd"),
]
