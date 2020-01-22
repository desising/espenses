from django import forms
from .models import Expense
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, InlineCheckboxes

class ExpenseListFormHelper(FormHelper):
    """
       This Class renders the filter form used for filtering the expenses
    """    

    model = Expense
    form_id = 'expense-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap4/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Filter Expense Records',       
                    InlineField('name'),
                    InlineField('name__cont'),
                    InlineField('amount'),
                    InlineField('amount__gt'),
                    InlineField('amount__lt'),
                    InlineField('created'),
                    InlineField('created__gt'),
                    InlineField('created__lt'),
                    InlineField('image__exists'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Filter', 
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )


class ExpenseCreateForm(forms.ModelForm):
    "This class renders the form which is used to create an expense"
    class Meta:
        model = Expense
        exclude = ('user', 'created')
