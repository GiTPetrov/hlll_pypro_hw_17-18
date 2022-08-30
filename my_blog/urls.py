from my_blog import views

from django.urls import path
from django.views.decorators.cache import cache_page

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # path('author-list/<str:slug>/', views.AuthorInfo.as_view(), name='author-detail'),
    # path('author-list/', views.AuthorsList.as_view(), name='author-list'),
    # path('book-list/<str:slug>/', views.BookInfo.as_view(), name='book-detail'),
    # path('book-list/', cache_page(10 * 60)(views.BooksList.as_view()), name='book-list'),
    # path('book-create/', views.BookFormCreateView.as_view(), name='book-create'),
    # path('book-view/<str:slug>/', views.BookFormView.as_view(), name='book-view'),
    # path('book-update/<str:slug>/', views.BookFormUpdateView.as_view(), name='book-update'),
    # path('book-delete/<str:slug>/', views.BookFormDeleteView.as_view(), name='book-delete'),
    # path('publisher-list/<str:slug>/', views.PublisherInfo.as_view(), name='publisher-detail'),
    # path('publisher-list/', views.PublishersList.as_view(), name='publisher-list'),
    # path('store-list/<str:slug>/', views.StoreInfo.as_view(), name='store-detail'),
    # path('store-list/', views.StoresList.as_view(), name='store-list'),
]
