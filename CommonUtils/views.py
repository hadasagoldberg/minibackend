from django.conf import settings
import redis

redis_instance = redis.StrictRedis(host=settings.REDIS_VM_HOST,
                                   port=settings.REDIS_LOCAL_PORT)
# Create your views here.
