from django.conf.urls import url
from blog.views import * 

urlpatterns = [

        # Example: /
        url(r'^$', PostLV.as_view(), name='index'),

        # Example: /post/ (same as /)
        url(r'^post/$', PostLV.as_view(), name='post_list'),

        # Example: /post/djanggo-example/
        url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

        # Example: /archive/
        url(r'^archive/$', PostAV.as_view(), name='post_archive'),

        # Example: /2012/
        url(r'^(?P<year>\d{4})/$', PostAV.as_view(), name='post_year_archive'),

        # Example: /2012/nov/
        url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_day_archive'),

        # Example: /2012/nov/10/
        url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

        # Example /today/
        url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

	# Example /tags/
	url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

	# Example /tag/tagname/
	url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

	# Example /search/
	url(r'^search/$', SearchFormView.as_view(), name='search'),

        # 아래의 내용 추가
        # Example: /add/
        url(r'^add/$',
            PostCreateView.as_view(), name="add",
        ),

        # Example: /change/
        url(r'^change/$',
            PostChangeLV.as_view(), name="change",
        ),

        # Example: /99/update/
        url(r'^(?P<pk>[0-9]+)/update/$',
            PostUpdateView.as_view(), name="update",
        ),

        # Example: /99/delete/
        url(r'^(?P<pk>[0-9]+)/delete/$',
            PostDeleteView.as_view(), name="delete"
        ),

]
