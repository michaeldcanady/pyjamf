"""Houses Department Type"""

from __future__ import annotations

from typing import TypeVar, TYPE_CHECKING, Type, Dict

from abc import abstractmethod

from pyjamf.types.classic.models._abstract_jamf_entity import AbstractJAMFEntity

if TYPE_CHECKING:
    from pyjamf.core import JamfServiceClient

E = TypeVar("E", bound="AbstractDepartment")

class AbstractDepartment(AbstractJAMFEntity):
    """Abstract Department Type
    """
    
    _id: int
    _name: str
    
    @abstractmethod
    def __init__(self: E, client: JamfServiceClient) -> None:
        super().__init__(client)
    
    @property
    @abstractmethod
    def id(self) -> int: ...

    @property
    @abstractmethod
    def name(self) -> str: ...
    
    @classmethod
    @abstractmethod
    def from_json(cls: Type[E], entry: Dict, client: JamfServiceClient) -> E: ...
