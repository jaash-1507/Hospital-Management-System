#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import collections
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models.signals import m2m_changed


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
