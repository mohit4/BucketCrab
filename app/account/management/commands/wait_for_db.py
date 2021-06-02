import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Wait For DB commands check if the database configured with the application is ready to accept
    connections or not
    """

    def handle(self, *args, **options):
        self.stdout.write( "Waiting for database..." )
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write( "Database unavailable, waiting for 1 sec..." )
                time.sleep(1)
        
        self.stdout.write( self.style.SUCCESS( "Database available!" ) )
