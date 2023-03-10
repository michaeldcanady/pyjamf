from typing import Optional, Iterable, Union

from pyrestsdk.type.model import QueryOption, HeaderOption

from typing import  TYPE_CHECKING, Optional, Iterable, Union, TypeVar, List, Dict, Any, Type, Callable

from pyrestsdk.request.supports_types import SupportsGetMethod, SupportsInvokeRequest

from pyjamf.request.classic._base_jamf_request import BaseJamfEntryRequest

from pyjamf.types.classic.models import ComputerGroup

if TYPE_CHECKING:
    from pyjamf.core import JamfServiceClient
    
J = TypeVar("J", bound="JamfServiceClient")

class ComputerGroupEntryCollectionRequest(
    SupportsInvokeRequest,
    SupportsGetMethod,
    BaseJamfEntryRequest[ComputerGroup]
):

    def __init__(self, request_url: str, client, options: Optional[Iterable[Union[QueryOption, HeaderOption]]]) -> None:
        super().__init__(request_url, client, options)

    
    def parse_result(self, obj_type, result: Union[Dict[str, Any], List[Dict[str, Any]]], client) -> Union[List[J], J]:
        """parses return into expected return type"""
        
        result = result["computer_groups"]

        _operation_dict: Dict[
            Type, Callable[[Union[Dict, List], JamfServiceClient], Union[List[J], J]]
        ] = {
            dict: lambda x, y: obj_type.from_json(x, y),  # type: ignore
            list: lambda x, y: [obj_type.from_json(raw_result, y) for raw_result in x],
        }

        if (_func := _operation_dict.get(type(result), None)) is None:
            raise Exception(f"unexpected type: {type(result)}")

        return _func(result, client)