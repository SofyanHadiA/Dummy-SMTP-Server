"""Mapper File for Country"""

from entity.geography import Country
from dal.sqa.mapping.country import DalCountry
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalCountry, Country, "ToEntity")
mapper.create_map(Country, DalCountry, "ToDal")
