from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('post-details/<int:post_id>', views.details, name='post_details'),
	path('delete-post', views.delete_post, name='delete_post'),
	path('update-post', views.update_post, name='update_post'),
	path('new-post', views.new_post, name='new_post'),
	path('user-posts', views.user_posts, name='user_posts'),
]
