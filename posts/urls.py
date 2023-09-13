from django.urls import path
from .views import postlist,postcreate,postupdate,postdelete,postdetail,commentcreate,commentupdate,commentdelete


urlpatterns = [
    path('', postlist,name="postlist"),
    path('create/',postcreate,name="postcreate"),
    path('<int:post_id>/',postdetail,name="postdetail"),
    path('<int:post_id>/update/',postupdate,name="postupdate"),
    path('<int:post_id>/delete/',postdelete,name="postdelete"),
    path('<int:post_id>/cmt/create/',commentcreate,name="commentcreate"),
    path('<int:post_id>/cmt/<int:cmt_id>/update/',commentupdate,name="commentupdate"),
    path('<int:post_id>/cmt/<int:cmt_id>/delete/',commentdelete,name="commentdelete")
]