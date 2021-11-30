# from ywzt.config.get_path import GetPath

driver_type = 'chrome'
base_url = 'http://erp-test.rantion.com/login/'
username = '廖宏'
password = '000000'
# project_dir = GetPath().get_itme_path()

# 连接uat的ssh信息
ssh_ip = '39.108.109.23'
ssh_port = 27391
ssh_user = 'develop'
ssh_passwd = 'Dev@2021#Rl!~'


# 连接uat的信息
uat_ip = '172.18.35.172'
uat_port = 3306
uat_user = 'root'
uat_passwd = 'Ran@tion2021#2'
uat_db = 'rantion_stock'

# sql与语句
sql = 'select use_qty from stock_sku where sku="EB0110" and warehouse_name="美西仓"'
