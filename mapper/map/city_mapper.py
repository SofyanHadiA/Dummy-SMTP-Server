"""Mapper File for City"""

from entity.geography import City
from dal.sqa.mapping.city import DalCity
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalCity, City, "ToEntity")
mapper.create_map(City, DalCity, "ToDal")
