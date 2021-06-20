import connect


class modelAccountData(connect.dataManagement):
	def show(self,orderby="users.id"):
		self.orderby = orderby
		result = []
		query = "SELECT users.id,username,password FROM users"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result

	def insert(self,username,password):
		self.username = username
		self.password = password
		query = "INSERT INTO users (username,password) VALUES ('{}','{}')".format(self.username,self.password)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def getByid(self, id=1):
		self.id = id
		result = []
		query = "SELECT users.id,username,password FROM users WHERE users.id = {}".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchone()
		return result

	def update(self,username,password,oldid):
		self.oldid = oldid
		self.username = username
		self.password = password
		query = "UPDATE users SET username = '{}', password = '{}' WHERE id = '{}'".format(self.username, self.password, self.oldid)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def delete(self,id):
		self.id = id
		query = "DELETE FROM users WHERE id = '{}'".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

class modelCakeData(connect.dataManagement):
	def show(self,orderby="cake.id"):
		self.orderby = orderby
		result = []
		query = "SELECT cake.id,name,stock,price FROM cake"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result

	def insert(self,name,stock,price):
		self.name = name
		self.stock = stock
		self.price = price
		query = "INSERT INTO cake (name,stock,price) VALUES ('{}','{}','{}')".format(self.name,self.stock,self.price)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def getByid(self, id=1):
		self.id = id
		result = []
		query = "SELECT cake.id,name,stock,price FROM cake WHERE cake.id = {}".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchone()
		return result

	def update(self,stock,price,oldid):
		self.oldid = oldid
		self.stock = stock
		self.price = price
		query = "UPDATE cake SET stock = '{}', price = '{}' WHERE id = '{}'".format( self.stock,self.price, self.oldid)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def delete(self,id):
		self.id = id
		query = "DELETE FROM cake WHERE id = '{}'".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()