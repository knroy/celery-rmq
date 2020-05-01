import os
import sys

from celery_rmq.app import CeleryAppProvider
from celery_rmq.exchange import register_exchange
from celery_rmq.queue import register_queue

# import django settings
from django.conf import settings

from consumers.testconsumer import BasicTestConsumer

# set default settings module to app settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app_provider = CeleryAppProvider(app_name='django_celery',
                                 object_config='django.conf:settings',
                                 installed_apps=settings.INSTALLED_APPS)

app = app_provider.get_app()


def register_exchanges():
    """ register exchanges """
    exchange_name = 'test_exchange'
    register_exchange(app_provider, exchange_name)


def register_queues():
    """ register queues """
    queue_name = 'test_queue'
    routing_key = 'test_routing'
    exchange_name = 'test_exchange'
    register_queue(app_provider, queue_name, routing_key, exchange_name)


def add_consumers():
    """ register consumers """
    app_provider.add_consumer(BasicTestConsumer)


# execution of following two functions
# "register_exchanges()" and "register_queues()"
# needs to be synced
# i.e one after another.
# because queues are depended on exchanges

register_exchanges()
register_queues()

add_consumers()

if 'worker' in sys.argv:
    print('starting app for celery app')
    app.start()
