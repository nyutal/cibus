import getpass
from cibus.cibus_core import cibus_core
from cibus.cibussts import cibusts

class CibusCli(object):
    
    def main(self):
        user_name = 'nyutal'
        company = 'yahoo'
        password = getpass.getpass()
        with cibus_core.Cibus() as cibus:
            cibus.login(user_name, company, password)
            data = cibus.get_order_history()
            res = cibusts.CibusSts().get_last_week_sts(data)
            print(res)


if __name__== "__main__":
    CibusCli().main()
