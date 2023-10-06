from converter import Converter

# DW bilgieri
DATAWAREHOUSE_HOST = "host_name"
DATAWAREHOUSE_USER = "admin"
DATAWAREHOUSE_PASSWORD = "12345"
port_number = 8080


uri = "mongodb+srv://admin:admin@cluster0.smovknl.mongodb.net/?retryWrites=true&w=majority"
mysql_bilgilerim = {'host': DATAWAREHOUSE_HOST, 'user': DATAWAREHOUSE_USER, 'password': DATAWAREHOUSE_PASSWORD, 'port': port_number, 'database': 'your_db_name'}

my_converter = Converter(uri, **mysql_bilgilerim)
my_converter.mysql_to_mongodb('test_table')


