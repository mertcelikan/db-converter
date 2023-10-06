from converter import Converter

# DW bilgieri
DATAWAREHOUSE_HOST = ""
DATAWAREHOUSE_USER = "bi-admin"
DATAWAREHOUSE_PASSWORD = ""
port_number = 3308


uri = "mongodb+srv://admin:admin@cluster0.smovknl.mongodb.net/?retryWrites=true&w=majority"
mysql_bilgilerim = {'host': DATAWAREHOUSE_HOST, 'user': DATAWAREHOUSE_USER, 'password': DATAWAREHOUSE_PASSWORD, 'port': port_number, 'database': 'your_db_name'}

my_converter = Converter(uri, **mysql_bilgilerim)
my_converter.mysql_to_mongodb('test_table')


