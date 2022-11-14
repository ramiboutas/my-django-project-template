from django.urls import path

from core.views import ExampleView

app_name = "core"

urlpatterns = [
    path(
        "this-is-just-a-example-url-for-testing",
        ExampleView.as_view(),
        name="example-detail",
    )
]
