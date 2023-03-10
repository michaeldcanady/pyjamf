"""Houses Building Entry Request Type
"""

from typing import Optional, Iterable, Union

from pyrestsdk.type.model import QueryOption, HeaderOption

from typing import TYPE_CHECKING, Optional, Iterable, Union, TypeVar, List, Dict, Any, Type, Callable

from pyrestsdk.request.supports_types import SupportsGetMethod, SupportsInvokeRequest, SupportsDeleteMethod, SupportsPutMethod, SupportsPostMethod

from pyjamf.request.classic._base_jamf_request import BaseJamfEntryRequest

from pyjamf.types.classic.models import Building

if TYPE_CHECKING:
    from pyjamf.core import JamfServiceClient

J = TypeVar("J", bound="JamfServiceClient")


class BuildingEntryRequest(
    SupportsInvokeRequest,
    SupportsGetMethod,
    SupportsDeleteMethod,
    SupportsPutMethod,
    SupportsPostMethod,
    BaseJamfEntryRequest[Building]
):
    """Building Entry Request Type
    """

    def __init__(self, request_url: str, client: "JamfServiceClient", options: Optional[Iterable[Union[QueryOption, HeaderOption]]]) -> None:
        super().__init__(request_url, client, options)

    def parse_result(self, obj_type, result: Union[Dict[str, Any], List[Dict[str, Any]]], client: "JamfServiceClient") -> Union[List[J], J]:
        """parses return into expected return type

        Args:
            obj_type (_type_): _description_
            result (Union[Dict[str, Any], List[Dict[str, Any]]]): _description_
            client (JamfServiceClient): _description_

        Raises:
            Exception: _description_

        Returns:
            Union[List[J], J]: _description_
        """

        result = result["building"]

        _operation_dict: Dict[
            Type, Callable[[Union[Dict, List],
                            JamfServiceClient], Union[List[J], J]]
        ] = {
            dict: lambda x, y: obj_type.from_json(x, y),  # type: ignore
            list: lambda x, y: [obj_type.from_json(raw_result, y) for raw_result in x],
        }

        if (_func := _operation_dict.get(type(result), None)) is None:
            raise Exception(f"unexpected type: {type(result)}")

        return _func(result, client)
