"""Mapper File for Booking"""

from entity.booking import Booking
from dal.sqa.mapping.booking import DalBooking
from mapper.object_mapper import ObjectMapper


class BookingMapper:
    def __init__(self):
        self.__mapper = ObjectMapper()
        self.__mapper.create_map(DalBooking, Booking, "ToEntity")
        self.__mapper.create_map(Booking, DalBooking, "ToDal")

    def to_entity(self, dal_booking=DalBooking):
        return self.__mapper.map(dal_booking, "ToEntity")

    def to_dal(self, booking):
        dal_booking = DalBooking()
        dal_booking.booking_id = booking.booking_id
        dal_booking.booking_date = booking.booking_date
        dal_booking.booking_status = booking.booking_status
        dal_booking.booking_type = booking.booking_type
        dal_booking.passenger_id = booking.passenger_id
        dal_booking.schedule_id = booking.schedule_id
        dal_booking.book_by = booking.book_by

        return dal_booking
