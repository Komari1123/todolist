from django.urls import path,include
from .views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate,signupfunc,loginfunc,logoutfunc,timer
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('list/',TodoList.as_view(),name = 'list'),
    path('detail/<int:pk>',TodoDetail.as_view(),name='detail'),
    path('create/',TodoCreate.as_view(),name='create'),
    path('delete/<int:pk>',TodoDelete.as_view(),name='delete'),
    path('update/<int:pk>',TodoUpdate.as_view(),name='update'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('timer/', timer, name='timer'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
