#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3

def main():
    """Run administrative tasks."""
    if "data.db" not in os.listdir():
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE user_response (
        username TEXT,
        name TEXT,
        usn TEXT,
        email TEXT,
        sem INTEGER CHECK (sem<=8),
        branch TEXT,
        rating INTEGER,
        subject TEXT,
        p_language TEXT,
        token TEXT PRIMARY KEY
        )
        ''') #make username primary key to restrict one response per user
        con.commit()
        con.close()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testing.settings')
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
