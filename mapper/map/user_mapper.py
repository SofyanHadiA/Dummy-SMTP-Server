"""Mapper File for User"""

from entity.employee import Employee
from dal.sqa.mapping.user import DalUser
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalUser, Employee, "ToEntity")
mapper.create_map(Employee, DalUser, "ToDal")

