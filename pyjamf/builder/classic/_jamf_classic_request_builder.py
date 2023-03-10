"""Houses Jamf Classic Request Builder Type"""

from pyrestsdk.requestbuilder import BaseRequestBuilder

from pyjamf.builder.classic._computer_group_request_builder import ComputerGroupRequestBuilder
from pyjamf.builder.classic._advanced_computer_search_request_builder import AdvancedComputerSearchesRequestBuilder
from pyjamf.builder.classic._building_request_builder import BuildingRequestBuilder

class JamfClassicRequestBuilder(BaseRequestBuilder):
    """Jamf Classic Request Builder Type"""

    def __init__(self, request_url: str, client) -> None:
        """intializes a new JamfClassicRequestBuilder

        Args:
            request_url (str): the url to make the request to
            client (_type_): the client used to make the request
        """
        super().__init__(request_url, client)
    
    @property
    def advanced_computer_searches(self) -> AdvancedComputerSearchesRequestBuilder:
        
        return AdvancedComputerSearchesRequestBuilder(self.append_segment_to_request_url("advancedcomputersearches"), self.request_client)
    
    @property
    def computer_groups(self) -> ComputerGroupRequestBuilder:
        
        return ComputerGroupRequestBuilder(self.append_segment_to_request_url("computergroups"), self.request_client)
    
    @property
    def buildings(self) -> BuildingRequestBuilder:
        
        return BuildingRequestBuilder(self.append_segment_to_request_url("buildings"), self.request_client)