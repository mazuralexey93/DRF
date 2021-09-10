from mainapp.models import ToDo, Project
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet


class ToDoFilter(FilterSet):
    project = filters.CharFilter(field_name='project__name', lookup_expr='contains')
    min_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    max_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = ToDo
        fields = ['project', 'created_at']


class ProjectFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']
