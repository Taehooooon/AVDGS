import pymssql

server = '192.168.1.189'
database = 'VDGS' 
username = '2VDGSIF'
password = '2VI'

cnxn = pymssql.connect(server, username, password, database)
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.excute("select top 5 * from [dbo].[EAI_DISPINFOAFL_RCV]")
row = cursor.fetchone()

while row:
    print(row[0], row[1], row[2])
    row = cursor.fetchone()

cnxn.close()


# sql = '''select top 5 * from [dbo].[EAI_DISPINFOIIS_RCV]'''

# res = cursor.excute()

# standID = '231'
# queryArr = []
# queryArr.append("SELECT")
# queryArr.append("*")
# queryArr.append("FROM DISPLAYTEXT")
# queryArr.append("Where stand ID = ")
# queryArr.append(standID)
# queryStr = " ".join(queryArr)

# print(queryArr)
# print(queryStr)