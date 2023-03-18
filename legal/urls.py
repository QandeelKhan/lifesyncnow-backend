from django.urls import path
from .views import (
    TermsAndConditionsList, TermsAndConditionsDetail,
    ClauseList, ClauseDetail,
    UserAgreementList, UserAgreementDetail,
)

app_name = 'terms_and_conditions'

urlpatterns = [
    path('terms/', TermsAndConditionsList.as_view(), name='terms_list'),
    path('terms/<int:pk>/', TermsAndConditionsDetail.as_view(), name='terms_detail'),
    path('clauses/', ClauseList.as_view(), name='clause_list'),
    path('clauses/<int:pk>/', ClauseDetail.as_view(), name='clause_detail'),
    path('agreements/', UserAgreementList.as_view(), name='user_agreement_list'),
    path('agreements/<int:pk>/', UserAgreementDetail.as_view(),
         name='user_agreement_detail'),
]
