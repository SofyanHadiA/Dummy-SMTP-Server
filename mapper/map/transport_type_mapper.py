"""Mapper File for Transport Type"""

from entity.transport_type import TransportType
from dal.sqa.mapping.transport_type import DalTransportType
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalTransportType, TransportType, "ToEntity")
mapper.create_map(TransportType, DalTransportType, "ToDal")
