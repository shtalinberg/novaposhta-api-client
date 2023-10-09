"""BaseModel module."""

from typing import Dict, Any


def api_method(method_name: str):
    """
    Decorator for methods to provide the api method name.
    :param method_name: name of the method from API.
    """

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            props = func(self, *args, **kwargs)
            return self._call(method_name, props)

        return wrapper

    return decorator


class BaseModel:
    """
    Base class for model.
    Uses NovaPoshta client to perform calls to the API and passes required
    model name.
    """

    name = "base"

    def __init__(self, client):
        self._client = client

    def _call(self, method: str, props: Dict[str, Any]):
        """
        Wraps call to the API by using client. Automatically passes model name.

        :param method: name of the called method from API.
        :param props: payload to send to API.
        :return: Response object.
        """
        return self._client.send(self.name, method, props)

    @staticmethod
    def _call_with_props(**properties: Any):
        """
        Filters out empty properties, convert to string and returns only those that have values.

        :param properties: properties to filter.
        """
        props = {
            k: str(v) if not isinstance(v, (list, dict)) else v
            for k, v in properties.items()
            if v is not None
        }
        return props

    def __str__(self):
        return self.name
