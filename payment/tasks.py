from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'My Shop - EE Invoice no. {order_id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'vitor.campos@engenharia.ufjf.br', [order.email])
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()
