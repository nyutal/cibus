from ..cibus_core import cibus_core
from ..cibus_core import consts
import datetime
import sys


class CibusSts(object):

    def _get_last_sunday_date(self):
        today = datetime.date.today()
        n_days_from_sunday = (today.weekday() + 1) % 7
        last_sunday = today - datetime.timedelta(days=n_days_from_sunday)
        return last_sunday

    def get_last_week_sts(self, orders):
        """[summary]
        
        Arguments:
            orders {Orders} -- accepted orders from cibus, assume ordered from lastest to oldest
        """

        last_sunday = self._get_last_sunday_date()
        last_week_orders = [o for o in orders if o.date >= last_sunday]
        total = sum(order.debit for order in last_week_orders)
        return total
        



