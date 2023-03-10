"""Houses Jamf Classic Request Builder Type"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyrestsdk.requestbuilder import BaseRequestBuilder

from pyjamf.builder.classic._advanced_computer_search_request_builder import AdvancedComputerSearchesRequestBuilder
from pyjamf.builder.classic._building_request_builder import BuildingRequestBuilder
from pyjamf.builder.classic._category_request_builder import CategoryRequestBuilder
from pyjamf.builder.classic._computer_group_request_builder import ComputerGroupRequestBuilder

if TYPE_CHECKING:
    from pyjamf.core import JamfServiceClient


class JamfClassicRequestBuilder(BaseRequestBuilder):
    """Jamf Classic Request Builder Type
    """

    def __init__(self, request_url: str, client: JamfServiceClient) -> None:
        """intializes a new JamfClassicRequestBuilder

        Args:
            request_url (str): the url to make the request to
            client (JamfServiceClient): the client used to make the request
        """
        super().__init__(request_url, client)

    @property
    def advanced_computer_searches(self) -> AdvancedComputerSearchesRequestBuilder:
        """Creates Advanced Computer Searches Request Builder

        Returns:
            AdvancedComputerSearchesRequestBuilder: The Advanced Computer Searches Request Builder
        """

        return AdvancedComputerSearchesRequestBuilder(self.append_segment_to_request_url("advancedcomputersearches"), self.request_client)

    @property
    def buildings(self) -> BuildingRequestBuilder:
        """Creates Building Request Builder

        Returns:
            BuildingRequestBuilder: The Building Request Builder
        """

        return BuildingRequestBuilder(self.append_segment_to_request_url("buildings"), self.request_client)

    @property
    def category(self) -> CategoryRequestBuilder:
        """Creates Category Request Builder

        Returns:
            CategoryRequestBuilder: The Category Request Builder
        """

        return CategoryRequestBuilder(self.append_segment_to_request_url("category"), self.request_client)

    @property
    def computer_groups(self) -> ComputerGroupRequestBuilder:
        """Creates Computer Group Request Builder

        Returns:
            ComputerGroupRequestBuilder: The Computer Group Request Builder
        """

        return ComputerGroupRequestBuilder(self.append_segment_to_request_url("computergroups"), self.request_client)
