from django.urls import path
from core.views import login_view, orm_dashboard, strategy_dashboard, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('orms-dashboard/', orm_dashboard, name='orms_dashboard'),
    path('strategy/', strategy_dashboard, name='strategy_dashboard'),
]