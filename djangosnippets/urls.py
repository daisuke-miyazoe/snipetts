from django.contrib import admin
from django.urls import path, include

from snippets.views import top, snippet_new, snippet_edit, snippet_detail

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
