from django.urls import path, include
from expenses import views

urlpatterns = [
                  path('', include('django.contrib.auth.urls')),
                  path('expenses/my/', views.ExpenseListView.as_view(), name=views.ExpenseListView.name),
                  path('expenses/create/', views.ExpenseCreateView.as_view(), name=views.ExpenseCreateView.name),
                  path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name=views.ExpenseDetailView.name),
                  path('expenses/<int:pk>/edit', views.ExpenseUpdateView.as_view(), name=views.ExpenseUpdateView.name),
                  path('expenses/<int:pk>/delete', views.ExpenseDeleteView.as_view(), name=views.ExpenseDeleteView.name),
                  path('expenses/register/', views.RegisterView.as_view(), name='register'),
]
