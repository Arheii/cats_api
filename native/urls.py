from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),

    # API Routes
    path("breeds", views.breeds, name="breeds"),
    path("cats", views.cats, name="cats"),
    path("cats/<int:cat_id>", views.cat, name="cat"),
    path("cats/new", views.new, name="new"),
    # path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
