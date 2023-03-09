"""PyJamf Requests"""

from pyjamf.request._advanced_mobile_device_searches_choices_entry_collection_request import AdvancedMobileDeviceSearchesChoicesEntryCollectionRequest
from pyjamf.request._advanced_mobile_device_searches_entry_collection_request import AdvancedMobileDeviceSearchesEntryCollectionRequest
from pyjamf.request._advanced_mobile_device_searches_entry_request import AdvancedMobileDeviceSearchesEntryRequest

from pyjamf.request._advanced_user_content_searches_entry_collection_request import AdvancedUserContentSearchesEntryCollectionRequest
from pyjamf.request._advanced_user_content_searches_entry_request import AdvancedUserContentSearchesEntryRequest

from pyjamf.request._app_dynamics_script_configuration_entry_collection_request import AppDynamicsScriptConfigurationEntryCollectionRequest

from pyjamf.request._departments_collection_request import DepartmentsCollectionRequest

from pyjamf.request._mobile_device_entry_collection_request import MobileDeviceEntryCollectionRequest
from pyjamf.request._mobile_device_entry_request import MobileDeviceEntryRequest

__all__ = [
    "AdvancedMobileDeviceSearchesChoicesEntryCollectionRequest",
    "AdvancedMobileDeviceSearchesEntryCollectionRequest",
    
    "AdvancedMobileDeviceSearchesEntryRequest",
    "AdvancedUserContentSearchesEntryCollectionRequest",
    
    "AppDynamicsScriptConfigurationEntryCollectionRequest",
    
    "AdvancedUserContentSearchesEntryRequest",
    "DepartmentsCollectionRequest",
    
    "MobileDeviceEntryCollectionRequest",
    "MobileDeviceEntryRequest",
]
