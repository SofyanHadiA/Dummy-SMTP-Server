"""Mapper File for UserLogin"""
from entity.user_login import UserLogin
from dal.sqa.mapping.user_login import DalUserLogin
from mapper.object_mapper import ObjectMapper

mapper = ObjectMapper()
mapper.create_map(DalUserLogin, UserLogin, "ToEntity")
mapper.create_map(UserLogin, DalUserLogin, "ToDal")

def to_dal(user_login):
    dal_user_login = DalUserLogin()
    dal_user_login.token = user_login.token
    dal_user_login.expiry_date_time = user_login.expiry_date_time
    dal_user_login.login_id = user_login.login_id
    dal_user_login.user_id = user_login.user_id

    return dal_user_login

mapper.to_dal = to_dal
