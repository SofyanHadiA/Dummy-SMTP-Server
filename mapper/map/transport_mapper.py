"""Mapper File for Transport"""

from entity.transport import Transport
from dal.sqa.mapping.transport import DalTransport
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalTransport, Transport, "ToEntity")
mapper.create_map(Transport, DalTransport, "ToDal")
