# Entrega del trabajo final `Sprint 8` 

## Para ejecutar los distintos endpoints

usuario cliente:
  - user: 74701370
  - pass: 1234
 
 usuario empleado:
  - user: 33679828
  - pass: 1234
  
  ## Endpoints:
  
  ## GET:
  
 ### OBTENER DATOS DE UN CLIENTE
  http://127.0.0.1:8000/api/cliente/ ` cliente_dni ` /
    
  ejemplo con cliente o empleado: http://127.0.0.1:8000/api/cuenta/74701370/
  
 ### OBTENER SALDO DE CUENTA DE UN CLIENTE
  http://127.0.0.1:8000/api/cuenta/ ` cliente_dni ` /
  
  ejemplo con cliente o empleado: http://127.0.0.1:8000/api/cliente/74701370/
  
 ###  OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
  http://127.0.0.1:8000/api/prestamos/ ` cliente_dni ` /
  
  ejemplo con cliente o empleado: http://127.0.0.1:8000/api/prestamos/74701370/

 ###  OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
   http://127.0.0.1:8000/api/prestamos_sucursal/ ` sucursal_id ` /
   
   ejemplo con empleado: http://127.0.0.1:8000/api/prestamos_sucursal/20/

 ###  OBTENER TARJETAS ASOCIADAS A UN CLIENTE
http://127.0.0.1:8000/api/tarjetas/ ` cliente_dni ` /
    
ejemplo con cliente o empleado: http://127.0.0.1:8000/api/tarjetas/74701370/

 ### LISTADO DE TODAS LAS SUCURSALES
http://127.0.0.1:8000/api/sucursales/
    
ejemplo publico: http://127.0.0.1:8000/api/sucursales/
 
 ## POST:
 
 ###  GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
http://127.0.0.1:8000/api/add_prestamo/ 

ejemplo con empleado: http://127.0.0.1:8000/api/add_prestamo/
    
body: 
```
      {"loan_payment": "HIPOTECARIO",
        "loan_total": 1000,
        "customer_id": 1 }
```
 ## DELETE:    
 ###  ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
http://127.0.0.1:8000/api/delete_prestamo/ ` prestamo_id ` /

ejemplo con empleado: http://127.0.0.1:8000/api/delete_prestamo/125/

 ## PUT:    
 ###  MODIFICAR DIRECCION DE UN CLIENTE
http://127.0.0.1:8000/api/direcciones/ ` cliente_dni ` /

ejemplo con cliente o empleado: http://127.0.0.1:8000/api/direcciones/74701370/

body: 
```
  {"address_street":"Iowa",
    "address_number":"10",
    "address_city":"Nueva Arabia Saudita",
    "address_province":"Tabasco",
    "address_country":"Mexico"}
```


  
