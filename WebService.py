#!/usr/bin/python2.7
import web
import xml.etree.ElementTree as ET
from mysql.connector import errorcode
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
import json
import requests


tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/GetImgs/(.*)', 'get_imgs',
    '/Insert/(.*)/(.*)', 'Insert'
)

app = web.application(urls, globals())

class list_users:        
    def GET(self):
	output = '';
	cnx = mysql.connector.connect(user='root', password='',host='localhost',database='test')
	cur = cnx.cursor()
	select_stmt = "SELECT * FROM sexo"
	cur.execute(select_stmt)
	vosa = cur.fetchall()
	output += str(vosa)
	
	
	
	cur.close()
	cnx.close()
        return output
        
class get_imgs:
    def GET(self, user):
	output = '';
	cnx = mysql.connector.connect(user='root', password='',host='localhost',database='DbServicioPython1')
	cur = cnx.cursor()
	select_stmt = "SELECT IdUsuario,URL FROM tbl_Imgs WHERE IdUsuario=%s"
	cur.execute(select_stmt,(user))
	rows = cur.fetchall()
	count = 0
	employee=cur.fetchone()
	
	for row in rows:
	    while (count < len(row)-1):
	        output+= str(row[count])+","
	        count = count + 1
	        output+= str(row[count])
	        output+= str(",")
	    count=0       
   
	cur.close()
	cnx.close()
        return json.dumps(output)  
        
        
class Insert:
    def GET(self, IdUsuario,URL):
	output = '';
	cnx = mysql.connector.connect(user='root', password='',host='localhost',database='DbServicioPython1')
	cur = cnx.cursor()
	select_stmt = "INSERT INTO  tbl_Imgs VALUES (%s,%s)"
	try:
	    cur.execute(select_stmt,(IdUsuario,URL))
	    cnx.commit()
	    cur.close()
	    cnx.close()
	    output="Insertado"
	except:
	  cnx.rollback()  
	  output="Error"   
        return json.dumps(output)
    

class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib["id"] == user:
		    d = json.dumps(child.attrib)
		    callback = 'jsoncallback'
		    return d
if __name__ == '__main__':
  app.run()
  