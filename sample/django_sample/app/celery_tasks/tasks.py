from __future__ import absolute_import, unicode_literals

from celery import shared_task

from app.celery import app_provider


@shared_task
def publish_message(message, exchange_name, route_key, content_type='application/text'):
    producer = app_provider.get_producer()
    producer.publish(message, content_type=content_type, exchange=exchange_name, routing_key=route_key)
