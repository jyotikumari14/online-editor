from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from editor import views

router = DefaultRouter()
router.register(r'file', views.fileUploading, base_name='file_api')

urlpatterns = [
	path('api/v1/', include(router.urls)),
	path('read/', views.readFile, name='read'),
	path('fileedit/', views.fileedit, name='fileedit'),
	path('update/<int:pk>/', views.update, name='update'),
]