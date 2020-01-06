
from django.conf.urls import url
from django.contrib import admin

from Feedback_app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.feedbackview),
]
