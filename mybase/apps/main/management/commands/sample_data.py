# -*- coding: utf8 -*-

from django.core.management.base import BaseCommand, CommandError
from main.models import *
from faker import Faker
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "make clients..."
        self.make_clients()
        print "done"

    def make_clients(self):
        Client.objects.all().delete()
        f = Faker()

        for i in range(100):
            try:
                name = f.company()
                client = Client()
                client.name = name
                client.descr = "%s\n%s\n%s" % (name, f.email(), f.phonenumber())
                client.status = random.randint(0,2)
                client.save()
            except Exception, e:
                print "%s - error: %s" % (client.name, e)
