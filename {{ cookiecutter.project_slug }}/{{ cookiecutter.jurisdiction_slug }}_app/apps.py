from django.apps import AppConfig


class {{ cookiecutter.jurisdiction_camel_case }}CouncilmaticConfig(AppConfig):
    name = "{{ cookiecutter.jurisdiction_slug }}_app"
    verbose_name = "{{ cookiecutter.project_name }}"
