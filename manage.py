#!/usr/bin/env python
import os
import sys

from decouple import config

if __name__ == "__main__":
    env = config('NEPTUNE_ENV', default='local')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"neptune.settings.{env}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv.__len__() == 1:
        sys.argv.append('runserver')
    execute_from_command_line(sys.argv)
