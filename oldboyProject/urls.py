"""oldboyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from bbs import views
from web_chat import urls as chat_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include(chat_urls)),
    url(r'^$', views.index,name='index'),
    url(r'^category/(\d+)/$',views.category,name="Category"),
    url(r'^article_detail/(\d+)/$',views.articl_detail,name="article_detail"),
    url(r'^new_article/$',views.new_article,name="new_article"),
    url(r'^logout/$',views.acc_logout,name="logout"),
    url(r'^login/$',views.acc_login,name="login"),
    url(r'^post_comment/$',views.post_comment,name="post_comment"),
    url(r'^test/$',views.test),
    url(r'^user_list/$',views.user_list),
    url(r'^get_comments/(\d+)/$',views.get_comments,name='get_comments'),
    # url(r'^get_latest_article_count',views.get_latest_article_count,name='get_latest_article_count'),



]
