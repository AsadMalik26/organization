from django.contrib import admin
from django.urls import path, include

from department.views import DepartmentListAPIView, DepartmentCreateAPIView, DepartmentListArnonAPIView, \
    DepartmentCreateWithModelView, DepartmentCreateWithSerializerView, DepartmentGetAPIView, DepartmentUpdateAPIView, \
    DepartmentDeleteAPIView

urlpatterns = [
    path('get/', DepartmentGetAPIView.as_view(), name='single-department'),
    path('list/', DepartmentListAPIView.as_view(), name='department-list'),
    path('arnon/', DepartmentListArnonAPIView.as_view(), name='department-list2'),

    path('add/', DepartmentCreateAPIView.as_view(), name='department-add'),
    path('add-model-method/', DepartmentCreateWithModelView.as_view(), name='department-add-model-method'),
    path('add-serializer-method/', DepartmentCreateWithSerializerView.as_view(), name='department-add-serializer-method'),

    path('update/', DepartmentUpdateAPIView.as_view(), name='department-update'),
    path('delete/', DepartmentDeleteAPIView.as_view(), name='department-delete'),
]
