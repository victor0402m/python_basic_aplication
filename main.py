
clients = [
	{
		'name': 'juan',
		'age': '28',
		'company': 'google',
		'job': 'designer',
	},
	{
		'name': 'victor',
		'age': '25',
		'company': 'QuercusDev',
		'job': 'Developer',
	}
]

def create_client(client):
	global clients
	if get_client_by_name(client.get('name')) == None:
		clients.append(client)
	else:
		print("Client already in the client's list")
	return clients

def update_client(client_id, new_client):
	global clients
	
	if client_id != None:
		clients[client_id] =  new_client
		return clients
	else:
		print('Client not exist')

def list_client():
	global clients
	for idx, client in enumerate(clients):
		print('{uuid} | {name} | {age} | {company} | {job}'.format(
			uuid=idx,
			name=client['name'],
			age=client['age'],
			company=client['company'],
			job=client['job']
			)
		)

def search_client(client_id):
	global clients
	if client_id == None:
		return False
	else:
		return True

def delete_client(client_id):
	global clients
	if client_id != None:
		del clients[client_id]
	else:
		print('Client not exist')


def _get_client_index():
	global clients
	client_name =  None

	while not client_name:
		client_name = input('What is the name of the client? ')
		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
		sys.exit()
	else:
		return get_client_by_name(client_name)
		

def get_client_by_name(client_name):
	global clients
	for idx, client in enumerate(clients):
		print("----")
		print(client.get('name'))
		print(client_name)
		if client.get('name') == client_name:
	 		return idx
	return None


def get_client_field(field_name):
	client_data =  None

	while not client_data:
		client_data = input('What is the client {}? '.format(field_name))
		
	return client_data

def get_client():
	client = {
		'name': get_client_field('name'),
		'age': get_client_field('age'),
		'company': get_client_field('company'),
		'job': get_client_field('job'),
	}
	return client

def _print_welcom():
	print('Welcom to Vic vents')
	print('*'*50)
	print('What would you like to do today?')
	print('[C] Create a client')
	print('[D] Delete a client')
	print('[U] Update a client')
	print('[S] Search a client')
	print('[L] List  clients')

if __name__ == '__main__':
	_print_welcom()

	acction = input()
	acction = acction.upper()

	if acction == 'C':
		client = get_client()
		create_client(client)
	elif acction == 'D':
		client_id = _get_client_index()
		delete_client(client_id)
	elif acction == 'U':
		client_id = _get_client_index()
		print('----------New Data----------')
		new_client = get_client()
		update_client(client_id, new_client)
	elif acction == 'S':
		client = _get_client_index()
		search = search_client(client)
		if search:
			print("Client exist")
		else:
			print("Client not exist")
	elif acction == 'L':
		list_client()
	else:
		print('The acction is unknown')

	list_client()

