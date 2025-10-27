#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

def main():
    """Run administrative tasks."""
    # 🎯 CONFIGURAR VARIÁVEL DE AMBIENTE DO DJANGO
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livraria.settings')
    
    try:
        # 📦 IMPORTAR E EXECUTAR COMANDOS DO DJANGO
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # 🎪 EXECUTAR COMANDO (ex: runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()