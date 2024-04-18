# import pymysql
# conn = pymysql.connect(host='192.168.122.110', port=30829,
#                        user='root', password='root',
#                        db='data',charset='utf8')

# cur = conn.cursor()
# cur.execute("select now() from dual;")
# result = cur.fetchall()
# print(result)
# cur.close()
# conn.close()

import sqlalchemy

def get_connection():
    id = 'root'
    passwd = 'root'
    host ='192.168.122.110'
    port = '30829'
    db = 'data'
    return sqlalchemy.create_engine("mysql+pymysql://" + id + ":" + passwd + "@" 
                                    + host + ":" + port + "/" + db+'?charset=utf8mb4')
 