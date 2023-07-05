----------------------------------------------------
-- Creacion de Base de Datos usuario y contraseña
----------------------------------------------------
CREATE DATABASE MasterBikeDB;
CREATE USER masterbike@localhost IDENTIFIED BY 'projectmasterbike';
GRANT ALL PRIVILEGES ON masterbikedb.* TO django@localhost;
FLUSH PRIVILEGES;
USE MasterBikeDB;

---------------------------------------------------------
-- Creacion de tablas datos para pruebas
---------------------------------------------------------

---------------------------------------------------------
-- Tabla Regiones
---------------------------------------------------------
INSERT INTO core_region(nombreRegion) VALUES
("Región de Arica y Parinacota"),("Región de Tarapacá"),("Región de Antofagasta"),("Región de Atacama"),("Región de Coquimbo"),
("Región de Valparaíso"),("Región Metropolitana"),("Región de O’Higgins"),("Región del Maule"),("Región del Ñuble"),
("Región del Biobío"),("Región de La Araucanía"),("Región de Los Ríos"),("Región de Los Lagos"),("Región de Aysén"),
("Región de Magallanes");


---------------------------------------------------------
-- Tabla Comunas
---------------------------------------------------------
INSERT INTO core_comuna(nombreComuna, region_id) VALUES
("Alhué",7),("Buin",7),("Calera de Tango",7),("Cerrillos",7),("Cerro Navia",7),("Colina",7),("Conchalí",7),
("Curacaví",7),("El Bosque",7),("El Monte",7),("Estación Central",7),("Huechuraba",7),("Independencia",7),
("Isla de Maipo",7),("La Cisterna",7),("La Florida",7),("La Granja",7),("Lampa",7),("La Pintana",7),
("La Reina",7),("Las Condes",7),("Lo Barnechea",7),("Lo Espejo",7),("Lo Prado",7),("Macul",7),("Maipú",7),
("María Pinto",7),("Melipilla",7),("Ñuñoaaaaaaa",7),("Padre Hurtado",7),("Paine",7),("Pedro Aguirre Cerda",7),
("Peñaflor",7),("Peñalolén",7),("Pirque",7),("Providencia",7),("Pudahuel",7),("Puente Alto",7),("Quilicura",7),
("Quinta Normal",7),("Recoleta",7),("Renca",7),("San Bernardo",7),("San Joaquín",7),("San José de Maipo",7),
("San Miguel",7),("San Pedro",7),("San Ramón",7),("Santiago",7),("Talagante",7),("Tiltil",7),("Vitacura",7);

---------------------------------------------------------
-- Tabla Producto
---------------------------------------------------------
INSERT INTO core_producto(nombreProducto, caracteristicaProducto, precioProducto, categoria_id, activo, destacado, imagen, slug, stock) VALUES
("Casco Rideland","Casco de bicicleta Rideland para hombre y mujer, ligeros para andar en montañas o carretera.", 25000 , 3, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186002/casco_ogxwws.jpg", "casco-rideland", 10),
("Sillin Topmega","Sillin Topmega con Tecnologia de alto nivel, permitiendo que puedas estar mucho más tiempo cómodo realizando deporte de alta intensidad.", 22500 , 2, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186001/asiento_pfz9cx.jpg", "sillin-topmega", 15),
("Horquilla Rockshox","El Lyrik Select combina la cámara de aire DebonAir con el confiable amortiguador Charger RC que ofrece compresión a baja velocidad y control de amortiguación de rebote.", 45000 , 2, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186001/amortiguadores_tt2f14.jpg", "horquilla-rockshox", 40),
("Set Proteccion RODA","Protección, actitud y comodidad! Es lo que te entrega este Set de Protección RODA. Fue diseñado pensando en entregar máxima protección y confort en su uso, entregando un toque de estilo.", 22000, 3, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186003/kit_protector_qx5v5b.jpg", "set-proteccion-roda", 55),
("Bicicleta Trek Madone","La Madone SL 6 ofrece un rendimiento aerodinámico avanzado y las sensaciones de nuestra bicicleta de competición definitiva.", 390000, 1, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186002/bici_de_3_palos_ctwgsx.png", "bicicleta-trek-madone", 20),
("Frenos disco Shimano M445 delantero","Asequible sistema de frenos de disco hidráulicos. Diseño aerodinámico de la palanca de freno.", 30000, 2, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186003/frenosShimano_orr92w.jpg", "frenos-disco-shimano-m445-delantero", 30),
("Guante Sixsixone Raji Glove","Es un guante liviano con una parte superior de malla de sarga elástica en el dorso de la mano y una palma de una sola capa con la parte superior de la palma para una protección sin ampollas, sin sacrificar la sensación de agarre.", 18000, 3, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186003/guantes_peiewi.jpg", "guante-sixsixone-raji-glove", 50),
("Bicicleta MTB TREK MARLIN 5","La Marlin 5 es una bicicleta de uso diario apta para las aventuras cotidianas, dentro y fuera de los senderos.", 650000, 1, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688186002/bicimonta%C3%B1era_wejfzq.jpg", "bicicleta-mtb-trek-marlin-5", 25),
("Oxford Halley","Atraviesa la ciudad y también la montaña con este modelo de marco de aluminio y frenos de disco mecánico que optimizarán tu recorrido mientras pedaleas.", 190000, 1, 1, 1, "https://res.cloudinary.com/dntrffhra/image/upload/v1688238047/Oxford-bike-27_5_nh8xo0.jpg", "oxford-halley", 35);

---------------------------------------------------------
-- Tabla Categoria
---------------------------------------------------------
INSERT INTO core_categoria(nombreCategoria, activo, slug) VALUES
("Bicicletas",1 ,"bicicletas"), ("Repuestos",1 ,"repuestos"), ("Accesorios",1 ,"accesorios"), ("Pedales",1 ,"pedales");

---------------------------------------------------------
-- Tabla Usuario
---------------------------------------------------------
INSERT INTO core_usuario(nombreUsuario, apellidoUsuario, rutUsuario, emailUsuario, contraseniaUsuario, direccionUsuario, comuna_id )VALUES 
("Carlos", "Mercury","13.564.331-3","cm13@pequeño.com", "ridioGaga", "baker street 21b",33),
("Thony", "Funeke","23.931.144-4","tfuneke@funao.com", "funekx100pre", "calle funable 3000",12);

---------------------------------------------------------
-- Selects distintos
---------------------------------------------------------
SELECT * FROM core_producto;
SELECT * FROM core_categoria;
SELECT * FROM core_usuario;
SELECT * FROM core_listacompras;
