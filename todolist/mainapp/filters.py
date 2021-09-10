from mainapp.models import ToDo
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet


class ToDoFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['text']
