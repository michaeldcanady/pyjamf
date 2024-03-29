"""Houses Category Entry Collection Request Type
"""
from __future__ import annotations

from typing import Optional, Iterable, Union, TYPE_CHECKING, Optional, Iterable, Union, TypeVar, List, Dict, Any, Type, Callable

from pyrestsdk.type.model import QueryOption, HeaderOption

from pyrestsdk.request.supports_types import SupportsGetMethod, SupportsInvokeCollectionRequest

from pyjamf.request.classic._base_jamf_request import BaseJamfEntryRequest

from pyjamf.types.classic.models import Category
from pyjamf.types import RequestType

if TYPE_CHECKING:
    from pyjamf.core import JamfServiceClient


class CategoryEntryCollectionRequest(
    SupportsInvokeCollectionRequest,
    SupportsGetMethod,
    BaseJamfEntryRequest[Category]
):
    """Category Entry Collection Request Type
    """
    
    __request_type__ = RequestType.Multiple
    __results_key__ = "categories"

    def __init__(self, request_url: str, client: JamfServiceClient, options: Optional[Iterable[Union[QueryOption, HeaderOption]]]) -> None:
        super().__init__(request_url, client, options)
