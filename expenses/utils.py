from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig

class FilteredTableView(SingleTableView):
    """
      This class is used as a helper class to incorporate 
      the filtered objects into a single template
    """
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(FilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context
