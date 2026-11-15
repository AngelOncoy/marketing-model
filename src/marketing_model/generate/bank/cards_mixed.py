"""Publishable tasks that balance the less frequent pillars and security-as-advice cases."""

CARDS = [
    # ---- seguridad convertida en consejo general (el reporte trae detalles que no se publican) ----
    dict(
        id="mx01", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="tienda-online/backend", riesgo=3,
        det="Se reemplazó el envío de la clave del webhook en la URL (/webhooks/pagos?key=...) por una firma HMAC en la cabecera y se rotaron las claves en el gestor de secretos.",
        fuente="Mejora en la integración de pagos", valor=3,
        razon="Solo se publica como consejo general sobre integraciones seguras, sin rutas ni detalles del cambio.",
        li="""Las claves de tus integraciones no deberían viajar a la vista.

Cuando conectas tu sistema con pagos, mensajería o cualquier servicio externo, estas prácticas reducen riesgos:

1. Nunca pongas claves en la dirección web: viajan y quedan guardadas en muchos lugares.
2. Verifica que cada mensaje venga de quien dice venir, con firmas digitales.
3. Cambia tus claves de forma periódica y guárdalas en un gestor de secretos.

¿Tus integraciones cumplen con estas tres? Si no estás seguro, conversemos.""",
        fb="3 prácticas para integraciones seguras: claves fuera de la dirección web, mensajes firmados y claves que se cambian periódicamente.",
        ig="""🔐 Integraciones seguras en 3 pasos.
Claves fuera de la dirección web, mensajes firmados y claves que se renuevan cada cierto tiempo.""",
        tt=[("Dirección web con texto borroso", "¿Tus claves viajan a la vista en una dirección web?"),
            ("Sobre con un sello", "Usa firmas para verificar cada mensaje."),
            ("Llave girando en una caja fuerte", "Y renueva tus claves en un gestor de secretos.")],
        tit="Integraciones seguras", bul=[("Claves ocultas", "Fuera de la dirección web."),
                                          ("Mensajes firmados", "Verifica el origen."),
                                          ("Claves renovadas", "Cada cierto tiempo.")],
        dato=None, cta="Conversemos",
        tags=["#Ciberseguridad", "#Integraciones", "#BuenasPrácticas", "#DesarrolloDeSoftware"],
        vis="3D illustration of a sealed envelope with a digital signature traveling between two servers",
    ),
    dict(
        id="mx02", area="hardware", sector="logística y transporte", tipo="interno", pilar="educativo",
        sec="matriz", mod="firmware-gateway", riesgo=3,
        det="Se cambió la contraseña por defecto admin/admin de los 12 gateways de campo, se cerró el puerto 23 y se activó la actualización de firmware firmada.",
        fuente="Endurecimiento de equipos de campo", valor=3,
        razon="Se publica solo como recomendación general para equipos IoT, sin mencionar qué equipos ni qué configuración tenían.",
        li="""Un equipo IoT con la contraseña de fábrica es una puerta abierta.

Si tienes sensores, cámaras o gateways conectados, revisa estas tres cosas hoy:

1. Cambia la contraseña que trae de fábrica, siempre.
2. Desactiva los servicios de acceso remoto que no uses.
3. Actualiza el firmware solo desde fuentes verificadas.

La seguridad de un equipo en campo se decide el día de la instalación. ¿Necesitas revisar los tuyos? Conversemos.""",
        fb="3 claves para proteger tus equipos IoT: cambia la contraseña de fábrica, desactiva accesos que no usas y actualiza solo desde fuentes verificadas.",
        ig="""🛡️ ¿Tu equipo IoT tiene la contraseña de fábrica?
Cámbiala, desactiva accesos que no usas y actualiza solo desde fuentes verificadas.""",
        tt=[("Etiqueta de un equipo con contraseña de fábrica", "¿Tus equipos siguen con la contraseña de fábrica?"),
            ("Interruptores apagándose", "Cámbiala y desactiva los accesos que no usas."),
            ("Barra de actualización con check", "Y actualiza solo desde fuentes verificadas.")],
        tit="Protege tus equipos IoT", bul=[("Cambia la contraseña", "La de fábrica, siempre."),
                                            ("Cierra accesos", "Los que no uses."),
                                            ("Firmware verificado", "De fuentes seguras.")],
        dato=None, cta="Conversemos",
        tags=["#Ciberseguridad", "#IoT", "#BuenasPrácticas", "#SeguridadIndustrial"],
        vis="3D illustration of a small IoT gateway with a padlock and a shield, dark circuit background",
    ),
    dict(
        id="mx03", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="asistente-erp", riesgo=3,
        det="Se agregaron defensas contra inyección de instrucciones en el asistente: separación del contenido del usuario, lista de herramientas permitidas y revisión humana para acciones que modifican datos (corrige hallazgo del issue de seguridad).",
        fuente="Defensas del asistente ante instrucciones maliciosas", valor=3,
        razon="Se publica como buena práctica general de IA, sin describir el hallazgo ni el sistema afectado.",
        li="""Si tu asistente de IA puede actuar, alguien intentará engañarlo.

Cuando un asistente lee correos, documentos o páginas web, ese contenido puede traer instrucciones escondidas. Tres prácticas que recomendamos:

1. Trata el contenido externo como datos, nunca como órdenes.
2. Limita las herramientas que el asistente puede usar.
3. Pide aprobación humana antes de cualquier acción que cambie datos.

La IA es útil cuando sus límites están bien definidos. ¿Cómo protegen tus asistentes?""",
        fb="Si tu asistente de IA puede actuar, protégelo: contenido externo como datos, herramientas limitadas y aprobación humana para cambios.",
        ig="""🤖 ¿Tu asistente de IA se deja engañar?
Contenido externo como datos, herramientas limitadas y aprobación humana para cualquier cambio.""",
        tt=[("Documento con texto oculto resaltado", "Un documento puede traer instrucciones escondidas para tu IA."),
            ("Caja de herramientas con pocas piezas", "Limita lo que tu asistente puede hacer."),
            ("Botón de aprobación humana", "Y aprueba tú cada acción que cambie datos.")],
        tit="Una IA con límites claros", bul=[("Contenido como datos", "Nunca como órdenes."),
                                              ("Pocas herramientas", "Solo las necesarias."),
                                              ("Aprobación humana", "Para cada cambio.")],
        dato=None, cta="Cuéntanos",
        tags=["#IAResponsable", "#Ciberseguridad", "#InteligenciaArtificial", "#BuenasPrácticas"],
        vis="3D illustration of a robot assistant behind a transparent filter separating documents from commands",
    ),
    dict(
        id="mx04", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="corall-app/rrhh", riesgo=3,
        det="Se restringió la vista de sueldos en el módulo de RR. HH. al rol planilla (tabla rrhh_sueldos), con registro de cada consulta; antes la veían todos los jefes de área.",
        fuente="Restricción de acceso a información salarial", valor=3,
        razon="Se publica como consejo general de privacidad, sin revelar cómo estaba configurado el sistema.",
        li="""No todos los jefes necesitan ver todos los sueldos.

La información salarial es de las más sensibles de una empresa. Tres prácticas para protegerla en tus sistemas:

1. Acceso solo para quien lo necesita por su función.
2. Registro de cada consulta: quién vio qué y cuándo.
3. Revisión periódica de los permisos, porque los roles cambian.

Proteger los datos del equipo también es cuidar la confianza. ¿Cuándo revisaste los permisos de tus sistemas?""",
        fb="La información salarial merece acceso restringido: solo quien lo necesita, registro de cada consulta y revisión periódica de permisos.",
        ig="""🔒 Datos del equipo, bien protegidos.
Acceso solo por función, registro de cada consulta y revisión periódica de permisos.""",
        tt=[("Carpeta con etiqueta confidencial", "¿Quién puede ver los sueldos en tu empresa?"),
            ("Llave entregándose a una sola persona", "Solo quien lo necesita por su función."),
            ("Registro de accesos en pantalla", "Y registra cada consulta.")],
        tit="Datos del equipo, protegidos", bul=[("Acceso por función", "Solo quien lo necesita."),
                                                 ("Registro de consultas", "Quién, qué y cuándo."),
                                                 ("Revisión periódica", "Los roles cambian.")],
        dato=None, cta="Conversemos",
        tags=["#ProtecciónDeDatos", "#RecursosHumanos", "#Ciberseguridad", "#BuenasPrácticas"],
        vis="3D illustration of a confidential folder inside a glass vault with a single key",
    ),
    # ---- catálogo ----
    dict(
        id="mx05", area="software", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se terminó la ficha comercial de los módulos del ERP para mypes: recursos humanos, CRM, tickets de soporte y propuestas de marketing, cada uno con capturas de pantalla anonimizadas",
        fuente="Ficha comercial de los módulos del ERP", valor=4,
        razon="Catálogo de producto propio terminado; contenido comercial sin riesgos.",
        li="""Un ERP pensado para cómo trabaja una mype peruana.

Estos son los módulos de nuestro ERP, que hoy usamos en nuestro propio equipo:

- Recursos humanos: personal, vacaciones y solicitudes.
- CRM: oportunidades y seguimiento comercial.
- Tickets de soporte: cada caso con estado y tiempo.
- Propuestas de marketing: ideas de contenido con revisión humana.

Empiezas con el módulo que más necesitas y sumas los demás cuando quieras. ¿Cuál sería el primero para ti?""",
        fb="Nuestro ERP para mypes: recursos humanos, CRM, tickets de soporte y propuestas de marketing. Empieza por el módulo que más necesites.",
        ig="""🧩 Un ERP a tu ritmo.
Recursos humanos, CRM, tickets y marketing. Empieza por el módulo que más necesitas.""",
        tt=[("Escritorio con hojas de cálculo", "¿Tu negocio vive en hojas de cálculo?"),
            ("Cuatro módulos apareciendo", "Nuestro ERP tiene recursos humanos, CRM, tickets y marketing."),
            ("Un módulo resaltado", "Empieza por el que más necesitas.")],
        tit="Un ERP a tu ritmo", bul=[("Recursos humanos", "Personal y solicitudes."),
                                      ("CRM y tickets", "Clientes y soporte."),
                                      ("Marketing", "Con revisión humana.")],
        dato=None, cta="Elige tu módulo",
        tags=["#ERP", "#Mypes", "#SoftwareAMedida", "#TransformaciónDigital"],
        vis="Grid of four app module cards on a laptop screen, clean light office desk",
        comp="grilla", vis_es="mockup de interfaz",
    ),
    dict(
        id="mx06", area="ia", sector="agroindustria", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se armó el catálogo de soluciones de inteligencia artificial: conteo y calibre por imagen, detección de plagas, predicción de demanda, lectura de documentos y asistentes de atención",
        fuente="Catálogo de soluciones de IA", valor=4,
        razon="Catálogo propio terminado; contenido comercial sin datos sensibles.",
        li="""Inteligencia artificial aplicada a problemas concretos, no a promesas.

Estas son las soluciones de IA que ya desarrollamos en proyectos reales:

- Conteo y calibre de fruta por imagen
- Detección de plagas en hojas
- Predicción de demanda
- Lectura automática de documentos
- Asistentes de atención con información oficial

Cada una empieza con un piloto corto para medir si funciona en tu operación. ¿Cuál te interesa?""",
        fb="Nuestras soluciones de IA: conteo y calibre por imagen, detección de plagas, predicción de demanda, lectura de documentos y asistentes de atención.",
        ig="""🧠 IA para problemas concretos.
Conteo y calibre por imagen, plagas, demanda, documentos y asistentes de atención.""",
        tt=[("Palabra IA con signo de pregunta", "¿Qué puede hacer la IA por tu empresa?"),
            ("Íconos de las cinco soluciones", "Contar fruta, detectar plagas, predecir demanda, leer documentos y atender consultas."),
            ("Piloto en campo", "Todo empieza con un piloto corto.")],
        tit="IA para problemas concretos", bul=[("Visión artificial", "Conteo, calibre y plagas."),
                                                ("Predicción", "Demanda semanal."),
                                                ("Documentos y atención", "Lectura y asistentes.")],
        dato=None, cta="Conversemos",
        tags=["#InteligenciaArtificial", "#VisiónArtificial", "#Innovación", "#IA"],
        vis="Grid of five clean line icons for vision, leaf, chart, document and chat over a soft gradient",
        comp="grilla",
    ),
    dict(
        id="mx07", area="hardware", sector="logística y transporte", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se completó el catálogo de soluciones para flotas: tracker GPS, sensores de temperatura para cadena de frío, botón de pánico y tablero de telemetría con alertas",
        fuente="Catálogo de soluciones para flotas", valor=4,
        razon="Catálogo propio terminado; contenido comercial sin riesgos.",
        li="""Todo lo que tu flota necesita para reportar, alertar y cuidarse.

Ordenamos nuestro catálogo de soluciones para flotas:

- Tracker GPS con autonomía configurable
- Sensores de temperatura para cadena de frío
- Botón de pánico con respaldo por SMS
- Tablero de telemetría con alertas

Hardware y plataforma diseñados por el mismo equipo, para que todo funcione junto. ¿Qué le falta a tu flota?""",
        fb="Soluciones para flotas: tracker GPS, sensores de cadena de frío, botón de pánico y tablero de telemetría con alertas. ¿Qué le falta a tu flota?",
        ig="""🚚 Soluciones para tu flota.
Tracker GPS, sensores de frío, botón de pánico y tablero de telemetría con alertas.""",
        tt=[("Camión en carretera", "¿Qué necesita tu flota?"),
            ("Cuatro equipos sobre una mesa", "Tracker GPS, sensores de frío, botón de pánico y tablero."),
            ("Tablero con alertas", "Todo diseñado para funcionar junto.")],
        tit="Soluciones para tu flota", bul=[("Tracker GPS", "Autonomía configurable."),
                                             ("Cadena de frío", "Sensores de temperatura."),
                                             ("Pánico y telemetría", "Alertas en tiempo real.")],
        dato=None, cta="Conversemos",
        tags=["#GestiónDeFlotas", "#Telemetría", "#Logística", "#IoT"],
        vis="Product lineup of a GPS tracker, a temperature sensor and a panic button in front of a truck",
        comp="grilla",
    ),
    dict(
        id="mx08", area="innovacion", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se definió la oferta de servicios de innovación: diagnóstico de madurez digital, talleres de co-diseño, acompañamiento en postulación a fondos y pilotos en campo",
        fuente="Oferta de servicios de innovación", valor=4,
        razon="Catálogo de servicios propio; contenido comercial sin riesgos.",
        li="""Innovar no siempre empieza con tecnología. A veces empieza con una buena pregunta.

Estos son nuestros servicios de innovación para empresas:

- Diagnóstico de madurez digital
- Talleres de co-diseño con tus usuarios
- Acompañamiento en la postulación a fondos
- Pilotos en campo antes de escalar

Te ayudamos a decidir qué hacer primero y a probarlo en pequeño. ¿Por dónde empezamos?""",
        fb="Servicios de innovación: diagnóstico digital, talleres de co-diseño, acompañamiento en fondos y pilotos en campo. ¿Por dónde empezamos?",
        ig="""🧭 Innovar empieza con una buena pregunta.
Diagnóstico digital, co-diseño, apoyo en fondos y pilotos en campo.""",
        tt=[("Signo de pregunta en una pizarra", "Innovar empieza con una buena pregunta."),
            ("Cuatro íconos de servicios", "Diagnóstico, co-diseño, fondos y pilotos en campo."),
            ("Pequeño piloto creciendo", "Te ayudamos a probar en pequeño antes de escalar.")],
        tit="Servicios de innovación", bul=[("Diagnóstico digital", "Por dónde empezar."),
                                            ("Co-diseño", "Con tus usuarios."),
                                            ("Fondos y pilotos", "Apoyo y prueba en campo.")],
        dato=None, cta="Conversemos",
        tags=["#Innovación", "#TransformaciónDigital", "#Mypes", "#PilotoEnCampo"],
        vis="Four connected circles with simple line icons on a white background with red geometric shapes",
        comp="grilla",
    ),
    dict(
        id="mx09", area="hardware", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se armó el catálogo de kits educativos: robótica básica, kit IoT con sensores y kit de estación de clima, cada uno con guía para docentes",
        fuente="Catálogo de kits educativos", valor=3,
        razon="Catálogo propio terminado para el sector educación.",
        li="""Tecnología que se aprende tocándola.

Presentamos nuestros kits educativos para colegios e institutos:

- Robótica básica
- Kit IoT con sensores
- Kit de estación de clima

Cada kit incluye una guía para docentes, para que puedan usarlo en clase desde el primer día. ¿Tu institución quiere uno? Escríbenos.""",
        fb="Kits educativos para colegios e institutos: robótica básica, IoT con sensores y estación de clima, con guía para docentes.",
        ig="""🎒 Aprender tocando.
Kits de robótica, IoT y estación de clima, con guía para docentes.""",
        tt=[("Manos abriendo una caja de kit", "La tecnología se aprende tocándola."),
            ("Los tres kits sobre una mesa", "Robótica, IoT con sensores y estación de clima."),
            ("Guía para docentes", "Con guía para usarlo desde la primera clase.")],
        tit="Aprender tocando", bul=[("Robótica básica", "Primeros pasos."),
                                     ("Kit IoT", "Sensores reales."),
                                     ("Estación de clima", "Ciencia aplicada.")],
        dato=None, cta="Escríbenos",
        tags=["#Educación", "#STEM", "#RobóticaEducativa", "#IoT"],
        vis="Three colorful educational electronics kits in open boxes on a classroom table",
        comp="grilla",
    ),
    # ---- eventos ----
    dict(
        id="mx10", area="software", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el webinar 'Vende por WhatsApp sin perder pedidos': jueves 10 de diciembre, 19:00, gratuito, transmisión por las redes de CorAll",
        fuente="Webinar sobre ventas por WhatsApp", valor=4,
        razon="Evento propio confirmado con fecha y canal.",
        li="""¿Vendes por WhatsApp y se te pierden pedidos entre los chats?

Te invitamos a nuestro webinar gratuito "Vende por WhatsApp sin perder pedidos", donde mostraremos cómo ordenar tus pedidos con herramientas simples.

📅 Jueves 10 de diciembre
🕖 19:00
📍 En vivo por nuestras redes

Ideal para mypes y emprendimientos. Te esperamos.""",
        fb="Webinar gratuito 'Vende por WhatsApp sin perder pedidos': jueves 10 de diciembre, 19:00, en vivo por nuestras redes.",
        ig="""📲 Vende por WhatsApp sin perder pedidos.
Webinar gratuito, jueves 10 de diciembre, 19:00, en vivo por nuestras redes.""",
        tt=[("Celular con muchos chats", "¿Se te pierden pedidos en WhatsApp?"),
            ("Pedidos ordenados en una lista", "Te enseñamos a ordenarlos con herramientas simples."),
            ("Fecha en pantalla", "Webinar gratuito, jueves 10 de diciembre, 19:00.")],
        tit="Vende sin perder pedidos", bul=[("Jueves 10 de diciembre", "A las 19:00."),
                                             ("Gratuito", "En vivo por redes."),
                                             ("Para mypes", "Y emprendimientos.")],
        dato="Jueves 10 de diciembre, 19:00", cta="Agenda la fecha",
        tags=["#WhatsApp", "#Ventas", "#Mypes", "#WebinarGratuito"],
        vis="Smartphone with chat bubbles transforming into an organized order list, red accents",
    ),
    dict(
        id="mx11", area="hardware", sector="agroindustria", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la demostración en campo de sensores para riego: viernes 11 de diciembre, 8:00 a 11:00, en un fundo aliado de Virú que autorizó el evento; cupo de 15 productores",
        fuente="Demostración de sensores de riego en campo", valor=4,
        razon="Evento confirmado con autorización del anfitrión; sin datos sensibles.",
        li="""Ver para creer: sensores de riego funcionando en un campo real.

Te invitamos a una demostración en campo, donde verás cómo los sensores de humedad de suelo y la estación de clima ayudan a decidir el riego.

📅 Viernes 11 de diciembre
🕗 8:00 a 11:00
📍 Fundo aliado en Virú
👥 15 cupos para productores

Inscripción previa en el enlace.""",
        fb="Demostración en campo de sensores para riego: viernes 11 de diciembre, 8:00 a 11:00, en un fundo de Virú. Solo 15 cupos para productores.",
        ig="""🌱 Sensores de riego, en campo.
Viernes 11 de diciembre, 8:00 a 11:00, en un fundo de Virú. 15 cupos para productores.""",
        tt=[("Campo regado al amanecer", "¿Quieres ver sensores de riego funcionando en un campo real?"),
            ("Sensor de suelo y estación de clima", "Te mostramos cómo ayudan a decidir el riego."),
            ("Fecha en pantalla", "Viernes 11 de diciembre, 8:00, en Virú. 15 cupos.")],
        tit="Sensores de riego en campo", bul=[("Viernes 11 de diciembre", "De 8:00 a 11:00."),
                                               ("Fundo en Virú", "Campo real."),
                                               ("15 cupos", "Para productores.")],
        dato="Viernes 11 de diciembre, 8:00", cta="Inscríbete",
        tags=["#AgriculturaDePrecisión", "#Riego", "#Agroindustria", "#Virú"],
        vis="Irrigated green field at sunrise with a soil sensor and a weather station in the foreground",
    ),
    dict(
        id="mx12", area="ia", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el bootcamp de introducción a visión artificial para estudiantes: 3 sábados de enero (10, 17 y 24), 9:00 a 13:00, en la sede de CorAll; 20 cupos con inscripción",
        fuente="Bootcamp de visión artificial", valor=4,
        razon="Evento confirmado con fechas, lugar y cupos.",
        li="""3 sábados para entrenar tu primer modelo de visión artificial.

Lanzamos nuestro bootcamp de introducción a la visión artificial para estudiantes. Aprenderás a tomar y etiquetar imágenes, entrenar un modelo y evaluarlo con datos reales.

📅 Sábados 10, 17 y 24 de enero
🕘 9:00 a 13:00
📍 Sede de CorAll, Trujillo
👥 20 cupos

Inscríbete en el enlace.""",
        fb="Bootcamp de visión artificial para estudiantes: sábados 10, 17 y 24 de enero, 9:00 a 13:00, sede de CorAll en Trujillo. 20 cupos.",
        ig="""📷 Tu primer modelo de visión artificial.
Sábados 10, 17 y 24 de enero, 9:00 a 13:00, en Trujillo. 20 cupos.""",
        tt=[("Laptop entrenando un modelo", "¿Quieres entrenar tu primer modelo de visión artificial?"),
            ("Fotos siendo etiquetadas", "Aprende a etiquetar, entrenar y evaluar con datos reales."),
            ("Fechas en pantalla", "Sábados 10, 17 y 24 de enero. 20 cupos.")],
        tit="Bootcamp de visión artificial", bul=[("3 sábados de enero", "10, 17 y 24."),
                                                  ("9:00 a 13:00", "En Trujillo."),
                                                  ("20 cupos", "Con inscripción.")],
        dato="Sábados 10, 17 y 24 de enero", cta="Inscríbete",
        tags=["#VisiónArtificial", "#Bootcamp", "#Estudiantes", "#InteligenciaArtificial"],
        vis="Laptop showing image annotation boxes on fruit photos, workshop table with notebooks",
    ),
    dict(
        id="mx13", area="innovacion", sector="cuero y calzado", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la mesa de trabajo 'Calzado 4.0' con fabricantes de El Porvenir: miércoles 9 de diciembre, 16:00 a 18:00, en un auditorio municipal que confirmó la reserva; ingreso libre con registro",
        fuente="Mesa de trabajo Calzado 4.0", valor=4,
        razon="Evento confirmado con fecha y lugar; dirigido al sector.",
        li="""¿Cómo se ve la Industria 4.0 en un taller de calzado de El Porvenir?

Te invitamos a la mesa de trabajo "Calzado 4.0", donde fabricantes y tecnólogos conversaremos sobre conteo de producción, control de calidad y pedidos digitales.

📅 Miércoles 9 de diciembre
🕓 16:00 a 18:00
📍 Auditorio municipal de El Porvenir

Ingreso libre con registro previo.""",
        fb="Mesa de trabajo 'Calzado 4.0' con fabricantes de El Porvenir: miércoles 9 de diciembre, 16:00 a 18:00. Ingreso libre con registro.",
        ig="""👞 Calzado 4.0.
Mesa de trabajo con fabricantes de El Porvenir, miércoles 9 de diciembre, 16:00. Ingreso libre con registro.""",
        tt=[("Taller de calzado tradicional", "¿Cómo se ve la Industria 4.0 en un taller de calzado?"),
            ("Contador de pares y tablet", "Hablemos de conteo, calidad y pedidos digitales."),
            ("Fecha en pantalla", "Miércoles 9 de diciembre, 16:00, en El Porvenir.")],
        tit="Calzado 4.0", bul=[("Miércoles 9 de diciembre", "De 16:00 a 18:00."),
                                ("El Porvenir", "Auditorio municipal."),
                                ("Ingreso libre", "Con registro.")],
        dato="Miércoles 9 de diciembre, 16:00", cta="Regístrate",
        tags=["#Calzado", "#Industria40", "#ElPorvenir", "#Innovación"],
        vis="Traditional shoe workshop table with leather pieces and a modern tablet, red geometric shapes",
    ),
    dict(
        id="mx14", area="innovacion", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Se realizó la charla 'Del problema al piloto' en una universidad de Trujillo para 60 estudiantes de ingeniería; la universidad autorizó publicar fotos generales del auditorio",
        fuente="Charla en una universidad", valor=3,
        razon="Evento realizado con autorización de fotos generales.",
        li="""60 estudiantes de ingeniería y una pregunta: ¿cómo se pasa de una idea a un piloto que funciona?

Esta semana compartimos la charla "Del problema al piloto" en una universidad de Trujillo. Hablamos de cómo definir un problema medible, probar en campo y decidir con datos.

Gracias por las preguntas y por el interés. Nos vemos en el próximo encuentro.""",
        fb="Gracias a los 60 estudiantes de ingeniería que nos acompañaron en la charla 'Del problema al piloto'. Nos vemos pronto.",
        ig="""🎓 Del problema al piloto.
Compartimos nuestra forma de trabajar con 60 estudiantes de ingeniería en Trujillo. ¡Gracias!""",
        tt=[("Auditorio lleno visto desde atrás", "60 estudiantes de ingeniería."),
            ("Diapositiva 'del problema al piloto'", "Hablamos de cómo pasar de una idea a un piloto."),
            ("Aplausos con overlay rojo", "Gracias por las preguntas. Nos vemos pronto.")],
        tit="Del problema al piloto", bul=[("60 estudiantes", "De ingeniería."),
                                           ("Problema medible", "Punto de partida."),
                                           ("Piloto en campo", "Decidir con datos.")],
        dato="60 estudiantes de ingeniería", cta="Conoce más",
        tags=["#Universidad", "#Innovación", "#Ingeniería", "#Trujillo"],
        vis="University auditorium seen from the back row with a projector screen, no faces visible",
        adj="campo",
    ),
    # ---- cultura ----
    dict(
        id="mx15", area="software", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Una practicante de desarrollo fue contratada a tiempo completo al terminar sus prácticas; autorizó publicar el logro sin su foto",
        fuente="Practicante contratada a tiempo completo", valor=3,
        razon="Logro de cultura y talento con autorización, sin datos personales.",
        li="""Empezó como practicante. Hoy se queda en el equipo.

Una de nuestras practicantes de desarrollo terminó sus prácticas y se suma a tiempo completo a CorAll. Durante estos meses trabajó en proyectos reales y demostró que el talento crece cuando tiene espacio.

Estamos orgullosos de formar a quienes construirán la tecnología de la región.

¡Bienvenida oficialmente al equipo!""",
        fb="De practicante a integrante del equipo: una de nuestras practicantes de desarrollo se suma a tiempo completo. ¡Bienvenida!",
        ig="""🌟 De practicante a integrante del equipo.
Una de nuestras practicantes de desarrollo se queda con nosotros a tiempo completo. ¡Bienvenida!""",
        tt=[("Credencial de practicante", "Empezó como practicante."),
            ("Escritorio con código en pantalla", "Trabajó en proyectos reales durante meses."),
            ("Credencial nueva del equipo", "Y hoy se queda a tiempo completo. ¡Bienvenida!")],
        tit="De practicante a equipo", bul=[("Proyectos reales", "Desde el primer día."),
                                            ("Talento local", "Que crece aquí."),
                                            ("Bienvenida", "Al equipo.")],
        dato=None, cta="Únete al equipo",
        tags=["#Talento", "#CulturaCorAll", "#Prácticas", "#EquipoCorAll"],
        vis="Desk with a new team badge, a laptop with code and a small coral-shaped plant",
    ),
    dict(
        id="mx16", area="ia", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Se implementó el viernes de aprendizaje: cada viernes, 1 hora para que el equipo estudie un tema nuevo; en el primer mes se cubrieron 4 temas de IA y hardware",
        fuente="Viernes de aprendizaje del equipo", valor=3,
        razon="Contenido de cultura de aprendizaje sin datos sensibles.",
        li="""Cada viernes, una hora para aprender algo nuevo.

Implementamos el "viernes de aprendizaje": una hora semanal para que el equipo estudie un tema que no domina y lo comparta con los demás. En el primer mes cubrimos 4 temas de inteligencia artificial y hardware.

La tecnología cambia rápido. Aprender juntos es la forma de no quedarse atrás.

¿Tu equipo tiene un espacio para aprender?""",
        fb="Nuestro 'viernes de aprendizaje': una hora semanal para estudiar algo nuevo. En el primer mes, 4 temas de IA y hardware.",
        ig="""📚 Viernes de aprendizaje.
Una hora cada viernes para aprender algo nuevo. Primer mes: 4 temas de IA y hardware.""",
        tt=[("Reloj marcando viernes", "Cada viernes, una hora para aprender."),
            ("Pizarra con un tema nuevo", "Estudiamos un tema que no dominamos."),
            ("Equipo compartiendo (sin rostros)", "En el primer mes: 4 temas de IA y hardware.")],
        tit="Viernes de aprendizaje", bul=[("Una hora semanal", "Cada viernes."),
                                           ("Temas nuevos", "IA y hardware."),
                                           ("Compartir", "Con todo el equipo.")],
        dato="4 temas en el primer mes", cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#AprendizajeContinuo", "#EquipoCorAll", "#Tecnología"],
        vis="Whiteboard with sketches of a neural network and a circuit, books and laptops on a table",
    ),
    dict(
        id="mx17", area="hardware", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Se celebró el Día de la Mujer en la Ingeniería con una conversación interna sobre las ingenieras del equipo y sus proyectos en hardware e IA; ellas autorizaron mencionar sus proyectos sin fotos",
        fuente="Día de la Mujer en la Ingeniería", valor=3,
        razon="Fecha especial con autorización de las protagonistas; sin datos personales.",
        li="""Hoy celebramos a las ingenieras que diseñan, programan y prueban en nuestro equipo.

En el Día de la Mujer en la Ingeniería compartimos una conversación sobre sus proyectos: sensores de campo, modelos de visión artificial y plataformas que hoy usan nuestros clientes.

Más ingenieras en tecnología significa mejores soluciones para todos.

Gracias por inspirar al equipo.""",
        fb="En el Día de la Mujer en la Ingeniería celebramos a las ingenieras de nuestro equipo y sus proyectos en hardware e IA. ¡Gracias por inspirar!",
        ig="""👩‍🔧 Día de la Mujer en la Ingeniería.
Celebramos a las ingenieras que diseñan sensores, entrenan modelos y construyen plataformas en CorAll.""",
        tt=[("Mesa con un sensor y una laptop", "Hoy es el Día de la Mujer en la Ingeniería."),
            ("Proyectos de hardware e IA", "Celebramos a las ingenieras de nuestro equipo y sus proyectos."),
            ("Mensaje sobre fondo rojo", "Gracias por inspirar al equipo.")],
        tit="Mujeres en la ingeniería", bul=[("Hardware", "Sensores de campo."),
                                             ("IA", "Visión artificial."),
                                             ("Plataformas", "Que usan los clientes.")],
        dato=None, cta="Conoce al equipo",
        tags=["#MujeresEnIngeniería", "#CulturaCorAll", "#Ingeniería", "#EquipoCorAll"],
        vis="Engineering workbench with a sensor prototype, laptop with a neural network diagram and soft red light",
    ),
    dict(
        id="mx18", area="innovacion", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Cierre de año del equipo: se repasaron los 3 aprendizajes principales del año (probar en campo antes, documentar mejor y pedir ayuda a tiempo); foto grupal autorizada",
        fuente="Aprendizajes del año del equipo", valor=3,
        razon="Contenido de cultura con consentimiento; lección general sin datos sensibles.",
        li="""Tres lecciones que nos deja este año.

En nuestro cierre de año, el equipo eligió los aprendizajes que queremos llevar al siguiente:

1. Probar en campo antes, no después.
2. Documentar mejor, aunque cueste tiempo.
3. Pedir ayuda a tiempo, porque nadie construye solo.

Gracias a todo el equipo por un año de trabajo y aprendizaje. Vamos por el siguiente.""",
        fb="Cierre de año: probar en campo antes, documentar mejor y pedir ayuda a tiempo. Tres lecciones que llevamos al próximo año. ¡Gracias, equipo!",
        ig="""✨ 3 lecciones del año.
Probar en campo antes, documentar mejor y pedir ayuda a tiempo. ¡Gracias, equipo!""",
        tt=[("Calendario en diciembre", "Cerramos el año con tres lecciones."),
            ("Tres notas adhesivas", "Probar en campo antes, documentar mejor y pedir ayuda a tiempo."),
            ("Foto grupal con overlay rojo", "Gracias, equipo. Vamos por el siguiente.")],
        tit="3 lecciones del año", bul=[("Probar en campo", "Antes, no después."),
                                        ("Documentar mejor", "Aunque cueste."),
                                        ("Pedir ayuda", "A tiempo.")],
        dato=None, cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#CierreDeAño", "#EquipoCorAll", "#Aprendizaje"],
        vis="Year-end team celebration table with notebooks, sticky notes and festive red accents",
        adj="equipo",
    ),
    # ---- servicio en territorio ----
    dict(
        id="mx19", area="hardware", sector="minería", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Capacitación en sitio a 20 supervisores de una operación minera en el uso de los detectores portátiles de gases y la revisión del historial; el cliente autorizó publicarlo sin nombre ni rostros",
        fuente="Capacitación en detectores de gases", valor=4,
        razon="Servicio terminado con autorización; sin datos del cliente.",
        li="""Un equipo de seguridad funciona cuando todos saben usarlo.

Capacitamos en sitio a 20 supervisores de una operación minera en el uso de los detectores portátiles de gases: configuración de umbrales, respuesta a alertas y revisión del historial del turno.

Entregar el equipo es la mitad del trabajo. La otra mitad es que se use bien.

¿Tu equipo necesita una capacitación así? Conversemos.""",
        fb="Capacitamos en sitio a 20 supervisores mineros en el uso de detectores de gases: umbrales, alertas e historial del turno.",
        ig="""⛑️ Capacitación en sitio.
20 supervisores mineros aprendieron a configurar, responder alertas y revisar el historial de los detectores de gases.""",
        tt=[("Detector de gases sobre una mesa", "Un equipo de seguridad sirve si se sabe usar."),
            ("Supervisores en una sala (de espaldas)", "Capacitamos a 20 supervisores en sitio."),
            ("Historial del turno en una tablet", "Umbrales, alertas e historial del turno.")],
        tit="Capacitación en sitio", bul=[("20 supervisores", "Capacitados en sitio."),
                                          ("Umbrales y alertas", "Configuración y respuesta."),
                                          ("Historial", "Revisión del turno.")],
        dato="20 supervisores capacitados", cta="Conversemos",
        tags=["#Minería", "#SeguridadIndustrial", "#Capacitación", "#Hardware"],
        vis="Mining site training room with gas detectors on a table and safety helmets, no faces",
        adj="campo",
    ),
    dict(
        id="mx20", area="ia", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Instalación y ajuste en sitio de la cámara de conteo en una empacadora de palta, con autorización para publicar sin nombre: se calibró la iluminación y se dejó operando en 2 líneas",
        fuente="Puesta en marcha de visión artificial en empaque", valor=4,
        razon="Servicio terminado con autorización; muestra el trabajo de campo detrás de la IA.",
        li="""Un modelo de visión artificial se termina de ajustar en la planta, no en la oficina.

Esta semana instalamos y ajustamos en sitio la cámara de conteo en una empacadora de palta. Calibramos la iluminación, ajustamos el ángulo y la dejamos operando en 2 líneas.

La luz, el polvo y la velocidad de la faja cambian todo. Por eso la puesta en marcha siempre es en campo.

¿Tu planta está pensando en visión artificial? Conversemos.""",
        fb="Puesta en marcha en sitio: cámara de conteo instalada y calibrada en 2 líneas de una empacadora de palta.",
        ig="""🥑 Ajuste en planta.
Instalamos y calibramos la cámara de conteo en 2 líneas de una empacadora de palta.""",
        tt=[("Faja de empaque con paltas", "La IA se termina de ajustar en la planta."),
            ("Técnico ajustando la cámara (sin rostro)", "Calibramos la luz y el ángulo de la cámara."),
            ("Pantalla de conteo en vivo", "Y quedó operando en 2 líneas.")],
        tit="Ajuste en planta", bul=[("Iluminación calibrada", "Para la planta real."),
                                     ("Ángulo ajustado", "Sobre la faja."),
                                     ("2 líneas operando", "Conteo en vivo.")],
        dato=None, cta="Conversemos",
        tags=["#VisiónArtificial", "#Palta", "#Agroindustria", "#InteligenciaArtificial"],
        vis="Avocado packing line with a camera mounted above and an LED light bar, industrial setting",
        adj="campo",
    ),
    dict(
        id="mx21", area="software", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Acompañamiento en campo durante la primera semana de uso de la app de cosecha: se resolvieron dudas de 8 cuadrillas y se ajustaron 3 pantallas según sus comentarios; el cliente autorizó publicar sin nombre",
        fuente="Acompañamiento en campo de la app de cosecha", valor=4,
        razon="Servicio terminado con autorización; muestra cómo se mejora con el usuario.",
        li="""La retroalimentación más útil de una app llega desde el surco.

Durante la primera semana de uso de la app de cosecha estuvimos en campo con 8 cuadrillas. Resolvimos dudas en el momento y, con sus comentarios, ajustamos 3 pantallas para hacerlas más simples.

Una herramienta se adopta cuando quien la usa siente que fue hecha para él.

¿Tu equipo de campo necesita una herramienta así? Conversemos.""",
        fb="Primera semana de la app de cosecha: acompañamos a 8 cuadrillas en campo y ajustamos 3 pantallas con sus comentarios.",
        ig="""🌾 Mejorar desde el surco.
Acompañamos a 8 cuadrillas en su primera semana con la app de cosecha y ajustamos 3 pantallas con sus comentarios.""",
        tt=[("Celular en manos de un cosechador (sin rostro)", "La opinión más útil sobre una app llega desde el campo."),
            ("Pantalla antes y después", "Con los comentarios de 8 cuadrillas ajustamos 3 pantallas."),
            ("Cuadrilla trabajando al fondo", "Una herramienta hecha con quien la usa.")],
        tit="Mejorar desde el surco", bul=[("8 cuadrillas", "Acompañadas en campo."),
                                           ("3 pantallas", "Ajustadas."),
                                           ("Usuarios reales", "Primero.")],
        dato="8 cuadrillas, 3 pantallas mejoradas", cta="Conversemos",
        tags=["#Agroindustria", "#AppMóvil", "#ExperienciaDeUsuario", "#AgriculturaDigital"],
        vis="Harvest field rows with a smartphone in the foreground showing a simple app screen",
        adj="campo",
    ),
    dict(
        id="mx22", area="innovacion", sector="educación", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Asesoría a un colegio para su plan de transformación digital, con autorización para publicar sin nombre: se definieron 3 prioridades (libreta digital, comunicación con familias y control de asistencia)",
        fuente="Asesoría de transformación digital a un colegio", valor=4,
        razon="Servicio terminado con autorización; sin datos personales.",
        li="""Un colegio no necesita toda la tecnología: necesita la correcta, en el orden correcto.

Acompañamos a un colegio en su plan de transformación digital. Después de conversar con dirección, docentes y familias, definimos 3 prioridades: libreta digital, comunicación con las familias y control de asistencia.

Empezar por lo que más impacto tiene en el día a día hace que el cambio se sostenga.

¿Tu institución quiere ordenar su camino digital? Conversemos.""",
        fb="Asesoramos a un colegio en su transformación digital: 3 prioridades claras, libreta digital, comunicación con familias y asistencia.",
        ig="""🏫 Tecnología correcta, en el orden correcto.
Plan digital para un colegio: libreta digital, comunicación con familias y control de asistencia.""",
        tt=[("Aula vacía con pizarra", "¿Por dónde empieza la transformación digital de un colegio?"),
            ("Tres prioridades en pantalla", "Definimos 3 prioridades con dirección, docentes y familias."),
            ("Celular con la libreta digital", "Libreta digital, comunicación y asistencia.")],
        tit="El orden correcto", bul=[("Libreta digital", "Notas a tiempo."),
                                      ("Comunicación", "Con las familias."),
                                      ("Asistencia", "Control diario.")],
        dato=None, cta="Conversemos",
        tags=["#Educación", "#TransformaciónDigital", "#Colegios", "#Innovación"],
        vis="Empty classroom with a whiteboard showing three simple priority icons, bright daylight",
    ),
    dict(
        id="mx23", area="hardware", sector="cuero y calzado", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Instalación del contador de pares en un segundo taller de calzado de El Porvenir, con autorización para publicar sin nombre; se capacitó a 2 supervisores",
        fuente="Instalación del contador de pares en un taller", valor=3,
        razon="Servicio terminado con autorización; sin datos del cliente.",
        li="""Un segundo taller de El Porvenir ya cuenta su producción en tiempo real.

Instalamos nuestro contador de pares en otro taller de calzado del distrito y capacitamos a 2 supervisores para leer el conteo del turno y detectar a tiempo cuando la línea se retrasa.

Tecnología hecha en Trujillo para los talleres de Trujillo.

¿Tu taller quiere saber cuánto produce mientras produce? Conversemos.""",
        fb="Un segundo taller de calzado de El Porvenir ya cuenta su producción en tiempo real con nuestro contador de pares. Capacitamos a 2 supervisores.",
        ig="""👞 Otro taller que cuenta en tiempo real.
Instalamos el contador de pares en un taller de El Porvenir y capacitamos a 2 supervisores.""",
        tt=[("Taller de calzado en plena producción", "Otro taller de El Porvenir se suma."),
            ("Contador instalado al final de la faja", "Instalamos nuestro contador de pares."),
            ("Supervisor revisando el total (sin rostro)", "Y capacitamos a 2 supervisores.")],
        tit="Producción en tiempo real", bul=[("Contador de pares", "Instalado."),
                                              ("2 supervisores", "Capacitados."),
                                              ("Hecho en Trujillo", "Para Trujillo.")],
        dato=None, cta="Conversemos",
        tags=["#Calzado", "#ElPorvenir", "#Industria40", "#HechoEnTrujillo"],
        vis="Shoe workshop production line with a small optical counter at the end of the conveyor",
        adj="campo",
    ),
    # ---- producto ----
    dict(
        id="mx24", area="innovacion", sector="agroindustria", tipo="interno", pilar="producto",
        sec="matriz", mod="tablero-productor",
        det="Se terminó el tablero del productor: muestra kilos entregados, calidad por lote y pagos pendientes en una sola vista móvil; probado con 5 productores de la red de pilotos.",
        fuente="Tablero móvil para productores", valor=4,
        razon="Producto terminado y probado con usuarios; sin datos personales.",
        li="""El productor también merece ver sus datos claros y en su celular.

Terminamos el tablero del productor: en una sola vista muestra los kilos entregados, la calidad de cada lote y los pagos pendientes.

Lo probamos con 5 productores de nuestra red de pilotos y ajustamos la pantalla hasta que se entendiera sin explicación.

Transparencia que fortalece la relación entre el productor y quien le compra. ¿Te interesa? Conversemos.""",
        fb="Tablero del productor: kilos entregados, calidad por lote y pagos pendientes en una sola vista móvil. Probado con 5 productores.",
        ig="""📱 Tus entregas, claras y en el celular.
Kilos entregados, calidad por lote y pagos pendientes en una sola vista.""",
        tt=[("Productor revisando un cuaderno (de espaldas)", "¿Sabe el productor cuánto entregó y cuánto le deben?"),
            ("Celular con el tablero", "Ahora lo ve en una sola pantalla."),
            ("Calidad por lote y pagos", "Kilos, calidad y pagos pendientes, claros.")],
        tit="Tus entregas en el celular", bul=[("Kilos entregados", "Al día."),
                                               ("Calidad por lote", "Transparente."),
                                               ("Pagos pendientes", "Sin sorpresas.")],
        dato=None, cta="Conversemos",
        tags=["#Agroindustria", "#Transparencia", "#AppMóvil", "#Innovación"],
        vis="Smartphone mockup with a farmer dashboard showing kilos, quality and payments, field backdrop",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="mx25", area="ia", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="asistente-despachos",
        det="Se entregó el asistente de estado de pedidos por WhatsApp para {cliente}: el cliente final escribe su número de pedido y recibe el estado y la hora estimada de llegada; derivó a una persona el 9 % de las consultas en la primera semana.",
        fuente="Asistente de estado de pedidos", valor=4,
        razon="Producto entregado con dato de uso y derivación humana; sin datos del cliente.",
        li=""""¿Dónde está mi pedido?" ya no tiene que esperar a que alguien conteste.

Entregamos un asistente por WhatsApp para una empresa de reparto: el cliente escribe su número de pedido y recibe el estado y la hora estimada de llegada.

Cuando la consulta es más compleja, el asistente deriva a una persona. En la primera semana eso pasó solo en el 9 % de los casos.

Respuestas inmediatas y un equipo libre para lo importante. ¿Te interesa? Conversemos.""",
        fb="Asistente por WhatsApp para consultar pedidos: estado y hora estimada al instante, y derivación a una persona cuando hace falta.",
        ig="""📦 ¿Dónde está mi pedido?
Escribe tu número de pedido y recibe el estado y la hora estimada al instante. Si hace falta, te atiende una persona.""",
        tt=[("Cliente esperando respuesta en el celular", "¿Dónde está mi pedido?"),
            ("Chat respondiendo con el estado", "El asistente responde con el estado y la hora estimada."),
            ("Mensaje derivado a una persona", "Y si la consulta es compleja, te atiende una persona.")],
        tit="¿Dónde está mi pedido?", bul=[("Estado al instante", "Por WhatsApp."),
                                           ("Hora estimada", "De llegada."),
                                           ("Atención humana", "Cuando hace falta.")],
        dato=None, cta="Conversemos",
        tags=["#Chatbot", "#Logística", "#WhatsApp", "#InteligenciaArtificial"],
        vis="Smartphone mockup with a chat showing a delivery status and an estimated arrival time",
        vis_es="mockup de interfaz",
    ),
]
