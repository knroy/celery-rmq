import json

from django.http import HttpResponse
from django.views.generic import View

from .tasks import publish_message


class CeleryTestView(View):

    def get(self, request):
        template = '''
        <div>
        <p>this is a test celery view</p>
        </div>
        '''

        task_message = {
            'type': 'send_mail',
            'data': {
                'body': 'this is a test mail',
                'header': 'Test mail',
                'from': 'info@example.com',
                'to': 'user@example.com'
            }
        }

        publish_message(json.dumps(task_message), 'test_exchange', 'test_routing', content_type='application/json')
        return HttpResponse(content=template)
