import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Nombre de usuario')
@click.option('--lastname', required=True, help='apellido de usuario')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('el nombre y apellido son requeridos')
    else:
        data= json_manager.read_json()
        new_id =len(data) +1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"Usuario {name} {lastname} se creo correctamente con el ID {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print (f"{user['id']} - {user['name']} - {user['lastname']}")
        

@cli.command()
@click.argument('id', type= int )
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"el usuario con ID: {id} no se encuentra")
    else:
        print (f"{user['id']} - {user['name']} - {user['lastname']}")
        
        
@cli.command()
@click.argument('id', type= int )
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"el usuario con ID: {id} no se encuentra")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"usuario con el ID:{id} se elimino correctamente")
        
        
@cli.command()
@click.argument('id', type=int)
@click.option('--name', help= 'Nombre de usuario')
@click.option('--lastname', help= 'Apellido de usuario')
def updateUser(id, name, lastname):
    data= json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name']= name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f"Usuario con el ID:{id} se actualizo correctamente")        
        
        
        
if __name__ == '__main__':
    cli()
    
