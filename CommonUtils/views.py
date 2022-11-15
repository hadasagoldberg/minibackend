from django.conf import settings
import redis

#redis_instance = redis.from_url('redis://34.132.95.210:6379/0')

redis_instance = redis.StrictRedis(host=settings.REDIS_VM_HOST,
                                 port=settings.REDIS_LOCAL_PORT,
                                db=0, password=settings.REDIS_PASSWORD)
# Create your views here.
