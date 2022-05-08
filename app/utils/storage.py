from redis import Redis


class Storage:
    def __init__(self):
        self.client = Redis(host="redis_server", port=6379)

    def set_key(self, key, value):
        self.client.set(key, value)

    def get_key(self, key):
        return self.client.get(key)
