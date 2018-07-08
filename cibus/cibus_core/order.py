import attr
import datetime
from .consts import Consts

def date_converter(date_str: str):
    return datetime.datetime.strptime(date_str, Consts.DATE_FORMAT).date()
    

@attr.s
class Order(object):
    date = attr.ib(converter=date_converter)
    debit = attr.ib(converter=float)
    sts = attr.ib(type=str)
    restaurant = attr.ib(type=str)