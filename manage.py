#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takecare.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')
>>>>>>> ef99cff9e7ad8f0fb4d1fe66578540b18f16eb55
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
