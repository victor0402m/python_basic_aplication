
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
	if client not in clients:
		clients.append(client)
	else:
		print("Client already in the client's list")
	return clients

def update_client(client, new_client):
	global clients

	if client in clients:
		index = clients.index(client)
		clients[index] =  new_client
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

def search_client(client_name):
	global clients
	for client in clients:
		if client != client_name:
			continue
		else:
			return True

def delete_client(client):
	global clients
	if client in clients:
		clients.remove(client)
	else:
		print('Client not exist')


def _get_client_index():
	client_name =  None

	while not client_name:
		client_name = input('What is the name of the client? ')
		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
		sys.exit()

	return client_name


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
		client = _get_client_index()
		delete_client(client)
	elif acction == 'U':
		client = _get_client_index()
		print('What is the new client?')
		new_client = input()
		update_client(client, new_client)
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

