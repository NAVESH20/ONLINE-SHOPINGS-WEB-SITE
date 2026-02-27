from django.urls import path

from buyapp.views import addimage,image,all,search,update,deleted,need,register,logins,user_logout

urlpatterns = [
    path("addimage",addimage),
    path("image",image),
    path("all",all),#(button)
    path("search",search),
    path("update",update),
    path("deleted",deleted),
    path("need",need),
    path("register",register),
    path("login",logins),
    path("logout",user_logout),
]