from django.conf.urls import url
from apps.comment.views import view_comment,new_comment

urlpatterns = [
    url(r'^newcomment$',new_comment),
    url(r'^$',view_comment, name= "create_comment"),
]
