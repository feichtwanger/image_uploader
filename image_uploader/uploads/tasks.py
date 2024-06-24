# uploads/tasks.py
from celery import shared_task
from PIL import Image as PilImage
from .models import Image
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_image(image_id):
    image = Image.objects.get(id=image_id)
    with PilImage.open(image.original.path) as img:
        # Создание миниатюры
        thumb = img.copy()
        thumb.thumbnail((150, 120))
        thumb.save(image.thumb.path)

        # Создание большой миниатюры
        big_thumb = img.copy()
        big_thumb.thumbnail((700, 700))
        big_thumb.save(image.big_thumb.path)

        # Создание изображения 1920x1080
        big_1920 = img.copy()
        big_1920.thumbnail((1920, 1080))
        big_1920.save(image.big_1920.path)

        # Создание изображения 2500x2500
        d2500 = img.copy()
        d2500.thumbnail((2500, 2500))
        d2500.save(image.d2500.path)

    image.processed = True
    image.save()

    # Уведомление через WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'image_{image_id}',
        {
            'type': 'image.processed',
            'image_id': image_id,
        }
    )
