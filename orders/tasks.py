from celery import shared_task
from .models import Order
import time


@shared_task
def prepare_order(order_id):
    order = Order.objects.get(id=order_id)
    time.sleep(order.total_cooking_time * 60)
