"""Mapper File for Travel Schedule"""

from entity.travel_schedule import TravelSchedule
from dal.sqa.mapping.travel_schedule import DalTravelSchedule
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalTravelSchedule, TravelSchedule, "ToEntity")
mapper.create_map(TravelSchedule, DalTravelSchedule, "ToDal")
