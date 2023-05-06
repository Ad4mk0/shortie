import sys
from app.logging.logger import log
from typing import List, Dict, Optional
import redis
from app.configuration import get_settings, check_rights
from app.exceptions.access_exception import NoAccess
from functools import lru_cache


SETTINGS = get_settings()


class RedisHandler:
    """Class for handling connection and operations for Redis
    """
    def __init__(self) -> None:
        self.client = self.connect()


    def connect(self) -> redis.client.Redis:
        """ Function will initialize redis client

        Returns:
            redis.client.Redis: initialized Redis client, or exits in sys.exit(1)
        """
        try:
            client = redis.Redis(host=SETTINGS.redis_host, port=SETTINGS.redis_port)
            ping = client.ping()
            if ping is True:
                return client
        except redis.ConnectionError:
            log.error("Redis connection Error!")
            sys.exit(1)
        

    def get(self, key: str) -> str | None:
        """ Function for retrieving data for given key

        Args:
            key (str): key to be looked for

        Returns:
            str: returns str value if found, else None
        """
        val = self.client.get(key)
        return val


    def put_nt(self, key: str, value: str) -> bool:
        """ Function will put value with corresponding key to hashtable

        Args:
            key (str)
            value (str)

        Returns:
            bool: returns True when succeeds
        """
        val = self.client.set(key, value)
        return val
    

    def put(self, key: str, value: str, time: int) -> bool:
        """ Function will put to Redis db

        Args:
            key (str): hash for url
            value (str): url
            time (int): time in minutes after which the hash will expire

        Returns:
            bool: returns True when succeeds
        """
        val = self.client.set(key, value, ex=time*60)
        return val

    
    def all_keys(self, token: str = "mamprava", pattern: str | None = "*") -> List[str]:
        """Function retrieves all existing keys in Redis db.
           Time complexity is O(N).

        Args:
            token (str): access token
            pattern (str, optional): glob-style pattern see here:
            https://redis.io/commands/keys/
            Defaults to "*".

        Returns:
            List[str]: _description_
        """
        val = self.client.keys(pattern)
        return val
    

    def all(self, token: str = "mamprava", pattern: str | None = "*", ) -> List[Dict[str, str]]:
        """Function retrieves all existing keys and values in Redis db.
           Time complexity is O(N).

        Args:
            token (str): access token
            pattern (str, optional): glob-style pattern see here:
            https://redis.io/commands/keys/
            Defaults to "*".

        Returns:
            List[Dict[str, str]]: List of dicts with shorted url's
        """
        if check_rights(token):
            keys = self.all_keys(token, pattern)
            all = [{"hash": key,
                    "link": self.get(key)} for key in keys ]
            return all
        raise NoAccess


    def put_slug(self, key: str, slug: str, value: str) -> str | None:
        """ Function for saveing data for given key and slug

        Args:
            key (str): key to be looked for
            value (str): key to be looked for
            slug (str): slug to be looked for

        Returns:
            str: returns str value if found, else None
        """
        return self.redis_put_nt(key+"%"+slug, value)


    def get_slug(self, key: str, slug: str) -> str | None:
        """ Function for retrieving data for given key and slug

        Args:
            key (str): key to be looked for
            slug (str): slug to be looked for

        Returns:
            str: returns str value if found, else None
        """
        val = self.client.get(key+"%"+slug)
        return val


    def remove(self, keys: List[str] | str, token: str):
        """ Removes keys from db

        Args:
            keys (List[str] | str): keys to be deleted from db
            token (str): access token

        Raises:
            NoAccess: when user does not have access for operation
        """
        if check_rights(token):
            self.client.delete(keys)
        else: 
            raise NoAccess


    def modify(self, key: str, value: str, token: str) -> Optional[bool]:
        """ Modify the existing record in db

        Args:
            key (str): key under which the data is stored
            value (str): new value
            token (str): access token

        Returns:
            Optional[bool]: returns True when succeeds
        """
        self.redis_remove(key, token)
        return self.redis_put_nt(key, value)



@lru_cache()
def get_redis_handler():
    return RedisHandler()
