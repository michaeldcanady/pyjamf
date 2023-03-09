from typing import Optional, Iterable, Union

from pyrestsdk.type.model import QueryOption, HeaderOption

from pyrestsdk.request.supports_types import SupportsGetMethod, SupportsInvokeCollectionRequest

from pyjamf.request._base_jamf_request import BaseJamfEntryRequest

from pyjamf.types.models import MobileDevice

class MobileDeviceEntryCollectionRequest(
    SupportsInvokeCollectionRequest,
    SupportsGetMethod,
    BaseJamfEntryRequest[MobileDevice]
):

    def __init__(self, request_url: str, client, options: Optional[Iterable[Union[QueryOption, HeaderOption]]]) -> None:
        super().__init__(request_url, client, options)
