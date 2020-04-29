# celery-rmq

celery-rmq is a python library to implement Celery and RabbitMQ message broker. 
it's a standalone library required celery and kombu (python library for rabbitmq).
Celery and RabbitMQ producer and consumer made easy with celery-rmq


## Quick Start

First of all, install rabbitmq and start.

Create a python app and create an virtual environment too. Activate the virtual environment.

1:: Install it:

```bash
pip install celery-rmq
```


2:: Basic Usage:

** app.py **

```python
from celery_rmq.app import CeleryAppProvider
from celery_rmq.exchange import register_exchange
from celery_rmq.queue import register_queue

from .consumers.testconsumer import BasicTestConsumer

apps = ['tests.testapp']

app_provider = CeleryAppProvider(app_name='test_celery_broker', installed_apps=apps)

app = app_provider.get_app()


# adding exchanges

def register_exchanges():
    register_exchange(app_provider, "test_exchange")


def register_queues():
    register_queue(app_provider, "test_queue", "test_routing", "test_exchange")


def add_consumers():
    app_provider.add_consumer(BasicTestConsumer)


# execution of following two functions
# "register_exchanges()" and "register_queues()"
# needs to be synced
# i.e one after another.
# because queues are depended on exchanges

register_exchanges()
register_queues()

add_consumers()

app.start()
```

register as many as exchanges, queues and consumers

3:: consumer.py

```python
import kombu
from celery import bootsteps

from celery_rmq.registry import get_queue


class BasicTestConsumer(bootsteps.ConsumerStep):

    def handle_message(self, body, message):
        print(body)
        message.ack()

    def get_consumers(self, channel):
        queue = get_queue("test_queue", "test_routing")
        return [kombu.Consumer(
            channel,
            queues=[queue],
            callbacks=[self.handle_message],
            accept=['json']
        )]
```

4:: If you want to add this with any framework,
create an app (example: **Django** apps) and create a tasks.py file under the app:

```python
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from tests.app import app_provider


@shared_task
def simple_json_message(message, exchange_name, route_key):
    producer = app_provider.get_producer()
    producer.publish(message, content_type='application/json', exchange=exchange_name, routing_key=route_key)
```

&nbsp;&nbsp;&nbsp;and call the `simple_json_message` function from the view as per your need.

5:: Run the celery worker:

```bash
celery worker -l info -A app
```

here app is app.py file

###### Done.

for testing purpose, we would like to send messages directly from RabbitMQ web panel. Go the the queue section and publish message.

<p align="center">
    <img src="https://github.com/knroy/celery-rmq/blob/master/screenshots/publish_message_from_rabbitmq.png?raw=True">
</p>

<p align="center">
    <img src="https://github.com/knroy/celery-rmq/blob/master/screenshots/terminal.png?raw=True">
</p>

