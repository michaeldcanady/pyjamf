import os

from pyjamf.identity import UsernamePasswordCredential
from pyjamf.core import JamfServiceClient
from pyjamf.types.classic.models import Building

def building_collection_test():
    
    credential = UsernamePasswordCredential(os.environ["INSTANCE"], os.environ["USERNAME"], os.environ["PASSWORD"])

    client = JamfServiceClient(credential, os.environ["INSTANCE"])
    
    buildings = client.classic_api.buildings.request.Get.invoke_request
    
    assert isinstance(buildings, list)
    assert isinstance(buildings[0], Building)

def building_by_id_test():

    credential = UsernamePasswordCredential(os.environ["INSTANCE"], os.environ["USERNAME"], os.environ["PASSWORD"])

    client = JamfServiceClient(credential, os.environ["INSTANCE"])

    building = client.classic_api.buildings.request_by_id("2").Get.invoke_request
    
    assert isinstance(building, Building)
    
def building_by_name_test():
    
    credential = UsernamePasswordCredential(os.environ["INSTANCE"], os.environ["USERNAME"], os.environ["PASSWORD"])

    client = JamfServiceClient(credential, os.environ["INSTANCE"])
    
    building = client.classic_api.buildings.request_by_name("Commons 1").Get.invoke_request
    
    assert isinstance(building, Building)