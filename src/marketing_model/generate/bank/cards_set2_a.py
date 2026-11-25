"""Second set of publishable tasks (v0.2): hardware and software."""

CARDS = [
    # ---------------- hardware ----------------
    dict(
        id="hw26", area="hardware", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="caudal-agua",
        det="Entrega de 4 caudalímetros conectados para el circuito de agua de proceso de {cliente}: miden caudal y presión cada minuto y envían el dato por radio a la sala de control a 1,5 km. En 10 días de prueba no se perdió ningún reporte.",
        fuente="Caudalímetros conectados para agua de proceso", valor=5,
        razon="Equipos entregados con un resultado de prueba concreto; se cuenta sin nombrar al cliente.",
        li="""¿Cuánta agua está pasando ahora mismo por tu circuito de proceso?

Entregamos 4 caudalímetros conectados para una operación minera. Miden caudal y presión cada minuto y envían el dato por radio a la sala de control, a 1,5 km de distancia.

En 10 días de prueba no se perdió ningún reporte.

Hardware diseñado y armado en Trujillo para condiciones exigentes. ¿Necesitas medir agua en tu operación? Conversemos.""",
        fb="Entregamos 4 caudalímetros conectados para una operación minera: caudal y presión cada minuto, enviados por radio a 1,5 km. En 10 días de prueba no se perdió ningún reporte.",
        ig="""💧 El agua de tu proceso, medida minuto a minuto.
Caudal y presión enviados por radio a la sala de control, a 1,5 km. 10 días de prueba sin perder un reporte.""",
        tt=[("Tubería de agua en una operación minera", "¿Sabes cuánta agua pasa ahora por tu proceso?"),
            ("Caudalímetro con antena sobre la tubería", "Estos equipos miden caudal y presión cada minuto."),
            ("Pantalla de la sala de control", "Y envían el dato por radio a 1,5 km, sin perder reportes.")],
        tit="Agua medida minuto a minuto", bul=[("Caudal y presión", "Dos variables en un solo equipo."),
                                               ("Reporte cada minuto", "Dato continuo para la sala de control."),
                                               ("Radio a 1,5 km", "Sin cables hasta la sala.")],
        dato="10 días de prueba sin perder reportes", cta="Conversemos",
        tags=["#Minería", "#GestiónDelAgua", "#IoT", "#Telemetría"],
        vis="Industrial flow meter with a small radio antenna mounted on a steel water pipe at a mining site, clear daylight",
    ),
    dict(
        id="hw27", area="hardware", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="hornos-vulcanizado",
        det="Control de temperatura de los hornos de vulcanizado de {cliente}: 3 hornos con sensores y alarma en el celular del jefe de planta si la temperatura sale del rango. Funcionando en los 2 turnos desde el lunes.",
        fuente="Control de temperatura de hornos de vulcanizado", valor=4,
        razon="Solución en operación con un beneficio claro para el sector; no expone datos del cliente.",
        li="""Un horno fuera de temperatura puede arruinar un lote entero de suelas.

En una fábrica de calzado instalamos sensores en 3 hornos de vulcanizado. Si la temperatura sale del rango, el jefe de planta recibe la alarma en su celular al momento.

Ya funciona en los 2 turnos de producción.

Así se corrige a tiempo, no al final del lote. ¿Tu planta tiene un punto crítico de temperatura? Cuéntanos tu caso.""",
        fb="Instalamos control de temperatura en 3 hornos de vulcanizado de una fábrica de calzado: alarma en el celular del jefe de planta si algo sale del rango, en los 2 turnos.",
        ig="""🔥 Hornos bajo control, turno tras turno.
Sensores en 3 hornos de vulcanizado y alarma al celular si la temperatura sale del rango.""",
        tt=[("Horno de vulcanizado en una fábrica de calzado", "¿Qué pasa si el horno se sale de temperatura?"),
            ("Sensor instalado en el horno", "Instalamos sensores en 3 hornos de vulcanizado."),
            ("Alarma llegando al celular", "Si algo sale del rango, el jefe de planta lo sabe al momento.")],
        tit="Hornos bajo control", bul=[("Tres hornos monitoreados", "Temperatura en tiempo real."),
                                        ("Alarma al celular", "Aviso inmediato al jefe de planta."),
                                        ("Dos turnos cubiertos", "Control durante toda la producción.")],
        dato=None, cta="Cuéntanos tu caso",
        tags=["#Calzado", "#IoT", "#ControlDeCalidad", "#Industria40"],
        vis="Industrial shoe sole vulcanizing oven with a small temperature sensor and a smartphone showing a temperature graph",
    ),
    dict(
        id="hw28", area="hardware", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="guias-campo",
        det="Se documentó la guía de grados de protección para los equipos de campo: qué significa IP54, IP65 e IP67 y cuándo conviene cada uno según polvo, lluvia o inmersión.",
        fuente="Guía de grados de protección IP", valor=3,
        razon="Contenido educativo útil para clientes que compran equipos de campo; no revela nada interno.",
        li="""IP54, IP65, IP67: ¿qué significan esas letras en la ficha de un equipo?

El código IP indica cuánto protege una caja contra el polvo (primer número) y contra el agua (segundo número).

IP54 resiste polvo y salpicaduras. IP65 aguanta polvo y chorros de agua, ideal para campo abierto. IP67 soporta incluso una inmersión breve.

Antes de comprar un equipo para exteriores, revisa este dato. ¿Tienes dudas sobre el tuyo? Escríbenos.""",
        fb="¿IP54, IP65 o IP67? El código IP indica la protección contra polvo y agua. Para campo abierto, IP65 suele ser lo mínimo recomendable.",
        ig="""🌧️ ¿Tu equipo aguanta la lluvia?
El código IP te lo dice: IP54 salpicaduras, IP65 chorros de agua, IP67 inmersión breve.""",
        tt=[("Equipo electrónico bajo la lluvia", "¿Tu equipo de campo aguanta la lluvia?"),
            ("Etiqueta con el código IP", "Mira el código IP: el primer número es polvo, el segundo es agua."),
            ("Tres cajas lado a lado", "IP54 salpicaduras, IP65 chorros de agua, IP67 inmersión breve.")],
        tit="¿Qué significa el código IP?", bul=[("Primer número: polvo", "Protección contra partículas."),
                                                 ("Segundo número: agua", "Protección contra líquidos."),
                                                 ("Campo abierto: IP65", "Lo mínimo recomendable afuera.")],
        dato=None, cta="Escríbenos",
        tags=["#Electrónica", "#IoT", "#Hardware", "#Tips"],
        vis="3D illustration of three sealed electronic enclosures with water droplets and dust particles around them",
    ),
    dict(
        id="hw29", area="hardware", sector="educación", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="Se armó el sensor número 100 en el laboratorio de CorAll, desde el primer lote de 12 equipos a inicios de año",
        fuente="Sensor número 100 armado en el laboratorio", valor=4,
        razon="Hito propio del laboratorio, fácil de celebrar sin datos sensibles.",
        li="""100 sensores armados en Trujillo.

A inicios de año armamos nuestro primer lote de 12 equipos. Hoy salió del laboratorio el sensor número 100.

Cada uno pasó por diseño, soldadura, pruebas y calibración en nuestro propio laboratorio.

Gracias a los clientes que confiaron en hardware hecho en la región. Vamos por los siguientes 100.""",
        fb="¡Llegamos a 100 sensores armados en nuestro laboratorio de Trujillo! Empezamos con un lote de 12 a inicios de año.",
        ig="""🎉 100 sensores hechos en Trujillo.
Empezamos con un lote de 12 a inicios de año. Diseño, soldadura y pruebas en nuestro laboratorio.""",
        tt=[("Mesa con sensores alineados", "Este es el sensor número 100 de nuestro laboratorio."),
            ("Soldadura de una placa", "Empezamos este año con un lote de 12."),
            ("Equipo celebrando en el laboratorio", "Gracias por confiar en hardware hecho en Trujillo.")],
        tit="100 sensores hechos en Trujillo", bul=[("Diseño propio", "Desde la placa hasta la caja."),
                                                    ("Pruebas en laboratorio", "Cada equipo se calibra."),
                                                    ("Hecho en Trujillo", "Hardware de la región.")],
        dato="100 sensores armados este año", cta="Conoce más",
        tags=["#HechoEnTrujillo", "#Hardware", "#IoT", "#Electrónica"],
        vis="Neat grid of one hundred small identical sensor devices on a lab table seen from above, warm celebratory light",
    ),
    dict(
        id="hw30", area="hardware", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Visita al fundo de {cliente} para reubicar 12 sensores de humedad de suelo según el nuevo trazado de riego; el cliente autorizó compartir fotos del campo sin su nombre",
        fuente="Reubicación de sensores de suelo en campo", valor=4,
        razon="Trabajo en campo autorizado; muestra acompañamiento sin identificar al cliente.",
        li="""Cuando cambia el riego, los sensores también tienen que moverse.

Esta semana estuvimos en un fundo de la región reubicando 12 sensores de humedad de suelo según el nuevo trazado de riego.

Un sensor mal ubicado mide bien, pero mide el lugar equivocado. Por eso el trabajo no termina con la instalación.

Acompañamos a nuestros clientes en campo durante toda la vida del equipo.""",
        fb="En campo reubicando 12 sensores de humedad de suelo según el nuevo trazado de riego de un fundo de la región.",
        ig="""🌱 Medir bien también es medir en el lugar correcto.
Reubicamos 12 sensores de humedad de suelo según el nuevo trazado de riego.""",
        tt=[("Técnico caminando entre surcos", "¿Qué pasa cuando cambia el trazado de riego?"),
            ("Sensor siendo reinstalado", "Movimos 12 sensores de humedad de suelo."),
            ("Vista del campo regado", "Porque un sensor tiene que medir el lugar correcto.")],
        tit="Sensores donde se necesitan", bul=[("Doce sensores reubicados", "Según el nuevo riego."),
                                                ("Trabajo en campo", "Con el equipo del fundo."),
                                                ("Acompañamiento continuo", "Más allá de la instalación.")],
        dato="12 sensores reubicados", cta="Conversemos",
        tags=["#AgriculturaDePrecisión", "#Agroindustria", "#Riego", "#IoT"],
        vis="Crop rows with a soil moisture sensor in the foreground and a soft red overlay band at the bottom",
        adj="campo",
    ),
    dict(
        id="hw31", area="hardware", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller presencial 'Arma tu primer sensor' en el laboratorio de CorAll: sábado 5 de diciembre, de 9:00 a 12:00, cupos limitados e inscripción por mensaje directo",
        fuente="Taller presencial para armar un sensor", valor=4,
        razon="Evento propio confirmado con fecha, hora y lugar.",
        li="""¿Siempre quisiste armar un sensor con tus propias manos?

Te invitamos al taller presencial "Arma tu primer sensor" en nuestro laboratorio.

📅 Sábado 5 de diciembre
🕘 De 9:00 a 12:00
📍 Laboratorio de CorAll, Trujillo

Cupos limitados. Inscríbete por mensaje directo.""",
        fb="Taller presencial 'Arma tu primer sensor': sábado 5 de diciembre, de 9:00 a 12:00, en nuestro laboratorio. Cupos limitados, inscríbete por mensaje directo.",
        ig="""🔧 Arma tu primer sensor con nosotros.
Sábado 5 de diciembre, de 9:00 a 12:00, en nuestro laboratorio. Cupos limitados.""",
        tt=[("Manos soldando una placa", "¿Quieres armar tu primer sensor?"),
            ("Laboratorio con mesas listas", "Ven a nuestro taller presencial en Trujillo."),
            ("Fecha en pantalla", "Sábado 5 de diciembre, de 9:00 a 12:00.")],
        tit="Arma tu primer sensor", bul=[("Sábado 5 de diciembre", "De 9:00 a 12:00."),
                                          ("Presencial", "En nuestro laboratorio."),
                                          ("Cupos limitados", "Inscríbete por mensaje.")],
        dato="Sábado 5 de diciembre, de 9:00 a 12:00", cta="Inscríbete",
        tags=["#TallerIoT", "#Electrónica", "#Trujillo", "#Aprende"],
        vis="Electronics workbench prepared for a workshop with soldering irons, sensor kits and empty stools, bright light",
    ),
    dict(
        id="hw32", area="hardware", sector="logística y transporte", tipo="interno", pilar="producto",
        sec="matriz", mod="sensor-puerta",
        det="Terminado el sensor de puerta para furgones: avisa a la central cuando la puerta se abre fuera de una zona autorizada y guarda la hora de cada apertura. Probado en 40 aperturas en el patio.",
        fuente="Sensor de apertura de puertas para furgones", valor=4,
        razon="Producto propio terminado y probado; aporta a clientes de transporte.",
        li="""¿Sabes cuándo y dónde se abre la puerta de tu furgón?

Terminamos nuestro sensor de puerta para furgones. Si la puerta se abre fuera de una zona autorizada, la central recibe el aviso al momento, y cada apertura queda registrada con su hora.

Lo probamos en 40 aperturas en patio antes de llevarlo a ruta.

Más control sobre la carga, sin cambiar la operación. ¿Te interesa para tu flota? Conversemos.""",
        fb="Nuevo sensor de puerta para furgones: aviso a la central si se abre fuera de zona y registro de cada apertura. Probado en 40 aperturas.",
        ig="""🚪 Tu carga, bajo control.
Nuestro sensor avisa si la puerta del furgón se abre fuera de zona y registra cada apertura.""",
        tt=[("Puerta trasera de un furgón", "¿Quién abrió la puerta del furgón, y dónde?"),
            ("Sensor en el marco de la puerta", "Nuestro sensor registra cada apertura con su hora."),
            ("Alerta en la pantalla de la central", "Y avisa si se abre fuera de una zona autorizada.")],
        tit="Cada apertura, registrada", bul=[("Aviso fuera de zona", "Alerta inmediata a la central."),
                                              ("Registro con hora", "Historial de cada apertura."),
                                              ("Probado en patio", "Antes de salir a ruta.")],
        dato="Probado en 40 aperturas", cta="Conversemos",
        tags=["#Logística", "#SeguridadDeCarga", "#IoT", "#GestiónDeFlotas"],
        vis="Back doors of a cargo van at night with a small sensor on the door frame and a soft red glow",
    ),
    dict(
        id="hw33", area="hardware", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Clase interna del equipo de hardware al equipo de software: cómo leer un esquemático y usar el multímetro; asistieron 11 personas",
        fuente="Clase interna de hardware para el equipo de software", valor=3,
        razon="Muestra la cultura de aprendizaje entre áreas; no contiene información sensible.",
        li="""En CorAll, el equipo de hardware le dio clase al de software.

Esta semana 11 personas aprendieron a leer un esquemático y a usar el multímetro, explicado por sus propios compañeros.

Cuando quien programa entiende el circuito, y quien diseña el circuito entiende el código, las soluciones salen mejor integradas.

Así aprendemos: entre nosotros y con las manos en la mesa.""",
        fb="Clase interna: nuestro equipo de hardware enseñó a 11 compañeros a leer un esquemático y usar el multímetro.",
        ig="""🔌 Software aprendiendo hardware.
11 compañeros aprendieron a leer un esquemático y usar el multímetro, en una clase dictada por el propio equipo.""",
        tt=[("Multímetro sobre una placa", "¿Un programador usando multímetro?"),
            ("Esquemático proyectado en la pared", "Nuestro equipo de hardware dio clase al de software."),
            ("Mesa con placas y laptops", "Así aprendemos: entre nosotros.")],
        tit="Software aprende hardware", bul=[("Leer un esquemático", "La base de todo circuito."),
                                              ("Usar el multímetro", "Medir antes de suponer."),
                                              ("Aprendizaje entre áreas", "Enseñan los propios compañeros.")],
        dato="11 personas en la clase", cta="Conoce más",
        tags=["#CulturaCorAll", "#Aprendizaje", "#Electrónica", "#TrabajoEnEquipo"],
        vis="Electronics lab table with a multimeter, circuit boards, laptops and a projected schematic in the background, no faces",
    ),
    dict(
        id="hw34", area="hardware", sector="cuero y calzado", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se preparó la ficha comercial de equipos para talleres de calzado: contador de pares, control de temperatura de hornos y sensor de humedad para almacenes de cuero",
        fuente="Ficha comercial de equipos para calzado", valor=4,
        razon="Catálogo propio de soluciones; contenido comercial sin datos de clientes.",
        li="""Tres equipos pensados para talleres y fábricas de calzado.

👟 Contador de pares: cuenta la producción al final de la faja, sin conteo manual.
🔥 Control de temperatura de hornos: alarma al celular si el horno sale del rango.
💧 Sensor de humedad para almacenes de cuero: avisa antes de que el cuero se dañe.

Todos diseñados y armados en Trujillo, con soporte local. ¿Cuál necesita tu taller? Escríbenos.""",
        fb="Equipos para talleres de calzado: contador de pares, control de temperatura de hornos y sensor de humedad para almacenes de cuero. Hechos en Trujillo.",
        ig="""👟 Tecnología para tu taller de calzado.
Contador de pares, control de hornos y sensor de humedad para el almacén de cuero.""",
        tt=[("Faja de producción de calzado", "Tres equipos para tu taller de calzado."),
            ("Contador de pares y horno", "Cuenta pares y controla la temperatura de tus hornos."),
            ("Almacén de cuero con sensor", "Y cuida la humedad de tu almacén de cuero.")],
        tit="Tecnología para tu taller", bul=[("Contador de pares", "Producción contada sin esfuerzo."),
                                              ("Control de hornos", "Alarma si sale del rango."),
                                              ("Humedad del almacén", "Cuero protegido.")],
        dato=None, cta="Escríbenos",
        tags=["#Calzado", "#Trujillo", "#IoT", "#HardwareAMedida"],
        vis="Grid of three clean line icons for a shoe counter, an oven and a humidity drop over a leather texture background",
        comp="grilla",
    ),
    dict(
        id="hw35", area="hardware", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se redactó para productores una explicación de cómo leer la humedad de suelo: capacidad de campo, punto de marchitez y en qué rango conviene regar",
        fuente="Cómo leer la humedad de suelo", valor=3,
        razon="Contenido educativo para clientes agrícolas; no expone información interna.",
        li="""Tu sensor marca un porcentaje de humedad. ¿Y ahora qué?

Para leer bien el dato hay que conocer dos puntos de tu suelo:
• Capacidad de campo: el máximo de agua que el suelo retiene después de regar.
• Punto de marchitez: por debajo de ese nivel, la planta ya no puede absorber agua.

El riego conviene antes de acercarse al punto de marchitez, sin pasar de la capacidad de campo. ¿Quieres ayuda para calibrar tus sensores? Escríbenos.""",
        fb="¿Cómo leer el dato de humedad de suelo? Conoce la capacidad de campo y el punto de marchitez de tu suelo y riega entre esos dos límites.",
        ig="""🌱 ¿Qué significa el dato de humedad de tu suelo?
Riega entre dos límites: la capacidad de campo y el punto de marchitez.""",
        tt=[("Sensor de humedad clavado en el suelo", "Tu sensor marca la humedad. ¿Y ahora qué?"),
            ("Gráfico con dos líneas de límite", "Conoce dos puntos: capacidad de campo y punto de marchitez."),
            ("Riego por goteo funcionando", "Riega entre esos dos límites.")],
        tit="Cómo leer la humedad", bul=[("Capacidad de campo", "El máximo que retiene el suelo."),
                                         ("Punto de marchitez", "El mínimo para la planta."),
                                         ("Riega entre ambos", "Ni de más ni de menos.")],
        dato=None, cta="Escríbenos",
        tags=["#Riego", "#AgriculturaDePrecisión", "#Agroindustria", "#Tips"],
        vis="3D illustration of a soil cross-section with a moisture sensor and two horizontal level lines, plant roots visible",
    ),
    dict(
        id="hw36", area="hardware", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="horometros",
        det="Entrega del tablero de horómetros para 18 equipos pesados de {cliente}: cada equipo envía sus horas de motor y el sistema avisa 50 horas antes del mantenimiento programado.",
        fuente="Tablero de horómetros para equipos pesados", valor=5,
        razon="Solución entregada con alcance concreto; se describe sin nombrar al cliente.",
        li="""El mantenimiento llega a tiempo cuando el equipo avisa solo.

Entregamos un tablero de horómetros para 18 equipos pesados de una operación minera. Cada equipo envía sus horas de motor y el sistema avisa 50 horas antes del mantenimiento programado.

Sin planillas ni lecturas a mano: el área de mantenimiento planifica con datos.

¿Tu flota de equipos todavía se controla en papel? Conversemos.""",
        fb="Tablero de horómetros para 18 equipos pesados: horas de motor en línea y aviso 50 horas antes de cada mantenimiento.",
        ig="""⚙️ El mantenimiento, a tiempo.
18 equipos pesados envían sus horas de motor y el sistema avisa 50 horas antes del mantenimiento.""",
        tt=[("Equipo pesado en una mina", "¿Cómo sabes cuándo le toca mantenimiento a cada equipo?"),
            ("Tablero con horas de motor", "Cada equipo envía sus horas de motor al tablero."),
            ("Aviso en pantalla", "Y el sistema avisa 50 horas antes del mantenimiento.")],
        tit="Mantenimiento que avisa solo", bul=[("Horas de motor", "Lectura automática por equipo."),
                                                 ("Aviso anticipado", "Antes del mantenimiento."),
                                                 ("Sin planillas", "Datos para planificar.")],
        dato="18 equipos pesados conectados", cta="Conversemos",
        tags=["#Minería", "#MantenimientoPreventivo", "#IoT", "#Telemetría"],
        vis="Heavy mining haul truck at an open pit at dawn with a subtle dashboard overlay showing engine hours",
    ),
    dict(
        id="hw37", area="hardware", sector="logística y transporte", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Se cumplió un año de los sensores de temperatura en la flota refrigerada de {cliente}; el cliente autorizó compartir sin su nombre que en ese tiempo se registraron más de 3 millones de lecturas",
        fuente="Un año de monitoreo en una flota refrigerada", valor=4,
        razon="Hito con un cliente que autorizó la difusión sin nombre.",
        li="""Un año cuidando la cadena de frío, lectura por lectura.

Hace un año instalamos sensores de temperatura en la flota refrigerada de una empresa de transporte. Desde entonces se registraron más de 3 millones de lecturas.

Cada una es una carga que llegó dentro de su rango, o una alerta que permitió actuar a tiempo.

Gracias por la confianza. Vamos por el segundo año.""",
        fb="Un año de monitoreo de temperatura en la flota refrigerada de un cliente de transporte: más de 3 millones de lecturas registradas.",
        ig="""❄️ Un año cuidando la cadena de frío.
Más de 3 millones de lecturas de temperatura en una flota refrigerada.""",
        tt=[("Camión refrigerado en carretera", "Hace un año instalamos estos sensores."),
            ("Sensor en la puerta del contenedor", "Miden la temperatura de la carga en todo el viaje."),
            ("Contador de lecturas en pantalla", "Ya van más de 3 millones de lecturas.")],
        tit="Un año de cadena de frío", bul=[("Un año en ruta", "Monitoreo continuo."),
                                             ("Millones de lecturas", "Temperatura de cada viaje."),
                                             ("Alertas a tiempo", "Para actuar antes.")],
        dato="Más de 3 millones de lecturas", cta="Conoce más",
        tags=["#CadenaDeFrío", "#Logística", "#IoT", "#Telemetría"],
        vis="Refrigerated truck on a coastal highway at dusk with a subtle glowing sensor icon and soft data lines",
    ),
    dict(
        id="hw38", area="hardware", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="kits-ambientales",
        det="Entrega de 20 kits de medición ambiental para los laboratorios de {cliente}: miden temperatura, humedad y calidad del aire, y los alumnos ven los datos en una página web.",
        fuente="Kits de medición ambiental para laboratorios escolares", valor=4,
        razon="Producto entregado a una institución educativa; se describe sin nombrarla.",
        li="""¿Cómo está el aire de tu salón de clase? Ahora los alumnos lo pueden medir.

Entregamos 20 kits de medición ambiental para los laboratorios de una institución educativa. Miden temperatura, humedad y calidad del aire, y los datos se ven en una página web.

Ciencia con datos reales del propio colegio, no solo del libro.

¿Quieres llevar kits como estos a tu institución? Escríbenos.""",
        fb="Entregamos 20 kits de medición ambiental para laboratorios escolares: temperatura, humedad y calidad del aire, con los datos en una página web.",
        ig="""🌡️ Ciencia con datos reales.
20 kits para medir temperatura, humedad y calidad del aire, con los datos en una página web.""",
        tt=[("Alumno junto a un kit en el laboratorio", "¿Cómo está el aire de tu salón?"),
            ("Kit de medición sobre la mesa", "Estos kits miden temperatura, humedad y calidad del aire."),
            ("Gráfico en una laptop", "Y los alumnos ven sus datos en una página web.")],
        tit="Ciencia con datos reales", bul=[("Tres variables", "Temperatura, humedad y aire."),
                                             ("Datos en la web", "Fáciles de consultar."),
                                             ("Para laboratorios escolares", "Aprender midiendo.")],
        dato="20 kits entregados", cta="Escríbenos",
        tags=["#EducaciónSTEM", "#IoT", "#CalidadDelAire", "#Electrónica"],
        vis="School lab table with small environmental sensor kits and a laptop showing simple colorful charts, bright daylight",
    ),
    dict(
        id="hw39", area="hardware", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Revisión en sitio de 30 equipos GPS de la flota de {cliente}: se cambiaron 4 antenas y se ajustó la frecuencia de reporte; el cliente autorizó publicar el trabajo sin su nombre",
        fuente="Revisión en sitio de equipos GPS", valor=3,
        razon="Servicio en sitio autorizado; muestra soporte sin identificar al cliente.",
        li="""Un GPS instalado no es un trabajo terminado.

Esta semana revisamos en sitio 30 equipos GPS de la flota de un cliente de transporte. Cambiamos 4 antenas y ajustamos la frecuencia de reporte según el uso real de cada unidad.

El mantenimiento preventivo evita que una unidad "desaparezca" del mapa justo cuando más se necesita.

¿Tus equipos de rastreo tienen quién los revise? Conversemos.""",
        fb="Revisión en sitio de 30 equipos GPS: cambio de 4 antenas y ajuste de la frecuencia de reporte según el uso de cada unidad.",
        ig="""🛰️ Mantenimiento que se nota en el mapa.
Revisamos 30 equipos GPS en sitio y ajustamos cada uno según su uso real.""",
        tt=[("Técnico revisando un camión", "Revisamos en sitio 30 equipos GPS."),
            ("Antena nueva instalada", "Cambiamos antenas y ajustamos cada equipo."),
            ("Mapa con todas las unidades", "Para que ninguna unidad desaparezca del mapa.")],
        tit="Rastreo siempre en línea", bul=[("Revisión en sitio", "Equipo por equipo."),
                                             ("Antenas renovadas", "Mejor señal en ruta."),
                                             ("Reporte ajustado", "Según el uso real.")],
        dato="30 equipos GPS revisados", cta="Conversemos",
        tags=["#GPS", "#GestiónDeFlotas", "#Logística", "#Soporte"],
        vis="Technician hands installing a small GPS antenna on a truck cab roof in a depot, no faces, golden hour",
    ),
    dict(
        id="hw40", area="hardware", sector="logística y transporte", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó una guía para clientes: qué revisar antes de comprar un GPS para flota (frecuencia de reporte, batería de respaldo, alertas y soporte local)",
        fuente="Qué revisar antes de comprar un GPS para flota", valor=3,
        razon="Contenido educativo útil para clientes de transporte; sin datos internos.",
        li="""¿Vas a comprar GPS para tu flota? Revisa estos 4 puntos antes de decidir.

1. Frecuencia de reporte: ¿cada cuánto envía la ubicación?
2. Batería de respaldo: ¿sigue reportando si desconectan el equipo?
3. Alertas: ¿avisa por exceso de velocidad, paradas o salida de zona?
4. Soporte local: ¿quién lo revisa si falla en ruta?

El precio importa, pero estos puntos deciden si el equipo sirve. ¿Tienes dudas? Escríbenos.""",
        fb="Antes de comprar GPS para tu flota revisa: frecuencia de reporte, batería de respaldo, alertas y soporte local.",
        ig="""🚚 ¿GPS para tu flota? Revisa esto primero.
Frecuencia de reporte, batería de respaldo, alertas y soporte local.""",
        tt=[("Camiones estacionados en fila", "¿Vas a comprar GPS para tu flota?"),
            ("Equipo GPS en la mano", "Revisa la frecuencia de reporte y la batería de respaldo."),
            ("Técnico en el patio", "Y pregunta por las alertas y el soporte local.")],
        tit="Antes de comprar un GPS", bul=[("Frecuencia de reporte", "Cada cuánto ubica."),
                                            ("Batería de respaldo", "Si lo desconectan."),
                                            ("Soporte local", "Quién lo revisa.")],
        dato=None, cta="Escríbenos",
        tags=["#GPS", "#GestiónDeFlotas", "#Logística", "#Tips"],
        vis="3D illustration of a small GPS tracker with four floating checklist icons around it, clean light background",
    ),
    # ---------------- software ----------------
    dict(
        id="sw26", area="software", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="asistencia-cuadrillas",
        det="App de asistencia para las cuadrillas de {cliente}: el capataz escanea el QR del fotocheck al ingreso y a la salida, y funciona sin señal. Registró 240 asistencias en el primer día.",
        fuente="App de asistencia de cuadrillas con QR", valor=5,
        razon="App entregada con uso real desde el primer día; no expone datos del cliente.",
        li="""Pasar lista a una cuadrilla no debería tomar media mañana.

Entregamos una app de asistencia para un fundo de la región: el capataz escanea el QR del fotocheck al ingreso y a la salida, incluso sin señal en el campo.

El primer día registró 240 asistencias, listas para planilla sin cuadernos ni digitación.

¿Tu control de asistencia sigue en papel? Conversemos.""",
        fb="Nueva app de asistencia para cuadrillas: escaneo de QR al ingreso y salida, funciona sin señal. 240 asistencias registradas el primer día.",
        ig="""📲 Asistencia de cuadrillas en segundos.
Escaneo de QR al ingreso y salida, sin señal. 240 asistencias el primer día.""",
        tt=[("Cuadrilla llegando al campo al amanecer", "¿Cuánto tarda pasar lista a tu cuadrilla?"),
            ("Celular escaneando un fotocheck", "Con esta app el capataz escanea el QR, incluso sin señal."),
            ("Resumen de asistencias en pantalla", "El primer día registró 240 asistencias.")],
        tit="Asistencia en segundos", bul=[("Escaneo de QR", "Ingreso y salida."),
                                           ("Funciona sin señal", "Sincroniza después."),
                                           ("Lista para planilla", "Sin digitación.")],
        dato="240 asistencias el primer día", cta="Conversemos",
        tags=["#Agroindustria", "#SoftwareAMedida", "#AppMóvil", "#TransformaciónDigital"],
        vis="Smartphone mockup scanning a QR badge in a crop field at sunrise, workers blurred in the background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw27", area="software", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="permisos-trabajo",
        det="Sistema de permisos de trabajo digital para {cliente}: el supervisor aprueba desde la tablet con lista de verificación y firma, y reemplaza los formatos en papel en 3 frentes de trabajo.",
        fuente="Permisos de trabajo digitales", valor=5,
        razon="Sistema entregado con impacto claro en seguridad y orden; sin datos del cliente.",
        li="""Un permiso de trabajo en papel se moja, se pierde o llega tarde.

Entregamos un sistema de permisos de trabajo digital para una operación minera. El supervisor revisa la lista de verificación y firma desde la tablet, en el mismo frente de trabajo.

Ya reemplazó los formatos en papel en 3 frentes.

Seguridad con trazabilidad, sin esperar al fin del turno. ¿Te interesa para tu operación? Conversemos.""",
        fb="Permisos de trabajo digitales para una operación minera: lista de verificación y firma desde la tablet, ya en 3 frentes de trabajo.",
        ig="""📋 Permisos de trabajo sin papel.
Lista de verificación y firma desde la tablet, en el mismo frente de trabajo.""",
        tt=[("Formato de papel arrugado", "¿Tus permisos de trabajo todavía son de papel?"),
            ("Supervisor con tablet, sin rostro", "Ahora se revisan y firman desde la tablet."),
            ("Tablero con permisos aprobados", "Ya funciona en 3 frentes de trabajo.")],
        tit="Permisos de trabajo sin papel", bul=[("Lista de verificación", "Paso a paso en la tablet."),
                                                  ("Firma digital", "En el mismo frente."),
                                                  ("Trazabilidad completa", "Cada permiso registrado.")],
        dato=None, cta="Conversemos",
        tags=["#Minería", "#SeguridadIndustrial", "#SoftwareAMedida", "#TransformaciónDigital"],
        vis="Tablet mockup showing a digital work permit checklist with a signature field, mining site in the background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw28", area="software", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="ordenes-produccion",
        det="Sistema de órdenes de producción para {cliente}: cada orden indica modelo, tallas y etapa, y el taller pasó de la pizarra a una pantalla por área. Se cargaron 85 órdenes en la primera semana.",
        fuente="Sistema de órdenes de producción para calzado", valor=5,
        razon="Sistema entregado con uso real; se cuenta sin nombrar al taller.",
        li="""De la pizarra a la pantalla: así se organiza ahora un taller de calzado.

Entregamos un sistema de órdenes de producción para una fábrica de calzado. Cada orden indica modelo, tallas y etapa, y cada área ve en su pantalla lo que le toca.

En la primera semana se cargaron 85 órdenes.

Menos preguntas de pasillo, más pares saliendo a tiempo. ¿Tu taller sigue con pizarra? Cuéntanos tu caso.""",
        fb="Sistema de órdenes de producción para calzado: modelo, tallas y etapa en una pantalla por área. 85 órdenes en la primera semana.",
        ig="""👞 Tu taller, ordenado.
Cada orden con modelo, tallas y etapa en una pantalla por área. 85 órdenes en la primera semana.""",
        tt=[("Pizarra llena de pedidos", "¿Tu taller todavía se organiza en una pizarra?"),
            ("Pantalla con órdenes por etapa", "Ahora cada área ve en pantalla lo que le toca."),
            ("Pares terminados en la faja", "85 órdenes cargadas en la primera semana.")],
        tit="De la pizarra a la pantalla", bul=[("Modelo y tallas", "Cada orden completa."),
                                                ("Etapa visible", "Una pantalla por área."),
                                                ("Menos preguntas", "Más pares a tiempo.")],
        dato="85 órdenes en la primera semana", cta="Cuéntanos tu caso",
        tags=["#Calzado", "#SoftwareAMedida", "#Producción", "#TransformaciónDigital"],
        vis="Wall-mounted screen in a shoe workshop showing production orders by stage, leather pieces on tables",
    ),
    dict(
        id="sw29", area="software", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/inventario",
        det="Despliegue del módulo de inventario de equipos en el ERP: cada laptop y herramienta tiene un código QR, un responsable y su fecha de mantenimiento. Se registraron 64 equipos.",
        fuente="Módulo de inventario de equipos en el ERP", valor=4,
        razon="Módulo propio terminado; muestra capacidad de desarrollo sin datos sensibles.",
        li="""¿Quién tiene la laptop del laboratorio? En nuestro ERP ya no hace falta preguntarlo.

Desplegamos el módulo de inventario de equipos: cada laptop y herramienta tiene un código QR, un responsable y su fecha de mantenimiento.

Ya registramos 64 equipos del equipo y del laboratorio.

Lo que construimos para nosotros también lo podemos construir para tu empresa. Conversemos.""",
        fb="Nuevo módulo de inventario en nuestro ERP: QR, responsable y fecha de mantenimiento para cada equipo. 64 equipos registrados.",
        ig="""🏷️ Cada equipo con su QR.
Responsable y fecha de mantenimiento a un escaneo. 64 equipos ya registrados en nuestro ERP.""",
        tt=[("Laptop con etiqueta QR", "¿Quién tiene esta laptop?"),
            ("Celular escaneando el QR", "Con un escaneo ves el responsable y el mantenimiento."),
            ("Lista de equipos en el ERP", "Ya registramos 64 equipos.")],
        tit="Cada equipo con su QR", bul=[("Código QR", "Identificación rápida."),
                                          ("Responsable asignado", "Siempre se sabe quién."),
                                          ("Mantenimiento programado", "Fechas a la vista.")],
        dato="64 equipos registrados", cta="Conversemos",
        tags=["#ERP", "#SoftwareAMedida", "#Inventario", "#TransformaciónDigital"],
        vis="Laptop with a QR sticker next to a smartphone showing an equipment detail screen, tidy office desk",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw30", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se escribió un artículo para redes: 5 preguntas para decidir entre una app móvil y una página web antes de pedir un desarrollo",
        fuente="App móvil o página web: cómo decidir", valor=3,
        razon="Contenido educativo para potenciales clientes; no revela información interna.",
        li="""¿App móvil o página web? Antes de decidir, responde estas 5 preguntas.

1. ¿Tus usuarios lo usarán todos los días o de vez en cuando?
2. ¿Necesitas cámara, GPS o funcionar sin internet?
3. ¿Te encontrarán desde Google?
4. ¿Cuánto presupuesto tienes para mantener dos versiones?
5. ¿Quieres lanzar rápido y probar la idea?

Muchas veces una web bien hecha es el primer paso correcto. ¿Te ayudamos a decidir? Escríbenos.""",
        fb="¿App o web? Piensa en la frecuencia de uso, si necesitas cámara o trabajar sin internet, cómo te encontrarán y cuánto podrás mantener.",
        ig="""📱 ¿App o web? 5 preguntas para decidir.
Frecuencia de uso, cámara o sin internet, Google, mantenimiento y rapidez.""",
        tt=[("Celular y laptop lado a lado", "¿App móvil o página web?"),
            ("Persona usando el celular en campo", "Si necesitas cámara o trabajar sin internet, piensa en una app."),
            ("Buscador en pantalla", "Si quieres que te encuentren en Google, empieza por la web.")],
        tit="¿App móvil o página web?", bul=[("Frecuencia de uso", "Diario o eventual."),
                                             ("Funciones del celular", "Cámara, GPS, sin internet."),
                                             ("Presupuesto de mantenimiento", "Una o dos versiones.")],
        dato=None, cta="Escríbenos",
        tags=["#DesarrolloWeb", "#AppMóvil", "#Tips", "#Mypes"],
        vis="3D illustration of a smartphone and a browser window on a balance scale, minimal clean background",
    ),
    dict(
        id="sw31", area="software", sector="educación", tipo="interno", pilar="hito",
        sec="matriz", mod="corall-app/metricas",
        det="El ERP de CorAll cumplió 6 meses en uso diario: 1200 tickets atendidos y 300 oportunidades comerciales registradas desde su lanzamiento interno.",
        fuente="Seis meses del ERP interno", valor=4,
        razon="Hito propio con cifras de uso; no expone datos de clientes.",
        li="""6 meses usando el ERP que construimos para nosotros mismos.

Desde que lo lanzamos, el equipo atendió 1200 tickets y registró 300 oportunidades comerciales en una sola plataforma.

Usarlo todos los días nos obliga a mejorarlo todas las semanas.

Esa experiencia es la que llevamos a los sistemas que hacemos para nuestros clientes.""",
        fb="Nuestro ERP interno cumplió 6 meses: 1200 tickets atendidos y 300 oportunidades comerciales registradas.",
        ig="""🎂 6 meses de nuestro ERP.
1200 tickets atendidos y 300 oportunidades comerciales en una sola plataforma.""",
        tt=[("Pantalla del ERP en la oficina", "Hace 6 meses lanzamos nuestro propio ERP."),
            ("Contador de tickets", "Desde entonces atendimos 1200 tickets."),
            ("Equipo trabajando, sin rostros", "Y registramos 300 oportunidades comerciales.")],
        tit="6 meses de nuestro ERP", bul=[("Tickets atendidos", "Soporte en un solo lugar."),
                                           ("Oportunidades registradas", "Ventas ordenadas."),
                                           ("Mejora semanal", "Lo usamos a diario.")],
        dato="1200 tickets y 300 oportunidades", cta="Conoce más",
        tags=["#ERP", "#SoftwareAMedida", "#HechoEnTrujillo", "#TransformaciónDigital"],
        vis="Laptop mockup of an ERP dashboard with milestone counters and a small celebration accent in brand red",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw32", area="software", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller gratuito 'Ordena tu inventario en una hoja de cálculo' para mypes: miércoles 9 de diciembre, 18:30, en las oficinas de CorAll en Trujillo",
        fuente="Taller de inventario para mypes", valor=4,
        razon="Evento propio confirmado con fecha, hora y lugar.",
        li="""¿Tu inventario vive en un cuaderno o en la memoria de alguien?

Te invitamos al taller gratuito "Ordena tu inventario en una hoja de cálculo", pensado para mypes.

📅 Miércoles 9 de diciembre
🕡 18:30
📍 Oficinas de CorAll, Trujillo

Trae tu laptop y sal con tu plantilla lista. Inscríbete por mensaje directo.""",
        fb="Taller gratuito para mypes 'Ordena tu inventario en una hoja de cálculo': miércoles 9 de diciembre, 18:30, en nuestras oficinas de Trujillo.",
        ig="""📦 Ordena tu inventario.
Taller gratuito para mypes: miércoles 9 de diciembre, 18:30, en nuestras oficinas de Trujillo.""",
        tt=[("Cuaderno de inventario desordenado", "¿Tu inventario está en un cuaderno?"),
            ("Hoja de cálculo ordenada", "Te enseñamos a ordenarlo en una hoja de cálculo."),
            ("Fecha en pantalla", "Miércoles 9 de diciembre, 18:30, gratis.")],
        tit="Ordena tu inventario", bul=[("Miércoles 9 de diciembre", "A las 18:30."),
                                         ("Gratuito", "Para mypes."),
                                         ("Trae tu laptop", "Sal con tu plantilla.")],
        dato="Miércoles 9 de diciembre, 18:30", cta="Inscríbete",
        tags=["#Mypes", "#Inventario", "#TallerGratuito", "#Trujillo"],
        vis="Small shop storage shelves with labeled boxes and a laptop showing a clean spreadsheet, warm light",
    ),
    dict(
        id="sw33", area="software", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Primer día de revisión de código en parejas: 8 practicantes trabajaron junto a desarrolladores con más experiencia; fotos del equipo con autorización",
        fuente="Día de revisión de código en parejas", valor=3,
        razon="Actividad de cultura interna con fotos autorizadas.",
        li="""Revisar código en pareja es una de las formas más rápidas de aprender.

Esta semana tuvimos nuestro primer día de revisión de código en parejas: 8 practicantes trabajaron junto a desarrolladores con más experiencia.

Se preguntó todo, se explicó cada decisión y se aprendió en las dos direcciones.

Así crece el equipo de CorAll.""",
        fb="Primer día de revisión de código en parejas: 8 practicantes junto a desarrolladores con más experiencia.",
        ig="""👩‍💻 Aprender en pareja.
8 practicantes revisaron código junto a desarrolladores con más experiencia.""",
        tt=[("Dos laptops lado a lado", "¿Cómo aprende un practicante en CorAll?"),
            ("Código en pantalla con comentarios", "Revisando código en pareja con alguien con más experiencia."),
            ("Equipo trabajando", "Y aprendiendo en las dos direcciones.")],
        tit="Aprender en pareja", bul=[("Revisión en parejas", "Código explicado."),
                                       ("Practicantes y seniors", "Juntos en la mesa."),
                                       ("Aprendizaje mutuo", "En las dos direcciones.")],
        dato=None, cta="Conoce más",
        tags=["#CulturaCorAll", "#Practicantes", "#DesarrolloDeSoftware", "#Aprendizaje"],
        vis="Pairs of people working together at laptops, seen from behind, with a soft red overlay band at the bottom",
        adj="equipo",
    ),
    dict(
        id="sw34", area="software", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Capacitación presencial en el uso de la app de despachos a 14 conductores de {cliente} en su base; el cliente autorizó publicar el trabajo sin su nombre",
        fuente="Capacitación de conductores en la app de despachos", valor=4,
        razon="Servicio en sitio autorizado por el cliente, sin identificarlo.",
        li="""Una app solo funciona si quien la usa se siente cómodo con ella.

Esta semana capacitamos en persona a 14 conductores de un cliente de transporte en el uso de la app de despachos: registrar la entrega con foto y firma, y qué hacer cuando no hay señal.

Resolvimos dudas en la misma base, con los celulares de cada uno.

Entregar software también es acompañar a quien lo usa.""",
        fb="Capacitamos en persona a 14 conductores en el uso de la app de despachos, directamente en su base.",
        ig="""🚚 Capacitación en la base.
14 conductores aprendieron a usar la app de despachos con sus propios celulares.""",
        tt=[("Conductores en la base, sin rostros", "Capacitamos a 14 conductores en su base."),
            ("Celular con la app de despachos", "Registrar la entrega con foto y firma."),
            ("Camiones saliendo", "Y qué hacer cuando no hay señal.")],
        tit="Capacitación en la base", bul=[("Catorce conductores", "Capacitados en persona."),
                                            ("Con sus celulares", "Práctica real."),
                                            ("Dudas resueltas", "En la misma base.")],
        dato="14 conductores capacitados", cta="Conversemos",
        tags=["#Logística", "#Capacitación", "#AppMóvil", "#SoftwareAMedida"],
        vis="Truck depot with a group of drivers seen from behind holding smartphones, morning light, no faces",
    ),
    dict(
        id="sw35", area="software", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="pensiones-colegio",
        det="Sistema de pagos de pensiones con recordatorios por correo para {cliente}: los padres ven su estado de cuenta y descargan su comprobante; la morosidad de octubre bajó de 18 % a 11 %. El colegio autorizó compartir el resultado sin su nombre.",
        fuente="Sistema de pensiones con recordatorios", valor=5,
        razon="Resultado medible autorizado por el cliente; se publica sin nombrarlo.",
        li="""Recordar a tiempo también es un servicio.

Entregamos a un colegio un sistema de pensiones: los padres ven su estado de cuenta, descargan su comprobante y reciben recordatorios por correo antes del vencimiento.

En el primer mes, la morosidad bajó de 18 % a 11 %.

Menos llamadas de cobranza y más tiempo para lo importante. ¿Tu institución necesita algo parecido? Conversemos.""",
        fb="Sistema de pensiones para un colegio: estado de cuenta, comprobantes y recordatorios por correo. La morosidad bajó de 18 % a 11 % en el primer mes.",
        ig="""🏫 Pensiones al día.
Estado de cuenta, comprobantes y recordatorios por correo. Morosidad de 18 % a 11 % en un mes.""",
        tt=[("Padre revisando el celular", "¿Y si el colegio te recordara la pensión a tiempo?"),
            ("Pantalla con estado de cuenta", "Los padres ven su estado de cuenta y descargan su comprobante."),
            ("Gráfico de morosidad bajando", "En el primer mes la morosidad bajó de 18 % a 11 %.")],
        tit="Pensiones al día", bul=[("Estado de cuenta", "Siempre disponible."),
                                     ("Recordatorios por correo", "Antes del vencimiento."),
                                     ("Comprobante descargable", "Sin ir al colegio.")],
        dato="Morosidad de 18 % a 11 %", cta="Conversemos",
        tags=["#Educación", "#SoftwareAMedida", "#GestiónEscolar", "#TransformaciónDigital"],
        vis="Smartphone mockup showing a school payment status screen with a green paid badge, school notebook in background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw36", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó un post explicativo: diferencia entre hosting compartido, servidor en la nube y servidor propio, con cuándo conviene cada uno a una mype",
        fuente="Hosting compartido, nube o servidor propio", valor=3,
        razon="Contenido educativo para clientes; no menciona la infraestructura de CorAll.",
        li="""¿Dónde debería vivir tu sistema? Tres opciones explicadas sin tecnicismos.

🏠 Hosting compartido: económico y simple, ideal para una web informativa.
☁️ Servidor en la nube: crece contigo y pagas por lo que usas; bueno para tiendas y sistemas.
🖥️ Servidor propio: control total, pero tú te encargas de energía, respaldos y mantenimiento.

Para la mayoría de mypes, la nube suele ser el equilibrio más razonable entre costo y tranquilidad. ¿Dudas? Escríbenos.""",
        fb="Hosting compartido, nube o servidor propio: qué conviene a tu mype según lo que vas a publicar y cuánto puedes mantener.",
        ig="""☁️ ¿Dónde vive tu sistema?
Hosting compartido, nube o servidor propio: te explicamos cuándo conviene cada uno.""",
        tt=[("Fila de servidores", "¿Dónde debería vivir tu sistema?"),
            ("Ícono de nube sobre una laptop", "La nube crece contigo y pagas por lo que usas."),
            ("Servidor en una oficina", "Un servidor propio te da control, pero también trabajo.")],
        tit="¿Dónde vive tu sistema?", bul=[("Hosting compartido", "Para webs simples."),
                                            ("Nube", "Crece contigo."),
                                            ("Servidor propio", "Control y trabajo.")],
        dato=None, cta="Escríbenos",
        tags=["#Nube", "#DesarrolloWeb", "#Mypes", "#Tips"],
        vis="3D illustration of a small house, a cloud and a server tower side by side on a clean surface, minimal style",
    ),
    dict(
        id="sw37", area="software", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se preparó la ficha comercial de los planes de soporte: básico, estándar y prioritario, con tiempos de primera respuesta de 24, 8 y 4 horas hábiles",
        fuente="Ficha de planes de soporte", valor=4,
        razon="Catálogo propio de servicios; información comercial pública.",
        li="""Tu sistema necesita alguien que responda cuando lo necesitas.

Estos son nuestros planes de soporte:

🟢 Básico: primera respuesta en 24 horas hábiles.
🟡 Estándar: primera respuesta en 8 horas hábiles.
🔴 Prioritario: primera respuesta en 4 horas hábiles.

Todos con atención desde Trujillo y seguimiento por ticket. ¿Cuál se ajusta a tu operación? Escríbenos.""",
        fb="Planes de soporte CorAll: básico (24 horas hábiles), estándar (8 horas hábiles) y prioritario (4 horas hábiles) de primera respuesta.",
        ig="""🛟 Soporte a tu medida.
Básico, estándar o prioritario: primera respuesta en 24, 8 o 4 horas hábiles.""",
        tt=[("Persona frente a una laptop con un problema", "¿Quién te responde cuando tu sistema falla?"),
            ("Tres tarjetas de planes", "Tenemos tres planes de soporte."),
            ("Equipo de soporte, sin rostros", "Con respuesta desde 4 horas hábiles.")],
        tit="Soporte a tu medida", bul=[("Plan básico", "Respuesta en un día."),
                                        ("Plan estándar", "Respuesta en la jornada."),
                                        ("Plan prioritario", "Respuesta más rápida.")],
        dato=None, cta="Escríbenos",
        tags=["#Soporte", "#SoftwareAMedida", "#Mypes", "#Trujillo"],
        vis="Grid of three clean plan cards with simple support line icons in green, yellow and red accents on white",
        comp="grilla",
    ),
    dict(
        id="sw38", area="software", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="seguimiento-envios",
        det="Portal de seguimiento de envíos para {cliente}: el destinatario ingresa su número de guía y ve el estado y la foto de entrega. Tuvo 1500 consultas en la primera semana.",
        fuente="Portal de seguimiento de envíos", valor=5,
        razon="Producto entregado con uso medible; no identifica al cliente.",
        li=""""¿Dónde está mi envío?" es la pregunta que más llamadas genera.

Entregamos un portal de seguimiento para una empresa de transporte: el destinatario ingresa su número de guía y ve el estado del envío y la foto de entrega.

En la primera semana recibió 1500 consultas que antes habrían sido llamadas.

¿Tu equipo pasa el día respondiendo dónde está cada envío? Conversemos.""",
        fb="Portal de seguimiento de envíos: el destinatario ve el estado y la foto de entrega con su número de guía. 1500 consultas en la primera semana.",
        ig="""📦 ¿Dónde está mi envío?
Con el número de guía se ve el estado y la foto de entrega. 1500 consultas en la primera semana.""",
        tt=[("Teléfono sonando en una oficina", "¿Cuántas veces te preguntan dónde está un envío?"),
            ("Pantalla del portal con estados", "Con este portal, el destinatario lo ve solo con su guía."),
            ("Foto de entrega en pantalla", "1500 consultas en la primera semana.")],
        tit="¿Dónde está mi envío?", bul=[("Número de guía", "Consulta directa."),
                                          ("Estado en línea", "Etapa por etapa."),
                                          ("Foto de entrega", "Prueba visual.")],
        dato="1500 consultas en la primera semana", cta="Conversemos",
        tags=["#Logística", "#SoftwareAMedida", "#ExperienciaDelCliente", "#TransformaciónDigital"],
        vis="Laptop and phone mockups showing a shipment tracking page with a delivery photo, parcels in background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw39", area="software", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Cierre de la primera campaña completa con la app de cosecha de {cliente}: el cliente autorizó compartir sin su nombre que se registraron 52 000 jabas sin planillas de papel",
        fuente="Primera campaña completa con la app de cosecha", valor=5,
        razon="Hito autorizado por el cliente con una cifra clara.",
        li="""Una campaña completa sin planillas de papel.

Cerramos la primera campaña de cosecha con nuestra app en un fundo de la región: se registraron 52 000 jabas por lote, desde el celular de cada cuadrilla.

Los datos del día llegaban al ingeniero el mismo día, no a fin de semana.

Gracias al equipo de campo por adoptarla. Vamos por la siguiente campaña.""",
        fb="Primera campaña completa con nuestra app de cosecha: 52 000 jabas registradas sin planillas de papel.",
        ig="""🍇 Una campaña sin papel.
52 000 jabas registradas por lote desde el celular de cada cuadrilla.""",
        tt=[("Jabas apiladas en campo", "Una campaña entera sin planillas de papel."),
            ("Celular registrando una jaba", "Cada cuadrilla registró sus jabas desde el celular."),
            ("Contador en pantalla", "52 000 jabas en total.")],
        tit="Una campaña sin papel", bul=[("Registro por lote", "Desde el celular."),
                                          ("Datos del día", "Al ingeniero, a tiempo."),
                                          ("Campaña completa", "Sin planillas.")],
        dato="52 000 jabas registradas", cta="Conoce más",
        tags=["#Agroindustria", "#Cosecha", "#AppMóvil", "#TransformaciónDigital"],
        vis="Stacks of harvest crates in a vineyard at sunset with a smartphone in the foreground showing a counter",
    ),
    dict(
        id="sw40", area="software", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="CorAll participará como mentor en el hackatón universitario 'Código Norte' el 28 y 29 de noviembre; la organización confirmó la participación y el nombre del evento es público",
        fuente="Mentoría en un hackatón universitario", valor=4,
        razon="Evento público confirmado con fechas.",
        li="""Este 28 y 29 de noviembre estaremos en el hackatón universitario "Código Norte".

Nuestro equipo participará como mentor: acompañaremos a los grupos a convertir una idea en un prototipo funcional en dos días.

Si participas, búscanos. Si eres estudiante y te interesa el desarrollo de software, este es un gran lugar para empezar.

Nos vemos en "Código Norte".""",
        fb="Estaremos como mentores en el hackatón universitario 'Código Norte', el 28 y 29 de noviembre.",
        ig="""💻 Nos vemos en "Código Norte".
Seremos mentores en el hackatón universitario, el 28 y 29 de noviembre.""",
        tt=[("Laptops y café sobre una mesa", "¿Vas al hackatón Código Norte?"),
            ("Pizarra con ideas", "Estaremos como mentores ayudando a los equipos."),
            ("Fecha en pantalla", "28 y 29 de noviembre. Búscanos.")],
        tit="Mentores en Código Norte", bul=[("Dos días de hackatón", "28 y 29 de noviembre."),
                                             ("Mentoría", "Idea a prototipo."),
                                             ("Para estudiantes", "Desarrollo de software.")],
        dato="28 y 29 de noviembre", cta="Agenda la fecha",
        tags=["#Hackatón", "#Estudiantes", "#DesarrolloDeSoftware", "#Trujillo"],
        vis="Hackathon room with laptops, sticky notes and coffee cups on long tables, energetic light, no faces",
    ),
]
