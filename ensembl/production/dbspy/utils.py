# See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Utility functions for the main module.
"""

from urllib.parse import urlsplit, urlunsplit, urlencode

from fastapi import Request


def url_for(
    request: Request, view: str, path_params: dict = None, query_params: dict = None
) -> str:
    """Builds the url for a view, including query params"""
    if path_params is None:
        path_params = {}
    url = request.url_for(view, **path_params)

    if query_params is not None:
        query_params = {k: v for k, v in query_params.items() if v is not None}
        parsed_url = list(urlsplit(url))
        parsed_url[3] = urlencode(query_params)
        url = urlunsplit(parsed_url)
    return url
