use cnc74aw4bsddu0ay;

create table productos(
	id_producto int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	producto varchar(40) NOT NULL,
	descripcion varchar(400) NOT NULL,
	existencias int(11) NOT NULL,
	precio_compra double(11,2) NOT NULL,
	precio_venta double(11,2) NOT NULL,
	imagen_producto varchar(100) NOT NULL
	);