import sqlite3
class dataManagement:
	def __init__(self):
		self.isDebug = False
		self.conn = sqlite3.connect('myDb.sqlite3')
		self.cur = self.conn.cursor() # instantiate a cursor obj