import csv
import os
from clients.models import ClientModel

class ClientServices:
	"""docstring for ClientServices"""
	def __init__(self, table_name):
		self.table_name = table_name


	def create_client(self, client):
		with open(self.table_name, mode='a') as f:
			writer = csv.DictWriter(f, fieldnames=ClientModel.shema()) 
			writer.writerow(client.to_dic())

	def list_clients(self):
		with open(self.table_name, mode='r') as f:
			reader = csv.DictReader(f, fieldnames=ClientModel.shema())

			return list(reader)

		
	def update_client(self, update_client):
		clients = self.list_clients()

		update_clients = []
		for client in clients:
			if client['uid'] == update_client.uid:
				update_clients.append(update_client.to_dic())
			else:
				update_clients.append(client)

		self._save_to_disk(update_clients)

	def _save_to_disk(self, clients):
		tmp_table_name = self.table_name+'.tmp'
		with open(tmp_table_name, mode='w') as f:
			writer = csv.DictWriter(f, fieldnames=ClientModel.shema()) 
			writer.writerows(clients)

			os.remove(self.table_name)
			os.rename(tmp_table_name, self.table_name)
	

	def delete_client(self, delete_client):
		clients = self.list_clients()

		update_list_clients = []
		for client in clients:
			if client['uid'] != delete_client.uid:
				update_list_clients.append(client)

		self._save_to_disk(update_list_clients)

		