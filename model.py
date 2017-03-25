import web

#db = web.database(dbn='mysql', db='mercancia', user='root', pw='1234')
db = web.database(dbn='mysql',host='d6ybckq58s9ru745.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', db='cnc74aw4bsddu0ay', user='snytvadvrbx49ka5', pw='md7jjiruser10jgz')

def get_posts():
    return db.select('productos', order='id_producto')

def get_post(id):
    try:
        return db.select('productos', where='id_producto=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(producto,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
    db.insert('productos',
              producto=producto,
              descripcion= descripcion,
              existencias = existencias, 
              precio_compra= precio_compra,
              precio_venta= precio_venta, 
              imagen_producto= imagen_producto)

def del_post(id):
    db.delete('productos', where="id_producto=$id", vars=locals())

def update_post(id, producto, descripcion, existencias, precio_compra, precio_venta,imagen_producto):
    db.update('productos', where="id_producto=$id", vars=locals(),
        producto=producto, descripcion=descripcion, existencias = existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto = imagen_producto)

    
def insertar(producto,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
	db.insert('productos',
		producto=producto,
		descripcion= descripcion,
		existencias = existencias, 
		precio_compra= precio_compra,
		precio_venta= precio_venta, 
		imagen_producto= imagen_producto)