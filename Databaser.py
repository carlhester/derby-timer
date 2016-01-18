import sqlite3

class Databaser:
	
	connection = 0

	def __init__(self):
		self.connection = self._connect()

	def _connect(self):
		return sqlite3.connect('racers.db')

	def commit(self):
		self.connection.commit()
					
	def SQL(self, query):
		self.connection.execute(query)


