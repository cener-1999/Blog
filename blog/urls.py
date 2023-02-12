from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.post, name='post'),
    path('classify/<str:type>', views.classify, name='classify'),
    path('tag/<str:tag>', views.tags, name='tag'),
    path('author/<str:name>', views.author, name='author'),
    path('archives/<int:year>/<int:month>', views.archive, name='archives'),
    path('make_comment/<int:post_pk>',views.make_comment,name='make_comment')
]
