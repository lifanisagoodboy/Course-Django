# _*_ coding:utf-8 _*_
__author__ = 'lifan'
__date__ = '2017/4/26 20:24'

from django.conf.urls import url,include
from .views import CourseListView,CourseDetailView,CourseListViewInterface
from .views import CourseInfoView,CommentView,AddCommentsView,VideoPlayView

urlpatterns = [
     #课程列表页
    url(r'^list/$',CourseListView.as_view(),name="course_list"),

    #课程列表接口
    url(r'^list_interface/$',CourseListViewInterface.as_view(),name="course_list_interface"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name="course_detail"),

    #章节详情页
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name="course_info"),

    #课程评论页
    url(r'^comment/(?P<course_id>\d+)/$', CommentView.as_view(), name="course_comment"),

    #添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

    #课程详情页
    url(r'^video/(?P<video_id>\d+)/$',VideoPlayView.as_view(),name="video_play"),

]