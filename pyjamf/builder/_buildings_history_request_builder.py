"""Houses Advanced Mobile Device Searches Choices Request Builder Type"""

from typing import Optional, Iterable

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyjamf.builder._buildings_history_export_request_builder import BuildingsHistoryExportRequestBuilder

class BuildingsHistoryRequestBuilder(EntityRequestBuilder):
    """Advanced Mobile Device Searches Choices Request Builder Type"""

    def __init__(self, request_url: str, client) -> None:
        """intializes a new DepartmentsRequestBuilder

        Args:
            request_url (str): the url to make the request to
            client (_type_): the client used to make the request
        """
        super().__init__(request_url, client)
        
    @property
    def export(self) -> BuildingsHistoryExportRequestBuilder:
        
        return BuildingsHistoryExportRequestBuilder(self.append_segment_to_request_url("export"), self.request_client)
        
    def request_with_options(self, options: Optional[Iterable[O]]) -> R:
        pass