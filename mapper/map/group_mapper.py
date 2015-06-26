"""Mapper File for Group"""

from entity.group import Group
from dal.sqa.mapping.group import DalGroup
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalGroup, Group, "ToEntity")
mapper.create_map(Group, DalGroup, "ToDal")
