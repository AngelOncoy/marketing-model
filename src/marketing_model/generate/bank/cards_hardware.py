"""Publishable hardware tasks with their reference proposal content."""

CARDS = [
    dict(
        id="hw01", area="hardware", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="firmware-sensor-pulpa",
        det="Cierre de la calibración del sensor de pulpa para la línea de mango de {cliente}: reconoce 3 rangos de madurez y entrega una lectura cada 2 segundos. En la prueba en planta, 112 de 120 muestras coincidieron con el laboratorio.",
        fuente="Calibración del sensor de pulpa de fruta", valor=5,
        razon="Producto terminado con un resultado medible en planta; se puede contar sin nombrar al cliente.",
        li="""¿Cuándo está lista la pulpa? Ahora lo dice un sensor, no solo el ojo del operario.

En una línea de procesamiento de mango, decidir la madurez a simple vista genera lotes desiguales. Calibramos nuestro sensor de pulpa para reconocer 3 rangos de madurez y entregar una lectura cada 2 segundos.

En la prueba en planta, 112 de 120 muestras coincidieron con el laboratorio.

Diseñamos el dispositivo, el modelo que interpreta el dato y la plataforma donde se decide. ¿Tu línea tiene un punto de control parecido? Cuéntanos tu caso.""",
        fb="Calibramos nuestro sensor de pulpa de fruta: 3 rangos de madurez y una lectura cada 2 segundos. En planta, 112 de 120 muestras coincidieron con el laboratorio. Escríbenos y te contamos cómo aplicarlo en tu línea.",
        ig="""🥭 Madurez medida, no adivinada.
Nuestro sensor de pulpa reconoce 3 rangos de madurez y lee cada 2 segundos. En planta, 112 de 120 muestras coincidieron con el laboratorio.""",
        tt=[("Primer plano de pulpa de mango en la línea", "¿Cómo sabes si la pulpa está en su punto?"),
            ("El sensor leyendo sobre la faja", "Nuestro sensor lo mide cada 2 segundos y reconoce 3 niveles de madurez."),
            ("Comparación con el resultado de laboratorio", "En planta, 112 de 120 muestras coincidieron con el laboratorio.")],
        tit="Madurez medida en tiempo real", bul=[("3 rangos de madurez", "Clasifica la pulpa según su punto de madurez."),
                                                  ("Lectura cada 2 segundos", "Información continua para el operario."),
                                                  ("Validado en planta", "Comparado contra resultados de laboratorio.")],
        dato="112 de 120 muestras coincidieron con el laboratorio", cta="Cuéntanos tu caso",
        tags=["#Agroindustria", "#IoT", "#SensoresInteligentes", "#ControlDeCalidad"],
        vis="Realistic 3D render of a compact industrial sensor over a stainless steel conveyor with mango pulp",
    ),
    dict(
        id="hw02", area="hardware", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="telemetria-flota",
        det="Despliegue del tablero de telemetría para la flota de {cliente}: 24 unidades reportando posición, velocidad y temperatura del motor cada 30 segundos, con alertas por exceso de velocidad.",
        fuente="Tablero de telemetría de flota", valor=5,
        razon="Solución desplegada con alcance concreto; se describe la capacidad sin identificar a la empresa.",
        li="""24 camiones, un solo tablero y alertas antes de que el problema llegue al taller.

Para una empresa de transporte, saber dónde está cada unidad no basta: importa cómo se está manejando y en qué estado va el motor. Desplegamos un tablero de telemetría que recibe posición, velocidad y temperatura del motor cada 30 segundos.

Si una unidad supera el límite de velocidad, el equipo de operaciones recibe la alerta al momento.

Hardware, plataforma y alertas diseñados por nuestro equipo en Trujillo. ¿Gestionas una flota? Conversemos.""",
        fb="Nuevo tablero de telemetría en operación: 24 unidades reportan posición, velocidad y temperatura del motor cada 30 segundos, con alertas por exceso de velocidad. ¿Tienes una flota? Escríbenos.",
        ig="""🚚 Tu flota, en tiempo real.
24 unidades reportan posición, velocidad y temperatura del motor cada 30 segundos. Si alguien se pasa del límite, la alerta llega al instante.""",
        tt=[("Camión saliendo de la base al amanecer", "¿Sabes qué pasa con tu flota cuando sale de la base?"),
            ("Pantalla del tablero con el mapa y las unidades", "Cada 30 segundos recibimos posición, velocidad y temperatura del motor."),
            ("Notificación de alerta en el celular", "Y si alguien se pasa del límite, la alerta llega al momento.")],
        tit="Tu flota en un tablero", bul=[("Posición en vivo", "Ubicación de cada unidad cada 30 segundos."),
                                           ("Temperatura del motor", "Detecta sobrecalentamientos a tiempo."),
                                           ("Alertas de velocidad", "Aviso inmediato al equipo de operaciones.")],
        dato="24 unidades reportando cada 30 segundos", cta="Conversemos",
        tags=["#Telemetría", "#GestiónDeFlotas", "#Logística", "#IoT"],
        vis="Dashboard mockup on a laptop showing a map with truck markers, in a logistics control room",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="hw03", area="hardware", sector="minería", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Visita técnica a la unidad minera de {cliente} para instalar 6 estaciones de monitoreo de polvo; el cliente autorizó difundir el trabajo sin mencionar su nombre. Se dejaron transmitiendo a 3800 m s. n. m.",
        fuente="Instalación de estaciones de monitoreo de polvo", valor=4,
        razon="Trabajo de campo terminado con autorización para difundirlo sin nombre; muestra capacidad en territorio.",
        li="""A 3800 metros de altura, el dato también tiene que llegar.

Instalamos 6 estaciones de monitoreo de polvo en una unidad minera. El reto no fue solo medir: fue lograr que cada estación transmita de forma estable en altura, con frío y con viento.

Hoy las 6 estaciones ya envían sus lecturas a la plataforma, donde el equipo de seguridad y medio ambiente puede revisarlas.

Así trabajamos: piloto en campo primero, escala después. ¿Tienes un reto de monitoreo en operación? Cuéntanos.""",
        fb="Instalamos 6 estaciones de monitoreo de polvo a 3800 m s. n. m. y ya transmiten sus lecturas a la plataforma. Si tu operación necesita monitoreo en campo, escríbenos.",
        ig="""⛰️ Monitoreo a 3800 m s. n. m.
Instalamos 6 estaciones de monitoreo de polvo en una unidad minera. Ya transmiten sus lecturas a la plataforma.""",
        tt=[("Paisaje de altura con la estación instalada", "Así se ve monitorear polvo a 3800 metros."),
            ("Técnico ajustando la estación (sin rostro)", "Instalamos 6 estaciones que miden y transmiten desde el campo."),
            ("Lecturas llegando a la plataforma", "Y los datos llegan directo a la plataforma del equipo de seguridad.")],
        tit="Monitoreo a 3800 metros", bul=[("6 estaciones instaladas", "Monitoreo continuo de polvo en la operación."),
                                                ("Transmisión en altura", "Diseñadas para frío y viento."),
                                                ("Datos en la plataforma", "Disponibles para seguridad y medio ambiente.")],
        dato="6 estaciones transmitiendo a 3800 m s. n. m.", cta="Cuéntanos tu reto",
        tags=["#Minería", "#MonitoreoAmbiental", "#IoT", "#Seguridad"],
        vis="Rugged environmental monitoring station on a tripod in a high-altitude Andean mining landscape",
        adj="campo",
    ),
    dict(
        id="hw04", area="hardware", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="contador-pares",
        det="Entrega del contador de pares para la línea de aparado de {cliente}: lector óptico en la salida de la faja y pantalla en el puesto del supervisor. En 2 turnos de prueba contó 1460 pares con 4 diferencias frente al conteo manual.",
        fuente="Contador de pares para calzado", valor=4,
        razon="Equipo entregado con resultado de prueba verificable; útil para el sector calzado.",
        li="""¿Cuántos pares salieron hoy de la línea? Ya no hay que esperar al cierre del turno para saberlo.

En una fábrica de calzado, el conteo manual consume tiempo y se presta a errores. Entregamos un contador de pares con lector óptico a la salida de la faja y una pantalla en el puesto del supervisor.

En 2 turnos de prueba contó 1460 pares, con solo 4 diferencias frente al conteo manual.

Tecnología hecha en Trujillo para la industria del calzado de Trujillo. ¿Quieres verlo funcionando? Escríbenos.""",
        fb="Nuestro contador de pares ya está en una línea de aparado: en 2 turnos de prueba contó 1460 pares con 4 diferencias frente al conteo manual. ¿Quieres llevarlo a tu taller? Escríbenos.",
        ig="""👞 Cada par cuenta.
Contador óptico a la salida de la faja: 1460 pares en 2 turnos de prueba y solo 4 diferencias frente al conteo manual.""",
        tt=[("Pares de calzado avanzando en la faja", "¿Todavía cuentas los pares a mano?"),
            ("El lector óptico detectando cada par", "Este lector los cuenta al salir de la faja."),
            ("Pantalla del supervisor con el total", "En 2 turnos de prueba: 1460 pares y solo 4 diferencias.")],
        tit="Cada par, contado al instante", bul=[("Lector óptico", "Detecta cada par al final de la faja."),
                                                  ("Pantalla al supervisor", "El total del turno, en vivo."),
                                                  ("Menos conteo manual", "Más tiempo para producir.")],
        dato="1460 pares contados con 4 diferencias", cta="Escríbenos",
        tags=["#Calzado", "#Industria40", "#Automatización", "#HechoEnTrujillo"],
        vis="Shoe production conveyor belt with an optical sensor mounted at the end, warm factory lighting",
    ),
    dict(
        id="hw05", area="hardware", sector="agroindustria", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Actualización del catálogo de hardware: se fotografiaron y documentaron 5 equipos listos para pilotos (sensor de pulpa, estación de clima, tracker GPS, contador óptico y gateway LoRa)",
        fuente="Catálogo de equipos para pilotos", valor=4,
        razon="Catálogo de productos propios terminados; contenido comercial sin riesgos.",
        li="""5 equipos listos para empezar un piloto en campo esta misma temporada.

Muchas empresas quieren medir antes de invertir en grande. Por eso ordenamos nuestro catálogo de hardware con los equipos que ya probamos en operación:

- Sensor de pulpa de fruta
- Estación de clima
- Tracker GPS
- Contador óptico
- Gateway LoRa

Cada uno se integra con nuestra plataforma, así que el dato llega listo para decidir. ¿Cuál necesitas para tu piloto? Escríbenos.""",
        fb="Nuestro catálogo de hardware para pilotos ya está listo: sensor de pulpa, estación de clima, tracker GPS, contador óptico y gateway LoRa. ¿Cuál necesitas? Escríbenos.",
        ig="""📦 5 equipos, un mismo objetivo: medir antes de escalar.
Sensor de pulpa, estación de clima, tracker GPS, contador óptico y gateway LoRa, todos conectados a nuestra plataforma.""",
        tt=[("Los 5 equipos sobre una mesa blanca", "Si quieres medir antes de invertir en grande, empieza por aquí."),
            ("Toma rápida de cada equipo", "Sensor de pulpa, estación de clima, tracker, contador óptico y gateway."),
            ("Pantalla de la plataforma recibiendo datos", "Todos envían su dato a la misma plataforma.")],
        tit="Equipos listos para tu piloto", bul=[("Sensor de pulpa", "Madurez de fruta en la línea."),
                                                  ("Estación de clima", "Datos de campo para decidir riego y cosecha."),
                                                  ("Tracker y gateway", "Ubicación y conectividad en campo.")],
        dato=None, cta="Elige tu equipo",
        tags=["#IoT", "#Agroindustria", "#HardwareAMedida", "#PilotoEnCampo"],
        vis="Clean product lineup of five small industrial IoT devices on a white studio surface, soft shadows",
        comp="grilla",
    ),
    dict(
        id="hw06", area="hardware", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="estacion-clima",
        det="Estación de clima instalada en el fundo de {cliente}: mide temperatura, humedad, radiación y lluvia y envía datos cada 10 minutos por LoRa a 2 km del gateway. Funcionó 7 días sin interrupciones.",
        fuente="Estación de clima en un fundo", valor=4,
        razon="Equipo terminado y probado en campo; resultado concreto sin datos sensibles.",
        li="""¿Riegas por calendario o por lo que realmente pasa en tu campo?

Instalamos una estación de clima en un fundo agrícola. Mide temperatura, humedad, radiación y lluvia, y envía los datos cada 10 minutos por LoRa, incluso a 2 km del gateway.

Desde la instalación lleva 7 días funcionando sin interrupciones, con datos listos para planificar riego y labores.

Medir primero, decidir después. Si quieres datos de clima en tu fundo, conversemos.""",
        fb="Nueva estación de clima en campo: temperatura, humedad, radiación y lluvia cada 10 minutos, a 2 km del gateway y 7 días sin interrupciones. Escríbenos para llevarla a tu fundo.",
        ig="""🌦️ El clima de tu fundo, cada 10 minutos.
Temperatura, humedad, radiación y lluvia enviadas por LoRa a 2 km del gateway. 7 días funcionando sin interrupciones.""",
        tt=[("Estación de clima entre cultivos al amanecer", "¿Riegas por calendario o por datos?"),
            ("Sensores de la estación en detalle", "Esta estación mide temperatura, humedad, radiación y lluvia."),
            ("Gráfico de datos en el celular", "Y envía todo cada 10 minutos, aunque esté a 2 km del gateway.")],
        tit="El clima de tu fundo, medido", bul=[("Cuatro variables clave", "Temperatura, humedad, radiación y lluvia."),
                                                 ("Datos cada 10 minutos", "Información fresca para decidir."),
                                                 ("Alcance LoRa", "Hasta 2 km del gateway.")],
        dato="7 días sin interrupciones", cta="Conversemos",
        tags=["#AgriculturaDePrecisión", "#Agroindustria", "#IoT", "#LoRa"],
        vis="Compact weather station with solar panel standing in a green crop field at sunrise",
    ),
    dict(
        id="hw07", area="hardware", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller práctico 'Tu primer prototipo IoT' para estudiantes: sábado 28 de noviembre, de 9:00 a 13:00, en la sede de CorAll en Trujillo; cupo de 20 personas e inscripción por formulario",
        fuente="Taller práctico de prototipos IoT", valor=4,
        razon="Evento propio confirmado con fecha, hora y lugar; ideal para convocatoria.",
        li="""¿Nunca has armado un dispositivo IoT? Este sábado puede ser el primero.

Te invitamos al taller práctico "Tu primer prototipo IoT", pensado para estudiantes que quieren pasar de la teoría a un circuito que funciona.

Sábado 28 de noviembre
De 9:00 a 13:00
Sede de CorAll en Trujillo
Cupo: 20 personas

Trabajarás con sensores reales y verás cómo el dato llega a una plataforma. Inscríbete con el formulario del enlace.""",
        fb="Taller práctico 'Tu primer prototipo IoT': sábado 28 de noviembre, de 9:00 a 13:00, en nuestra sede de Trujillo. Solo 20 cupos. Inscríbete en el enlace.",
        ig="""🔧 Arma tu primer prototipo IoT.
Sábado 28 de noviembre, 9:00 a 13:00, sede de CorAll en Trujillo. Solo 20 cupos. Inscripción en el enlace de la biografía.""",
        tt=[("Mesa con placas, sensores y cables", "¿Quieres armar tu primer dispositivo IoT?"),
            ("Manos conectando un sensor a una placa", "En nuestro taller trabajarás con sensores reales."),
            ("Pantalla con los datos del prototipo", "Sábado 28 de noviembre, de 9:00 a 13:00. Solo 20 cupos.")],
        tit="Tu primer prototipo IoT", bul=[("Sábado 28 de noviembre", "Un taller práctico de medio día."),
                                            ("9:00 a 13:00", "Con sensores y placas reales."),
                                            ("Solo 20 cupos", "Inscripción por formulario.")],
        dato="Sábado 28 de noviembre, 9:00 a 13:00", cta="Inscríbete",
        tags=["#TallerIoT", "#Estudiantes", "#Educación", "#Trujillo"],
        vis="Workbench with microcontroller boards, sensors and jumper cables arranged neatly, top view",
    ),
    dict(
        id="hw08", area="hardware", sector="logística y transporte", tipo="interno", pilar="educativo",
        sec="matriz", mod="tracker-gps",
        det="Pruebas de autonomía del tracker GPS terminadas: con reporte cada 5 minutos la batería duró 21 días; con reporte cada minuto, 6 días. Se documentó la recomendación de configuración por tipo de uso.",
        fuente="Pruebas de autonomía del tracker GPS", valor=4,
        razon="Resultado de pruebas propio que se convierte en una buena práctica útil para el público.",
        li="""¿Cada cuánto debe reportar un GPS? Depende de qué tanto quieras que dure la batería.

Terminamos las pruebas de autonomía de nuestro tracker y el resultado es claro:

- Reporte cada 5 minutos: 21 días de batería.
- Reporte cada minuto: 6 días.

No siempre más datos es mejor. Para activos que se mueven poco, un reporte más espaciado da semanas de autonomía. Para unidades en ruta, conviene más frecuencia y carga periódica.

¿Quieres saber cuál configuración te conviene? Escríbenos.""",
        fb="¿Cada cuánto debe reportar un GPS? En nuestras pruebas: cada 5 minutos, 21 días de batería; cada minuto, 6 días. Te ayudamos a elegir la configuración para tu operación.",
        ig="""🔋 Más datos no siempre es mejor.
Nuestro tracker GPS: reporte cada 5 minutos = 21 días de batería. Cada minuto = 6 días. Elige según tu operación.""",
        tt=[("El tracker sobre una caja de carga", "¿Cuánto dura la batería de un GPS?"),
            ("Gráfico de batería bajando", "Si reporta cada minuto, 6 días."),
            ("Mismo gráfico con pendiente suave", "Si reporta cada 5 minutos, 21 días. Elige según tu operación.")],
        tit="¿Cada cuánto debe reportar?", bul=[("Cada 5 minutos", "21 días de batería."),
                                                ("Cada minuto", "6 días de batería."),
                                                ("Según tu operación", "Activos quietos o unidades en ruta.")],
        dato="21 días vs. 6 días de batería", cta="Escríbenos",
        tags=["#GPS", "#Logística", "#IoT", "#BuenasPrácticas"],
        vis="Small rugged GPS tracker device on a shipping crate, with a stylized battery icon glow",
        comp="antes / después",
    ),
    dict(
        id="hw09", area="hardware", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="matriz", mod="gateway-lora",
        det="Se completó la red LoRa del fundo de {cliente}: 3 gateways cubren 180 hectáreas y ya conectan 40 sensores de humedad de suelo.",
        fuente="Red LoRa para sensores de suelo", valor=5,
        razon="Hito de proyecto terminado con cifras de alcance; se cuenta sin nombrar al cliente.",
        li="""180 hectáreas conectadas con solo 3 gateways.

En el campo, el reto no es instalar sensores: es que todos lleguen a transmitir. Completamos una red LoRa que cubre 180 hectáreas de un fundo y ya conecta 40 sensores de humedad de suelo.

Con esta base, el equipo agrícola puede decidir el riego por sector según lo que dice el suelo y no por intuición.

Diseñamos la red, instalamos los equipos y entregamos la plataforma. ¿Tu fundo necesita conectividad en campo? Conversemos.""",
        fb="Hito cumplido: 3 gateways LoRa cubren 180 hectáreas y conectan 40 sensores de humedad de suelo. Riego por sector según datos reales. ¿Hablamos de tu fundo?",
        ig="""📡 180 hectáreas conectadas.
Con 3 gateways LoRa ya transmiten 40 sensores de humedad de suelo. El riego ahora se decide con datos.""",
        tt=[("Vista aérea simulada de un fundo", "¿Cómo conectas sensores en 180 hectáreas?"),
            ("Gateway en un poste con panel solar", "Con 3 gateways LoRa como este."),
            ("Mapa con 40 puntos encendidos", "Hoy transmiten 40 sensores de humedad de suelo.")],
        tit="180 hectáreas conectadas", bul=[("3 gateways LoRa", "Cobertura para todo el fundo."),
                                             ("40 sensores de suelo", "Humedad medida por sector."),
                                             ("Riego con datos", "Decisiones basadas en el suelo.")],
        dato="3 gateways, 180 hectáreas, 40 sensores", cta="Conversemos",
        tags=["#LoRa", "#AgriculturaDePrecisión", "#Agroindustria", "#IoT"],
        vis="Aerial view of farmland divided in sectors with glowing connection lines between small devices",
    ),
    dict(
        id="hw10", area="hardware", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Celebración interna por el primer año del laboratorio de hardware: el equipo repasó los 12 prototipos construidos en el año y se tomó una foto grupal (todos dieron su consentimiento para publicarla)",
        fuente="Primer año del laboratorio de hardware", valor=4,
        razon="Contenido de cultura con consentimiento del equipo; muestra trayectoria sin datos sensibles.",
        li="""Un año, 12 prototipos y muchas horas de soldador.

Hoy celebramos el primer aniversario de nuestro laboratorio de hardware. En estos meses construimos 12 prototipos: algunos ya trabajan en campo y otros nos enseñaron lo que no debíamos repetir.

Lo que más valoramos es al equipo que convierte una idea en un dispositivo que funciona fuera del laboratorio.

Gracias a todos los que hicieron posible este primer año. Vamos por más.""",
        fb="Nuestro laboratorio de hardware cumple su primer año: 12 prototipos construidos y un equipo que convierte ideas en dispositivos que funcionan en campo. ¡Gracias, equipo!",
        ig="""🎉 Un año de laboratorio.
12 prototipos, muchas pruebas y un equipo que convierte ideas en dispositivos reales. ¡Gracias por este primer año!""",
        tt=[("Mesa del laboratorio con herramientas", "Hace un año este laboratorio empezó con una mesa y un soldador."),
            ("Toma rápida de varios prototipos", "Hoy suma 12 prototipos construidos."),
            ("Foto grupal del equipo con overlay rojo", "Y un equipo que los hace funcionar en campo. ¡Feliz primer año!")],
        tit="Un año de laboratorio", bul=[("12 prototipos", "Construidos en el primer año."),
                                          ("Pruebas en campo", "Ideas que salieron del laboratorio."),
                                          ("Un gran equipo", "Gracias a cada integrante.")],
        dato="12 prototipos en el primer año", cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#Hardware", "#Aniversario", "#EquipoCorAll"],
        vis="Electronics lab workbench with soldering station, prototypes and warm celebratory light",
        adj="equipo",
    ),
    dict(
        id="hw11", area="hardware", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="matriz", mod="telemetria-frio",
        det="Instalación de sensores de temperatura en 10 contenedores refrigerados de {cliente}; registran cada 5 minutos y alertan si la carga sale del rango de 2 a 8 °C.",
        fuente="Monitoreo de temperatura en contenedores refrigerados", valor=4,
        razon="Servicio instalado y funcionando; se presenta como capacidad sin nombrar al cliente.",
        li="""Una carga refrigerada no avisa cuando se calienta. Ahora sí.

Instalamos sensores de temperatura en 10 contenedores refrigerados. Registran cada 5 minutos y envían una alerta si la carga sale del rango de 2 a 8 °C.

Así el equipo puede reaccionar en ruta y no al momento de la entrega, cuando ya es tarde.

Cadena de frío con datos, de principio a fin. ¿Transportas productos sensibles a la temperatura? Escríbenos.""",
        fb="Cadena de frío monitoreada: sensores en 10 contenedores refrigerados que registran cada 5 minutos y alertan si la carga sale de 2 a 8 °C. Escríbenos para conocer más.",
        ig="""❄️ La cadena de frío, vigilada.
Sensores en 10 contenedores registran cada 5 minutos y alertan si la carga sale del rango de 2 a 8 °C.""",
        tt=[("Contenedor refrigerado en carretera", "¿Cómo sabes si tu carga se mantiene fría en ruta?"),
            ("Sensor dentro del contenedor", "Estos sensores registran la temperatura cada 5 minutos."),
            ("Alerta en el celular", "Si sale del rango de 2 a 8 °C, avisan al momento.")],
        tit="Cadena de frío con datos", bul=[("Registro cada 5 minutos", "Historial completo del viaje."),
                                             ("Rango configurable", "De 2 a 8 °C, según la carga."),
                                             ("Alertas en ruta", "Reaccionar antes de la entrega.")],
        dato="10 contenedores monitoreados", cta="Escríbenos",
        tags=["#CadenaDeFrío", "#Logística", "#IoT", "#Telemetría"],
        vis="Refrigerated shipping container on a truck at dusk with a small sensor glowing on the door",
    ),
    dict(
        id="hw12", area="hardware", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="matriz", mod="docs-hardware",
        det="Se redactó la guía interna de instalación de sensores en campo tras las últimas visitas: protección IP65, altura de montaje, orientación del panel solar y prueba de señal antes de retirarse.",
        fuente="Guía de instalación de sensores en campo", valor=3,
        razon="Lección práctica convertible en consejo general, sin datos internos ni de clientes.",
        li="""Un sensor bien elegido puede fallar por una mala instalación.

Después de varias visitas a campo, ordenamos lo que siempre revisamos antes de dar por terminada una instalación:

1. Protección IP65 para polvo y agua.
2. Altura de montaje según lo que se mide.
3. Panel solar orientado para recibir sol todo el día.
4. Prueba de señal antes de retirarse.

Parecen detalles, pero marcan la diferencia entre un dato continuo y una visita extra. ¿Qué otra práctica agregarías?""",
        fb="4 claves para instalar sensores en campo: protección IP65, altura correcta, panel solar bien orientado y prueba de señal antes de irte. ¿Qué agregarías?",
        ig="""🛠️ 4 claves para instalar sensores en campo.
IP65, altura correcta, panel solar orientado y prueba de señal antes de retirarte. Detalles que evitan visitas extra.""",
        tt=[("Técnico frente a un poste en campo (sin rostro)", "Un buen sensor puede fallar por una mala instalación."),
            ("Detalle de la caja IP65 y el panel solar", "Revisa protección IP65, altura y orientación del panel."),
            ("Celular mostrando señal correcta", "Y nunca te vayas sin probar la señal.")],
        tit="Instala sensores sin sorpresas", bul=[("Protección IP65", "Contra polvo y agua."),
                                                   ("Altura y orientación", "Según la variable y el sol."),
                                                   ("Prueba de señal", "Antes de retirarte del sitio.")],
        dato=None, cta="Cuéntanos tu experiencia",
        tags=["#BuenasPrácticas", "#IoT", "#Agroindustria", "#SensoresEnCampo"],
        vis="3D illustration of a sensor mounted on a pole in a field with a small solar panel and signal waves",
    ),
    dict(
        id="hw13", area="hardware", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="detector-gases",
        det="Entrega del detector portátil de gases para {cliente}: mide CO y H2S, vibra y suena al superar el umbral configurado y guarda el historial del turno. Se entregaron 15 unidades.",
        fuente="Detector portátil de gases", valor=4,
        razon="Producto entregado con funciones claras; aporta valor de seguridad sin datos del cliente.",
        li="""En interior mina, una alerta a tiempo es la diferencia.

Entregamos 15 detectores portátiles de gases para una operación minera. Cada equipo mide CO y H2S, vibra y suena al superar el umbral configurado y guarda el historial de todo el turno.

Al terminar la jornada, el supervisor revisa el registro y sabe en qué momentos hubo exposición.

Hardware diseñado para condiciones reales de operación. ¿Necesitas equipos de seguridad a medida? Conversemos.""",
        fb="Entregamos 15 detectores portátiles de gases: miden CO y H2S, alertan con vibración y sonido y guardan el historial del turno. Conversemos sobre tu operación.",
        ig="""⚠️ Alertas que se sienten y se escuchan.
15 detectores portátiles que miden CO y H2S, vibran y suenan al superar el umbral y guardan el historial del turno.""",
        tt=[("Detector colgado en el chaleco de un trabajador (sin rostro)", "En interior mina, una alerta a tiempo lo cambia todo."),
            ("Pantalla del detector marcando el umbral", "Este equipo mide CO y H2S y avisa con vibración y sonido."),
            ("Supervisor revisando el historial en una tablet", "Y guarda el historial de todo el turno.")],
        tit="Alertas de gases a tiempo", bul=[("Mide CO y H2S", "Los gases más críticos en interior mina."),
                                              ("Vibra y suena", "Alerta imposible de ignorar."),
                                              ("Historial del turno", "Revisión al cerrar la jornada.")],
        dato="15 detectores entregados", cta="Conversemos",
        tags=["#Minería", "#SeguridadIndustrial", "#Hardware", "#IoT"],
        vis="Portable gas detector clipped to a high-visibility vest in a dim mine tunnel, dramatic lighting",
    ),
    dict(
        id="hw14", area="hardware", sector="cuero y calzado", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Charla interna sobre por qué medimos humedad y temperatura en el almacén de cuero: el cuero mal almacenado se mancha y se deforma; se acordó compartir recomendaciones generales con el sector",
        fuente="Recomendaciones de almacenamiento de cuero", valor=3,
        razon="Contenido educativo general para el sector; no expone datos de clientes ni internos.",
        li="""El cuero también sufre en el almacén.

Cuando el ambiente no se controla, el cuero puede mancharse o deformarse antes de llegar a la línea. Algunas recomendaciones generales:

- Mide humedad y temperatura, no las supongas.
- Evita la luz solar directa sobre los rollos.
- Deja espacio para que el aire circule.

Medir el ambiente es simple y evita pérdidas que solo se notan al cortar. ¿Cómo controlas tu almacén hoy?""",
        fb="El cuero mal almacenado se mancha y se deforma. Mide humedad y temperatura, evita la luz solar directa y deja circular el aire. ¿Cómo controlas tu almacén?",
        ig="""🧳 Cuida el cuero antes de cortarlo.
Mide humedad y temperatura, evita la luz solar directa y deja circular el aire en el almacén.""",
        tt=[("Rollos de cuero apilados en un almacén", "¿Sabías que el cuero puede dañarse antes de llegar a la línea?"),
            ("Sensor de humedad en la pared", "Mide la humedad y la temperatura, no las supongas."),
            ("Rollos bien separados", "Y deja espacio para que circule el aire.")],
        tit="Cuida tu cuero en el almacén", bul=[("Mide el ambiente", "Humedad y temperatura reales."),
                                                 ("Sin sol directo", "Protege los rollos de la luz."),
                                                 ("Aire que circule", "Espacio entre los rollos.")],
        dato=None, cta="Cuéntanos",
        tags=["#Cuero", "#Calzado", "#BuenasPrácticas", "#IoT"],
        vis="Warehouse shelves with neatly stacked leather rolls and a small wall-mounted humidity sensor",
    ),
    dict(
        id="hw15", area="hardware", sector="logística y transporte", tipo="cliente", pilar="hito",
        sec="matriz", mod="telemetria-flota",
        det="La plataforma de telemetría de {cliente} alcanzó 50 unidades conectadas; desde el inicio del piloto con 8 unidades se mantuvieron los reportes en línea.",
        fuente="Telemetría: de piloto a 50 unidades", valor=5,
        razon="Hito de crecimiento real que respalda el enfoque de piloto antes de escalar.",
        li="""Empezamos con 8 unidades. Hoy son 50.

Así trabajamos: primero un piloto en campo para probar que el dato es confiable y útil; después, escalar.

Una empresa de transporte inició con 8 unidades conectadas a nuestra plataforma de telemetría. Con los resultados del piloto, hoy ya son 50 unidades reportando en línea.

Crecer con datos da confianza. ¿Quieres empezar tu propio piloto? Conversemos.""",
        fb="De 8 a 50 unidades conectadas: así creció un piloto de telemetría que empezó pequeño y hoy opera a escala. ¿Empezamos el tuyo?",
        ig="""📈 De 8 a 50 unidades.
Un piloto de telemetría que empezó pequeño y hoy opera a escala. Primero probar, después crecer.""",
        tt=[("Un camión solo en el patio", "Empezamos con 8 unidades."),
            ("Muchos camiones en fila", "Hoy son 50 conectadas a la plataforma."),
            ("Tablero con todas las unidades", "Primero un piloto, después escalar. Así trabajamos.")],
        tit="De 8 a 50 unidades", bul=[("Piloto de 8 unidades", "Para validar el dato en campo."),
                                       ("Hoy 50 unidades", "Reportando en línea."),
                                       ("Escala con confianza", "Decisiones basadas en resultados.")],
        dato="De 8 a 50 unidades conectadas", cta="Empieza tu piloto",
        tags=["#Telemetría", "#Logística", "#PilotoEnCampo", "#GestiónDeFlotas"],
        vis="Line of heavy trucks in a depot at sunset seen from above, subtle data connection lines",
        comp="línea de tiempo",
    ),
    dict(
        id="hw16", area="hardware", sector="agroindustria", tipo="interno", pilar="producto",
        sec="matriz", mod="balanza-iot",
        det="Terminada la balanza conectada para centros de acopio: pesa jabas hasta 60 kg, envía el peso por wifi a la plataforma y asocia cada pesada al productor con un código QR. Probada con 200 pesadas en laboratorio.",
        fuente="Balanza conectada para acopio", valor=4,
        razon="Producto propio terminado y probado; útil para el sector agro.",
        li="""En el acopio, cada kilo cuenta y cada pesada debería quedar registrada.

Terminamos nuestra balanza conectada para centros de acopio. Pesa jabas de hasta 60 kg, envía el peso por wifi a la plataforma y asocia cada pesada al productor con un código QR.

Ya la probamos con 200 pesadas en laboratorio, lista para su primer piloto en campo.

Menos cuadernos, menos errores de digitación y pagos más claros para cada productor. ¿Te interesa probarla? Escríbenos.""",
        fb="Nuestra balanza conectada pesa jabas de hasta 60 kg, envía el peso a la plataforma y lo asocia al productor con un QR. Probada con 200 pesadas. ¿La probamos en tu acopio?",
        ig="""⚖️ Cada pesada, registrada.
Balanza conectada para acopio: jabas de hasta 60 kg, peso enviado a la plataforma y QR por productor. 200 pesadas de prueba.""",
        tt=[("Jabas de fruta en un centro de acopio", "¿Todavía anotas las pesadas en un cuaderno?"),
            ("La balanza leyendo un QR", "Esta balanza asocia cada pesada al productor con un QR."),
            ("La pesada apareciendo en la plataforma", "Y envía el peso directo a la plataforma.")],
        tit="Cada pesada, registrada", bul=[("Hasta 60 kg", "Para jabas de campo."),
                                            ("Código QR", "Cada pesada asociada al productor."),
                                            ("Directo a la plataforma", "Sin digitar a mano.")],
        dato="200 pesadas de prueba", cta="Pruébala",
        tags=["#Agroindustria", "#IoT", "#Trazabilidad", "#Acopio"],
        vis="Industrial platform scale with a crate of fruit and a small QR reader, clean agricultural warehouse",
    ),
    dict(
        id="hw17", area="hardware", sector="educación", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Entrega e instalación de 4 kits de robótica educativa en el laboratorio de un instituto técnico, con autorización para difundir sin nombre; se capacitó a 3 docentes",
        fuente="Kits de robótica educativa en un instituto", valor=4,
        razon="Servicio terminado con autorización para difundirlo sin nombre.",
        li="""Aprender robótica es más fácil cuando el kit está en el aula y no en el catálogo.

Entregamos e instalamos 4 kits de robótica educativa en el laboratorio de un instituto técnico. También capacitamos a 3 docentes para que puedan usarlos desde la próxima clase.

Nuestro objetivo es que la tecnología llegue al aula lista para usarse, con acompañamiento y no solo con una caja.

¿Tu institución quiere implementar un laboratorio así? Conversemos.""",
        fb="Entregamos 4 kits de robótica educativa en un instituto técnico y capacitamos a 3 docentes para usarlos desde la próxima clase. ¿Llevamos uno a tu institución?",
        ig="""🤖 Robótica en el aula.
Instalamos 4 kits de robótica educativa en un instituto técnico y capacitamos a 3 docentes para usarlos desde ya.""",
        tt=[("Laboratorio con mesas y kits nuevos", "Así se ve un laboratorio listo para aprender robótica."),
            ("Manos armando un robot pequeño", "Instalamos 4 kits de robótica educativa."),
            ("Docentes revisando una guía (sin rostro)", "Y capacitamos a 3 docentes para usarlos desde la próxima clase.")],
        tit="Robótica lista para el aula", bul=[("4 kits instalados", "En el laboratorio del instituto."),
                                                ("3 docentes capacitados", "Listos para la próxima clase."),
                                                ("Acompañamiento", "No solo entregamos una caja.")],
        dato="4 kits y 3 docentes capacitados", cta="Conversemos",
        tags=["#RobóticaEducativa", "#Educación", "#STEM", "#Tecnología"],
        vis="Classroom lab table with small educational robots and microcontroller kits, bright natural light",
        adj="campo",
    ),
    dict(
        id="hw18", area="hardware", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="matriz", mod="lab-pruebas",
        det="Comparación de autonomía de 3 tipos de batería para sensores de campo: litio recargable con panel solar, pilas alcalinas y litio no recargable. Se documentó cuándo conviene cada una.",
        fuente="Comparación de baterías para sensores", valor=3,
        razon="Aprendizaje técnico general, convertible en consejo útil sin datos internos.",
        li="""¿Qué batería conviene para un sensor en campo? Depende de dónde lo instales.

Comparamos 3 opciones para nuestros sensores:

- Litio recargable con panel solar: ideal si hay sol y quieres olvidarte del cambio.
- Pilas alcalinas: económicas, pero piden cambios frecuentes.
- Litio no recargable: buena opción en zonas con poca luz y difícil acceso.

Elegir bien la energía reduce visitas y mantenimiento. ¿Qué usas tú en campo?""",
        fb="¿Panel solar, pilas alcalinas o litio no recargable? Comparamos 3 opciones de energía para sensores de campo y cada una tiene su lugar. Te ayudamos a elegir.",
        ig="""🔋 Elige bien la energía de tu sensor.
Panel solar si hay sol, alcalinas si buscas costo bajo y litio no recargable para zonas de difícil acceso.""",
        tt=[("Tres baterías sobre una mesa", "¿Qué batería le pones a un sensor en campo?"),
            ("Sensor con panel solar al sol", "Si hay sol, litio recargable con panel solar."),
            ("Sensor en una zona sombreada", "Si hay poca luz y difícil acceso, litio no recargable.")],
        tit="¿Qué batería necesita tu sensor?", bul=[("Panel solar", "Para zonas con buen sol."),
                                                      ("Alcalinas", "Bajo costo, más cambios."),
                                                      ("Litio no recargable", "Difícil acceso o poca luz.")],
        dato=None, cta="Escríbenos",
        tags=["#IoT", "#BuenasPrácticas", "#EnergíaSolar", "#SensoresEnCampo"],
        vis="3D illustration of three battery types next to a small field sensor with a solar panel",
    ),
    dict(
        id="hw19", area="hardware", sector="minería", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada nuestra participación con stand en la feria regional de proveedores mineros: 4 y 5 de diciembre, centro de convenciones de Trujillo, stand 18; se mostrarán el detector de gases y el tracker GPS",
        fuente="Participación en feria de proveedores mineros", valor=4,
        razon="Evento confirmado con fecha y lugar; contenido de convocatoria sin datos sensibles.",
        li="""Te esperamos en el stand 18.

Participaremos en la feria regional de proveedores mineros con nuestras soluciones de hardware para operación:

📅 4 y 5 de diciembre
📍 Centro de convenciones de Trujillo, stand 18

Podrás ver en funcionamiento nuestro detector portátil de gases y el tracker GPS, y conversar con el equipo que los diseñó.

¿Vas a la feria? Pasa por el stand y cuéntanos tu reto.""",
        fb="Estaremos en la feria regional de proveedores mineros, 4 y 5 de diciembre, en el centro de convenciones de Trujillo, stand 18. Ven a ver el detector de gases y el tracker GPS.",
        ig="""📍 Stand 18, te esperamos.
Feria regional de proveedores mineros, 4 y 5 de diciembre, centro de convenciones de Trujillo. Ven a ver nuestro hardware en acción.""",
        tt=[("Pasillo de feria con stands", "¿Vas a la feria de proveedores mineros?"),
            ("Detector de gases y tracker sobre un mostrador", "Llevaremos nuestro detector de gases y el tracker GPS."),
            ("Logo de marca en el stand vacío", "4 y 5 de diciembre, stand 18. Te esperamos.")],
        tit="Visítanos en el stand 18", bul=[("Diciembre, stand 18", "4 y 5 de diciembre, feria de proveedores mineros."),
                                             ("Centro de convenciones", "Trujillo."),
                                             ("Hardware en vivo", "Detector de gases y tracker.")],
        dato="4 y 5 de diciembre, stand 18", cta="Visítanos",
        tags=["#Minería", "#FeriaMinera", "#Hardware", "#Trujillo"],
        vis="Modern trade fair booth with red and black panels and two devices on a display counter, no people",
    ),
    dict(
        id="hw20", area="hardware", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Mantenimiento preventivo de 25 sensores de humedad de suelo en un fundo de arándanos, con autorización del cliente para publicar sin nombre; se limpiaron, se revisó la batería y se verificó la señal de todos",
        fuente="Mantenimiento preventivo de sensores en campo", valor=3,
        razon="Servicio terminado con autorización; muestra el acompañamiento después de la instalación.",
        li="""Instalar es el inicio. Mantener es lo que asegura el dato.

Esta semana hicimos el mantenimiento preventivo de 25 sensores de humedad de suelo en un fundo de arándanos: limpieza, revisión de batería y verificación de señal en cada uno.

Un sensor sucio o sin batería deja de informar justo cuando más se necesita. Por eso acompañamos cada instalación con visitas programadas.

¿Tus equipos de campo tienen un plan de mantenimiento? Conversemos.""",
        fb="Mantenimiento preventivo de 25 sensores de humedad de suelo en un fundo de arándanos: limpieza, batería y señal revisadas. El dato se cuida en campo.",
        ig="""🫐 El dato también se mantiene.
Revisamos 25 sensores de humedad de suelo en un fundo de arándanos: limpieza, batería y señal, uno por uno.""",
        tt=[("Hileras de arándanos con un sensor", "Instalar sensores es solo el inicio."),
            ("Manos limpiando un sensor", "Esta semana revisamos 25 sensores de humedad de suelo."),
            ("Celular con la señal verificada", "Limpieza, batería y señal. Así cuidamos el dato.")],
        tit="El dato también se mantiene", bul=[("25 sensores revisados", "En un fundo de arándanos."),
                                                ("Batería y señal", "Verificadas una por una."),
                                                ("Visitas programadas", "Acompañamiento continuo.")],
        dato="25 sensores con mantenimiento preventivo", cta="Conversemos",
        tags=["#Agroindustria", "#Arándanos", "#IoT", "#Mantenimiento"],
        vis="Blueberry field rows with a soil moisture sensor in the foreground and morning mist",
        adj="campo",
    ),
    dict(
        id="hw21", area="hardware", sector="logística y transporte", tipo="interno", pilar="producto",
        sec="matriz", mod="boton-panico",
        det="Terminado el botón de pánico para cabina: al presionarlo 3 segundos envía la ubicación y una alerta a la central; funciona aunque no haya datos móviles usando SMS. Probado en 30 activaciones.",
        fuente="Botón de pánico para cabina", valor=4,
        razon="Producto propio terminado y probado; beneficio claro de seguridad.",
        li="""Cuando algo sale mal en ruta, pedir ayuda no puede depender de la señal de datos.

Terminamos nuestro botón de pánico para cabina: al presionarlo 3 segundos envía la ubicación y una alerta a la central. Si no hay datos móviles, la alerta sale por SMS.

Lo probamos en 30 activaciones antes de darlo por terminado.

Seguridad para conductores y tranquilidad para la central. ¿Quieres conocerlo? Escríbenos.""",
        fb="Nuestro botón de pánico para cabina envía ubicación y alerta a la central con solo 3 segundos; sin datos móviles, usa SMS. Probado en 30 activaciones.",
        ig="""🚨 Ayuda con un solo botón.
3 segundos presionado y la central recibe tu ubicación. Sin datos móviles, la alerta sale por SMS. Probado en 30 activaciones.""",
        tt=[("Cabina de camión de noche", "En ruta, pedir ayuda no puede depender de la señal."),
            ("Mano presionando el botón", "Con 3 segundos, la central recibe tu ubicación."),
            ("Mensaje SMS llegando a la central", "Y si no hay datos móviles, la alerta sale por SMS.")],
        tit="Ayuda con un solo botón", bul=[("3 segundos", "Para activar la alerta."),
                                            ("Ubicación a la central", "Respuesta más rápida."),
                                            ("Respaldo por SMS", "Funciona sin datos móviles.")],
        dato="Probado en 30 activaciones", cta="Escríbenos",
        tags=["#SeguridadVial", "#Logística", "#Hardware", "#Transporte"],
        vis="Close-up of a red panic button mounted on a truck dashboard at night, soft red ambient light",
    ),
    dict(
        id="hw22", area="hardware", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Se recibió a 2 practicantes de ingeniería electrónica en el laboratorio; su primer reto fue armar y calibrar una estación de clima en una semana",
        fuente="Llegada de practicantes al laboratorio", valor=3,
        razon="Contenido de cultura y talento sin datos personales ni sensibles.",
        li="""Su primer reto: armar una estación de clima en una semana.

Damos la bienvenida a 2 practicantes de ingeniería electrónica que se suman a nuestro laboratorio de hardware. Aquí aprenderán como aprendimos todos: con un proyecto real desde el primer día.

Creemos en el talento de la región y en abrir espacios para que crezca cerca de casa.

¡Bienvenidos al equipo!""",
        fb="Damos la bienvenida a 2 practicantes de ingeniería electrónica. Su primer reto: armar y calibrar una estación de clima en una semana. ¡Bienvenidos!",
        ig="""👋 Bienvenidos al laboratorio.
2 practicantes de ingeniería electrónica se suman al equipo. Primer reto: una estación de clima en una semana.""",
        tt=[("Puerta del laboratorio abriéndose", "Hoy llegan 2 nuevos practicantes."),
            ("Piezas de una estación de clima sobre la mesa", "Su primer reto: armar una estación de clima en una semana."),
            ("Estación terminada en la azotea", "Así se aprende aquí: con proyectos reales.")],
        tit="Bienvenidos al laboratorio", bul=[("2 practicantes", "De ingeniería electrónica."),
                                               ("Un reto real", "Estación de clima en una semana."),
                                               ("Talento local", "Crecer cerca de casa.")],
        dato=None, cta="Únete al equipo",
        tags=["#Talento", "#Prácticas", "#CulturaCorAll", "#Electrónica"],
        vis="Electronics lab with weather station parts laid out on a workbench, welcoming warm light",
    ),
    dict(
        id="hw23", area="hardware", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="nivel-tanques",
        det="Sensores ultrasónicos de nivel instalados en 6 tanques de agua de proceso de {cliente}; la plataforma muestra el nivel en tiempo real y avisa al bajar del 20 %.",
        fuente="Monitoreo de nivel de tanques", valor=4,
        razon="Solución instalada con beneficio claro; no se identifica al cliente.",
        li="""Que un tanque se quede vacío no debería ser una sorpresa.

Instalamos sensores ultrasónicos de nivel en 6 tanques de agua de proceso de una operación minera. La plataforma muestra el nivel en tiempo real y envía un aviso cuando baja del 20 %.

El equipo ya no tiene que subir a revisar cada tanque: el dato llega solo y a tiempo para reponer.

¿Dónde necesitas medir nivel en tu operación? Conversemos.""",
        fb="Sensores de nivel en 6 tanques de agua de proceso: nivel en tiempo real y aviso cuando baja del 20 %. Menos revisiones manuales, más tiempo para reponer.",
        ig="""💧 Nivel de tanques en tiempo real.
6 tanques de agua de proceso monitoreados y aviso automático cuando bajan del 20 %.""",
        tt=[("Tanques industriales al aire libre", "¿Todavía subes a revisar cada tanque?"),
            ("Sensor ultrasónico en la tapa", "Este sensor mide el nivel en tiempo real."),
            ("Aviso de nivel bajo en el celular", "Y avisa cuando baja del 20 %.")],
        tit="Tus tanques en tiempo real", bul=[("6 tanques", "Monitoreados en la operación."),
                                               ("Nivel en vivo", "Sin subir a revisar."),
                                               ("Aviso al 20 %", "Tiempo para reponer.")],
        dato="Aviso automático por debajo del 20 %", cta="Conversemos",
        tags=["#Minería", "#IoT", "#GestiónDelAgua", "#Monitoreo"],
        vis="Industrial water tanks at a mining site with ultrasonic sensors on top, clear sky",
    ),
    dict(
        id="hw24", area="hardware", sector="agroindustria", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="Se cerró el primer lote de producción de 30 sensores de pulpa ensamblados y probados en el laboratorio de CorAll; todos pasaron la prueba de calibración",
        fuente="Primer lote de producción de sensores", valor=5,
        razon="Hito propio de producción con resultado verificable.",
        li="""Del prototipo al primer lote: 30 sensores listos.

Cerramos el primer lote de producción de nuestro sensor de pulpa de fruta. Ensamblamos y probamos 30 unidades en nuestro laboratorio de Trujillo, y todas pasaron la prueba de calibración.

Pasar de un prototipo que funciona a un lote que funciona igual es uno de los saltos más difíciles en hardware. Hoy lo celebramos.

Gracias al equipo que lo hizo posible.""",
        fb="Primer lote de producción cerrado: 30 sensores de pulpa ensamblados y probados en Trujillo, y todos pasaron la calibración. ¡Gracias, equipo!",
        ig="""✅ 30 de 30.
Primer lote de producción del sensor de pulpa: 30 unidades ensambladas en Trujillo y todas pasaron la calibración.""",
        tt=[("Un solo prototipo sobre la mesa", "Así empezó: un prototipo."),
            ("Fila de 30 sensores ensamblados", "Hoy cerramos el primer lote: 30 sensores."),
            ("Check en la prueba de calibración", "Y todos pasaron la calibración.")],
        tit="Primer lote: 30 sensores", bul=[("30 unidades", "Ensambladas en Trujillo."),
                                             ("Todas calibradas", "Sin excepciones."),
                                             ("Del prototipo al lote", "Un gran salto.")],
        dato="30 de 30 sensores pasaron la calibración", cta="Conoce el sensor",
        tags=["#HechoEnTrujillo", "#Hardware", "#Agroindustria", "#Producción"],
        vis="Neat rows of identical small industrial sensors on an assembly table, top-down shot",
    ),
    dict(
        id="hw25", area="hardware", sector="logística y transporte", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Guía para el área comercial: diferencias entre GPS con red celular y con LoRa para rastreo de activos; celular para unidades en ruta, LoRa para activos dentro de un predio",
        fuente="Celular o LoRa para rastreo de activos", valor=3,
        razon="Contenido educativo general que ayuda al cliente a elegir; sin datos internos.",
        li="""¿Celular o LoRa para rastrear tus activos? No es una pregunta técnica, es de operación.

- Red celular: ideal para unidades que salen a ruta y recorren grandes distancias.
- LoRa: ideal para activos dentro de un predio, como un fundo, una planta o un patio de maniobras, con bajo consumo y sin costo de datos por equipo.

Muchas operaciones necesitan ambos. Lo importante es elegir según dónde se mueve cada activo.

¿Tienes dudas sobre cuál te conviene? Escríbenos.""",
        fb="¿Celular o LoRa? Celular para unidades en ruta; LoRa para activos dentro de un predio, con bajo consumo. Te ayudamos a elegir.",
        ig="""📍 ¿Celular o LoRa?
Celular para unidades en ruta. LoRa para activos dentro de un fundo, planta o patio. Elige según dónde se mueve cada activo.""",
        tt=[("Camión en carretera", "Si tu activo sale a ruta, usa red celular."),
            ("Montacargas dentro de una planta", "Si se mueve dentro de un predio, LoRa."),
            ("Mapa con ambos tipos de activos", "Muchas operaciones necesitan ambos.")],
        tit="¿Celular o LoRa?", bul=[("Celular", "Unidades en ruta."),
                                     ("LoRa", "Activos dentro del predio."),
                                     ("Ambos", "Según tu operación.")],
        dato=None, cta="Escríbenos",
        tags=["#LoRa", "#GPS", "#Logística", "#BuenasPrácticas"],
        vis="Split illustration: a truck on a highway on one side, a forklift inside a warehouse on the other",
        comp="antes / después",
    ),
]
