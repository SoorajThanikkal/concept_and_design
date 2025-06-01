from django.urls import path


from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path('send-message/', views.send_message, name='send_message'),
    path('media/<path:path>', views.serve_media, name='serve_media'),
]
handler404 = 'concept_app.views.custom_404'
