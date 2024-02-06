from django.urls import path
# internals
from api.views import  CodeExplainView
# from api.views import UserView, TokenView,
urlpatterns = [
    # path('users/', UserView.as_view(), name='users'),
    # path('tokens/', TokenView.as_view(), name='tokens'),
    path('code-explain/', CodeExplainView.as_view(), name='code-explain' )
]