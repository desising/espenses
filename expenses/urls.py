from django.urls import path
from expenses import views

urlpatterns = [
                  path('my/', views.ExpenseListView.as_view(), name=views.ExpenseListView.name),
                  path('create/', views.ExpenseCreateView.as_view(), name=views.ExpenseCreateView.name),
                  path('<int:pk>/', views.ExpenseDetailView.as_view(), name=views.ExpenseDetailView.name),
                  path('<int:pk>/edit', views.ExpenseUpdateView.as_view(), name=views.ExpenseUpdateView.name),
                  path('<int:pk>/delete', views.ExpenseDeleteView.as_view(), name=views.ExpenseDeleteView.name),
                  path('register/', views.RegisterView.as_view(), name='register'),
]
