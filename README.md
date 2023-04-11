
Per fer funcionar la aplicació podeu activar l'entorn utilitzant el script 'env\Scripts\activate' un cd a la carpeta de Flask, i després utilitzant la comanda python app.py

Després heu de fer un cd a la carpete de my-sv-map, utilitzar la comanda 'npm install' i a continuació, utilitzar la comanda 'npm run serve'. Només cal donar clic al link i veure l'aplicació en funcionament.

Dintre del Flask estan els requeriments que es necessiten per poder fer-ho funcionar i dos arxius importants:
    -app.py que és l'aplicació principal que mostra les APIs.
    -config.py que és la configuració per accedir a la base de dades

Dintre del my-svg-map tenim:
    -router.js que administra les rutes del frontend
    -App.vue que és l'aplicació principal del Vue
    -Els components, els quals són cada una de les vistes que es poden accedir del Vue.