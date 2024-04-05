from django.contrib import admin
from django.urls import path
from amira import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofrighttcylinder/',views.surfacearea,name="surafceareaofrightcylinder"),
    path('',views.surfacearea,name="surafceareaofrightcylinderroot")
]