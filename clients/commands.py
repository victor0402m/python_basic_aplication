import click

from clients.services import ClientServices 
from clients.models import ClientModel

@click.group()
def clients():
	""" Manage the clients lifecycle"""
	pass


@clients.command()
@click.option('-n','--name',
				type=str,
				prompt=True,
				help='The client name ')
@click.option('-a','--age',
				type=str,
				prompt=True,
				help='The client age ')
@click.option('-c','--company',
				type=str,
				prompt=True,
				help='The client company ')
@click.option('-j','--job',
				type=str,
				prompt=True,
				help='The client job ')
@click.pass_context
def create(ctx, name, age, company, job):
	""" Create new clients """
	client = ClientModel(name, age, company, job)
	client_services =  ClientServices(ctx.obj['clients_table'] )
	client_services.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
	""" List clients"""
	client_services = ClientServices(ctx.obj['clients_table'])
	clients_list = client_services.list_clients()
	click.echo('uuid | name | age | company | job')
	click.echo("*"*70)
	for client in clients_list:
		click.echo('{uid} | {name} | {age} | {company} | {job}'.format(
			uid=client['uid'],
			name=client['name'],
			age=client['age'],
			company=client['company'],
			job=client['job']
			)
		)


@clients.command()
@click.argument('client_uid',
	type=str)
@click.pass_context
def update(ctx, client_uid):
	""" Update a client"""
	client_services = ClientServices(ctx.obj['clients_table'])

	clients_list = client_services.list_clients()

	client = [client for client in clients_list if client['uid'] == client_uid]

	if client:
		client = _update_client_flow(ClientModel(**client[0]))
		client_services.update_client(client)
		click.echo('Client updated')
	else:
		click.echo('Client not fount')


def _update_client_flow(client):
	click.echo('Leave emty if you dont want to modify the value')
	
	client.name = click.prompt('New name ', type=str, default=client.name)
	client.age = click.prompt('New age ', type=str, default=client.age)
	client.company = click.prompt('New company ', type=str, default=client.company)
	client.job = click.prompt('New job ', type=str, default=client.job)

	return client


@clients.command()
@click.argument('client_uid',
	type=str)
@click.pass_context
def delete(ctx, client_uid):
	""" Delete a client"""
	client_services = ClientServices(ctx.obj['clients_table'])

	clients_list = client_services.list_clients()

	client = [client for client in clients_list if client['uid'] == client_uid]

	if client:
		client = ClientModel(**client[0])
		client_services.delete_client(client)
		click.echo('Client deleted')
	else:
		click.echo('Client not fount')



all = clients