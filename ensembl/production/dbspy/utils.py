from urllib.parse import urlsplit, urlunsplit, urlencode

from fastapi import Request


def url_for(
    request: Request, view: str, path_params: dict = None, query_params: dict = None
) -> str:
    if path_params is None:
        path_params = {}
    url = request.url_for(view, **path_params)

    if query_params is not None:
        query_params = {k: v for k, v in query_params.items() if v is not None}
        parsed_url = list(urlsplit(url))
        parsed_url[3] = urlencode(query_params)
        url = urlunsplit(parsed_url)
    return url
