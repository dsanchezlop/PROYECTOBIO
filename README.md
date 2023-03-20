Per la primera entrega hem fet un petit mockup de funcionament en Flask, encara no està feta la part del Frontend que serà la que tingui el MVC.

Actualment, podeu activar l'entorn fent un cd a la carpeta de Flask, activant l'entorn utilitzant el script env\Scripts\activate i després utilitzant la comanda python app.py

En aquest cas, només està fet el Flask per veure com podria funcionar en un principi.
Coses que es poden fer ara mateix:
-Anar a les rutes disponibles que canvien en funció de si l'usuari ha iniciat sessió o no.
-Inici de sessió.
-Registre.
-Si n'hi ha una ruta desconeguda o sense permisos, redirigeix a home.
-Actualitzar el teu propi usuari.
-Tancament de sessió.

Coses a canviar
-La llibreria de connexió amb la base de dades, passarem de mysql.connector a SQLAlchemy, ja que dóna un millor funcionament per l'aplicació segons les vostres instruccions. Amb aquest canvi podrem desenvolupar l'API per connexió amb el Frontend més eficientment. (Pablo ens ha recomanat aquest tutorial: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

Coses a desenvolupar:
-Les APIs.
-Connexió backend-frontend.
-Revisió de funcionalitats de les connexions client-servidor.
-Mostra, actualització y descàrrega de les dades de la BBDD.
-Mapes D3 de països-fertilitzants, flora-fertilitzant.
-Alineament de seqüències de espècies afectades.