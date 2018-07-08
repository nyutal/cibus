import requests
import getpass
from contextlib import contextmanager
from bs4 import BeautifulSoup
from lxml import html
from .order import Order
from .consts import Consts

from . import cibusexceptions

class Cibus(object):

    SITE_URL = 'https://www.mysodexo.co.il/'
    ORDER_HISTORY_URL = ''.join([SITE_URL,'new_my/new_my_orders.aspx'])
    
    def __init__(self):
        self.session = requests.Session()
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        # print('close cibus')
        pass

    def login(self, user_name, company, password):
        login_page = self.session.get(Cibus.SITE_URL).text
        tree = html.fromstring(login_page)
        token_val = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
        token2_val = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]
        payload = {
            "txtUsr": user_name,
            "txtPas": password,
            "txtCmp": company,
            '__VIEWSTATE':  token_val,
            '__VIEWSTATEGENERATOR': token2_val,
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'remember_me': 'on',
            'ctl09': '',
            'ctl13': '',
        }
        res = self.session.post(Cibus.SITE_URL, data=payload, allow_redirects=True)
        if res.url == Cibus.SITE_URL:
            raise cibusexceptions.CibusFailedConnect()

    def get_order_history(self):
        page = self.session.get(Cibus.ORDER_HISTORY_URL)
        soup = BeautifulSoup(page.text, "lxml")
        table = soup.find('table', attrs={'class':'fixed-table bar foot'})
        # table_body = table.find('tbody')
        rows = table.find_all('tr', attrs={'class':'del'}) #filter only valid transaction
        row_and_columns = [row.find_all('td') for row in rows[:-1]] #(:-1) to drop last summary column
        data = [[col.text.strip() for col in row] for row in row_and_columns]
        
        orders = [Order(d[Consts.DATE_IDX], d[Consts.DEBIT_IDX], d[Consts.STS_IDX], d[Consts.RESTAURANT_IDX]) for d in data]
        return orders

    
    def get_last_week_expenses(self):
        orders = self.get_order_history()
        print(orders[:2])


    
    def context(self):
        with requests.Session() as s:
            self.s = s 
            return self

# def main():
#     user_name = 'nyutal'
#     company = 'yahoo'
#     password = getpass.getpass()
#     with Cibus() as cibus:
#         cibus.login(user_name, company, password)
#         cibus.get_last_week_expenses()



# if __name__== "__main__":
    # main()
        
    
    



        