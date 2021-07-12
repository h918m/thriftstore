from django.urls import include, path
from knox.views import LogoutView
from vendor.views import VendorDetailView

from . import views

app_name = "account"

urlpatterns = [
    path("", include("knox.urls")),
    path("account", VendorDetailView.as_view(), name="vendor_user"),
    path("account/register", views.AccountDetail.as_view(), "account_auth"),
    path("account/login", views.AuthDetail.as_view(), "account_login"),
    path("account/logout", LogoutView.as_view(), name="knox_logout"),
]
