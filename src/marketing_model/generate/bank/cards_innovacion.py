"""Publishable innovation tasks with their reference proposal content."""

CARDS = [
    dict(
        id="in01", area="innovacion", sector="cuero y calzado", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Diagnóstico de madurez digital terminado en una curtiembre, con autorización para publicar sin nombre: se evaluaron 6 áreas y se entregó una hoja de ruta con 3 proyectos priorizados",
        fuente="Diagnóstico de madurez digital en una curtiembre", valor=5,
        razon="Servicio terminado con autorización; muestra la metodología sin datos del cliente.",
        li="""Antes de invertir en tecnología, conviene saber por dónde empezar.

Terminamos un diagnóstico de madurez digital en una curtiembre de la región. Evaluamos 6 áreas de la empresa, desde compras hasta despacho, y entregamos una hoja de ruta con 3 proyectos priorizados según su impacto y su costo.

Un diagnóstico evita gastar en lo que no urge y ayuda a dar el primer paso con seguridad.

¿Quieres saber cuál es el primer paso para tu empresa? Conversemos.""",
        fb="Diagnóstico de madurez digital en una curtiembre: 6 áreas evaluadas y una hoja de ruta con 3 proyectos priorizados. ¿Hacemos el de tu empresa?",
        ig="""🧭 ¿Por dónde empezar a digitalizarte?
Diagnóstico en una curtiembre: 6 áreas evaluadas y 3 proyectos priorizados en una hoja de ruta.""",
        tt=[("Planta de curtiembre", "¿Por dónde empieza la transformación digital de una empresa?"),
            ("Checklist de áreas evaluadas", "Por un diagnóstico: evaluamos 6 áreas."),
            ("Hoja de ruta con 3 proyectos", "Y entregamos 3 proyectos priorizados.")],
        tit="¿Por dónde empezar?", bul=[("6 áreas evaluadas", "De compras a despacho."),
                                        ("Hoja de ruta", "Con prioridades claras."),
                                        ("3 proyectos", "Según impacto y costo.")],
        dato="6 áreas evaluadas, 3 proyectos priorizados", cta="Conversemos",
        tags=["#TransformaciónDigital", "#MadurezDigital", "#Curtiembre", "#Innovación"],
        vis="Leather tannery workshop with a translucent roadmap diagram overlay of three milestones",
        adj="campo",
    ),
    dict(
        id="in02", area="innovacion", sector="cuero y calzado", tipo="cliente", pilar="hito",
        sec="matriz", mod="lana-40",
        det="Proyecto Industria 4.0: se completó la integración de sensores y tablero en la línea de procesamiento de lana de {cliente}: 4 puntos de medición en línea y producción por turno visible en tiempo real. El cliente autorizó difundir el caso sin su nombre.",
        fuente="Industria 4.0 en una línea de lana", valor=5,
        razon="Hito terminado con autorización para difundir el caso sin nombre.",
        li="""Una línea de procesamiento de lana que ahora se puede ver en tiempo real.

Completamos la integración de sensores y tablero en una línea de procesamiento de lana: 4 puntos de medición en línea y la producción por turno visible en el momento.

Antes, el avance se conocía al final del día. Hoy el jefe de planta lo ve mientras sucede y puede reaccionar a tiempo.

Industria 4.0 aplicada a una industria tradicional. ¿Tu línea necesita visibilidad? Conversemos.""",
        fb="Industria 4.0 en una línea de lana: 4 puntos de medición y producción por turno en tiempo real. Del reporte al final del día a decidir en el momento.",
        ig="""🐑 Lana 4.0.
4 puntos de medición en línea y producción por turno visible en tiempo real.""",
        tt=[("Fibras de lana en movimiento", "Así se procesa la lana."),
            ("Sensores en la máquina", "Instalamos 4 puntos de medición en la línea."),
            ("Tablero con producción por turno", "Y la producción por turno ahora se ve en tiempo real.")],
        tit="Lana 4.0", bul=[("4 puntos de medición", "En la línea."),
                             ("Producción por turno", "En tiempo real."),
                             ("Reacción a tiempo", "Del jefe de planta.")],
        dato="4 puntos de medición en línea", cta="Conversemos",
        tags=["#Industria40", "#Textil", "#Innovación", "#TransformaciónDigital"],
        vis="Wool processing machinery with soft data overlay lines and a dashboard screen nearby",
    ),
    dict(
        id="in03", area="innovacion", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller 'Innovación abierta para mypes de La Libertad': martes 9 de diciembre, 15:00 a 18:00, sede de CorAll en Trujillo, con 30 cupos; cofinanciado por un programa público de innovación",
        fuente="Taller de innovación abierta para mypes", valor=5,
        razon="Evento confirmado con fecha, lugar y cupos; ideal para convocatoria.",
        li="""Las mejores ideas para tu negocio pueden venir de fuera de tu negocio.

Te invitamos al taller "Innovación abierta para mypes de La Libertad", donde trabajaremos con casos reales cómo resolver problemas junto a clientes, proveedores y universidades.

📅 Martes 9 de diciembre
🕒 15:00 a 18:00
📍 Sede de CorAll, Trujillo
👥 30 cupos

Inscríbete en el enlace.""",
        fb="Taller 'Innovación abierta para mypes de La Libertad': martes 9 de diciembre, 15:00 a 18:00, sede de CorAll en Trujillo. 30 cupos.",
        ig="""💡 Innovación abierta para mypes.
Martes 9 de diciembre, 15:00 a 18:00, sede de CorAll en Trujillo. Solo 30 cupos.""",
        tt=[("Notas adhesivas en una pared", "¿Y si la solución a tu problema viene de fuera?"),
            ("Mesa de trabajo colaborativo (sin rostros)", "Ven al taller de innovación abierta para mypes."),
            ("Fecha en pantalla", "Martes 9 de diciembre, 15:00. 30 cupos.")],
        tit="Innovación abierta para mypes", bul=[("Martes 9 de diciembre", "De 15:00 a 18:00."),
                                                  ("Sede de CorAll", "Trujillo."),
                                                  ("30 cupos", "Inscripción en el enlace.")],
        dato="Martes 9 de diciembre, 15:00", cta="Inscríbete",
        tags=["#InnovaciónAbierta", "#Mypes", "#LaLibertad", "#Innovación"],
        vis="Workshop wall covered in sticky notes in red, black and white, with geometric shapes",
    ),
    dict(
        id="in04", area="innovacion", sector="agroindustria", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="Se recibió la resolución de aprobación del proyecto de trazabilidad agrícola en el concurso de un programa público de innovación; el proyecto durará 12 meses y se puede anunciar públicamente",
        fuente="Aprobación de un proyecto de innovación", valor=5,
        razon="Hito confirmado oficialmente y anunciable; sin montos ni datos sensibles.",
        li="""Nuestro proyecto de trazabilidad agrícola fue aprobado.

Recibimos la resolución de aprobación en el concurso de un programa público de innovación. Durante los próximos 12 meses desarrollaremos una solución de trazabilidad para que cada lote pueda contar su historia, del campo al cliente.

Agradecemos la confianza y al equipo que trabajó en la postulación.

Iremos compartiendo los avances. ¿Te interesa la trazabilidad para tu producción? Escríbenos.""",
        fb="¡Proyecto aprobado! Durante 12 meses desarrollaremos una solución de trazabilidad agrícola del campo al cliente. Gracias por la confianza.",
        ig="""🎉 ¡Proyecto aprobado!
12 meses para desarrollar trazabilidad agrícola, del campo al cliente.""",
        tt=[("Documento con sello de aprobado", "Tenemos una gran noticia."),
            ("Lote de fruta con un código QR", "Nuestro proyecto de trazabilidad agrícola fue aprobado."),
            ("Línea de tiempo de 12 meses", "Son 12 meses para llevar cada lote del campo al cliente.")],
        tit="Proyecto aprobado", bul=[("Trazabilidad agrícola", "Del campo al cliente."),
                                      ("12 meses", "De desarrollo."),
                                      ("Avances", "Los compartiremos aquí.")],
        dato="12 meses de proyecto", cta="Escríbenos",
        tags=["#Innovación", "#Trazabilidad", "#Agroindustria", "#ProyectoAprobado"],
        vis="Crate of fresh produce with a QR tag in soft light and a subtle approval seal icon",
        comp="dato destacado",
    ),
    dict(
        id="in05", area="innovacion", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se documentó la metodología de piloto en campo de CorAll: problema medible, prueba corta en condiciones reales, decisión con datos y recién después escalar",
        fuente="Metodología de piloto antes de escalar", valor=4,
        razon="Contenido educativo que explica la forma de trabajo; sin datos internos.",
        li="""Escalar una solución que no se probó en campo es apostar a ciegas.

Así trabajamos cada proyecto:

1. Definimos un problema medible.
2. Hacemos una prueba corta en condiciones reales.
3. Decidimos con los datos de esa prueba.
4. Recién entonces escalamos.

Es más lento al inicio, pero evita inversiones grandes en algo que no funciona. ¿Tienes un problema que quieras probar en pequeño? Conversemos.""",
        fb="Primero piloto, después escala: problema medible, prueba corta en campo, decisión con datos y recién entonces escalar.",
        ig="""🧪 Primero probar, después escalar.
Problema medible, prueba corta en campo, decisión con datos y recién entonces escalar.""",
        tt=[("Gran inversión cayendo", "Escalar sin probar es apostar a ciegas."),
            ("Pequeño piloto en campo", "Primero, una prueba corta en condiciones reales."),
            ("Gráfico creciendo con datos", "Decidimos con datos y recién escalamos.")],
        tit="Primero probar, después escalar", bul=[("Problema medible", "Qué queremos cambiar."),
                                                    ("Piloto en campo", "Corto y real."),
                                                    ("Decisión con datos", "Antes de escalar.")],
        dato=None, cta="Conversemos",
        tags=["#Innovación", "#PilotoEnCampo", "#TransformaciónDigital", "#BuenasPrácticas"],
        vis="3D illustration of a small seedling in a test tube growing into a larger plant, stepwise",
        comp="línea de tiempo",
    ),
    dict(
        id="in06", area="innovacion", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Taller de co-diseño con 15 productores de una cooperativa agraria para definir qué datos necesitan de su cosecha; la cooperativa autorizó publicar fotos del taller sin rostros",
        fuente="Taller de co-diseño con productores", valor=4,
        razon="Servicio terminado con autorización; muestra el trabajo con usuarios reales.",
        li="""Una herramienta para productores se diseña mejor con ellos en la mesa.

Realizamos un taller de co-diseño con 15 productores de una cooperativa agraria. Juntos definimos qué datos de su cosecha necesitan ver, cuándo y en qué formato.

Escuchar primero nos ahorra construir pantallas que nadie usa.

¿Tu organización quiere diseñar una solución con sus propios usuarios? Conversemos.""",
        fb="Taller de co-diseño con 15 productores de una cooperativa: definimos juntos qué datos de su cosecha necesitan ver. Diseñar con el usuario, no para él.",
        ig="""🌾 Diseñar con los productores.
Taller de co-diseño con 15 productores para definir qué datos de su cosecha necesitan ver.""",
        tt=[("Manos de productores sobre papelógrafos", "¿Quién sabe qué necesita un productor? El productor."),
            ("Dibujos de pantallas en papel", "Hicimos un taller de co-diseño con 15 productores."),
            ("Boceto convirtiéndose en pantalla", "Y juntos definimos qué datos necesitan ver.")],
        tit="Diseñar con los productores", bul=[("15 productores", "De una cooperativa."),
                                                ("Co-diseño", "Ideas desde el campo."),
                                                ("Menos pantallas inútiles", "Escuchar primero.")],
        dato="15 productores participaron", cta="Conversemos",
        tags=["#CoDiseño", "#Agroindustria", "#Innovación", "#Cooperativas"],
        vis="Hands of farmers working on paper prototypes and sticky notes on a rustic wooden table",
        adj="campo",
    ),
    dict(
        id="in07", area="innovacion", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Se implementó el buzón interno de ideas: en el primer mes el equipo envió 23 ideas y 2 pasaron a prototipo",
        fuente="Buzón interno de ideas", valor=3,
        razon="Contenido de cultura de innovación sin datos sensibles.",
        li="""23 ideas en un mes. 2 ya son prototipo.

Abrimos un buzón interno de ideas para que cualquier persona del equipo proponga mejoras, sin importar su área. En el primer mes recibimos 23 ideas y 2 ya pasaron a prototipo.

La innovación no es solo tarea de un área: aparece cuando todos sienten que su idea cuenta.

¿Cómo recoges las ideas de tu equipo?""",
        fb="Nuestro buzón interno de ideas recibió 23 propuestas en su primer mes y 2 ya pasaron a prototipo. La innovación es de todos.",
        ig="""💡 23 ideas en un mes.
Así arrancó nuestro buzón interno de ideas. 2 ya pasaron a prototipo.""",
        tt=[("Buzón con papeles", "Abrimos un buzón de ideas para todo el equipo."),
            ("Contador llegando a 23", "En el primer mes llegaron 23 ideas."),
            ("Prototipo sobre la mesa", "Y 2 ya son prototipo.")],
        tit="23 ideas en un mes", bul=[("Buzón abierto", "Para todo el equipo."),
                                       ("23 ideas", "En el primer mes."),
                                       ("2 prototipos", "Ya en marcha.")],
        dato="23 ideas, 2 prototipos", cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#Innovación", "#Ideas", "#EquipoCorAll"],
        vis="Red mailbox with folded paper notes and a small prototype device beside it, warm light",
    ),
    dict(
        id="in08", area="innovacion", sector="minería", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Contenido sobre cómo medir el retorno de un proyecto de innovación: definir la línea base antes de empezar, elegir 1 o 2 indicadores y medir de nuevo al cerrar el piloto",
        fuente="Cómo medir el retorno de la innovación", valor=4,
        razon="Contenido educativo general útil para clientes industriales.",
        li="""¿Cómo saber si un proyecto de innovación valió la pena? Midiendo antes de empezar.

Tres pasos simples:

1. Mide la línea base: cómo funciona hoy el proceso.
2. Elige solo uno o dos indicadores que importen de verdad.
3. Vuelve a medir al cerrar el piloto, en las mismas condiciones.

Sin línea base, cualquier resultado es una opinión. ¿Ya mides tus procesos antes de cambiarlos?""",
        fb="Para medir el retorno de un proyecto de innovación: mide la línea base, elige uno o dos indicadores y vuelve a medir al cerrar el piloto.",
        ig="""📏 Sin línea base, es solo una opinión.
Mide antes, elige uno o dos indicadores y vuelve a medir al cerrar el piloto.""",
        tt=[("Proceso industrial en marcha", "¿Tu proyecto de innovación valió la pena?"),
            ("Indicador antes del cambio", "Mide la línea base antes de empezar."),
            ("Mismo indicador después", "Y vuelve a medir al cerrar el piloto.")],
        tit="Mide antes de innovar", bul=[("Línea base", "Cómo funciona hoy."),
                                          ("Pocos indicadores", "Los que importan."),
                                          ("Medir al cierre", "En las mismas condiciones.")],
        dato=None, cta="Cuéntanos",
        tags=["#Innovación", "#Indicadores", "#Industria40", "#BuenasPrácticas"],
        vis="3D illustration of two gauges side by side showing a before and after reading",
        comp="antes / después",
    ),
    dict(
        id="in09", area="innovacion", sector="educación", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="Se firmó el convenio de cooperación con un instituto técnico de Trujillo para prácticas y proyectos conjuntos de innovación; ambas partes autorizaron anunciarlo",
        fuente="Convenio con un instituto técnico", valor=4,
        razon="Hito firmado y autorizado para anunciarse.",
        li="""Talento local y proyectos reales: firmamos un convenio de cooperación.

Formalizamos un convenio con un instituto técnico de Trujillo para desarrollar prácticas profesionales y proyectos conjuntos de innovación.

Creemos que la tecnología de la región se construye con su gente. Este convenio abre la puerta para que más estudiantes aprendan trabajando en problemas reales de las empresas.

Gracias por la confianza. Vamos por buenos proyectos juntos.""",
        fb="Firmamos un convenio con un instituto técnico de Trujillo para prácticas y proyectos conjuntos de innovación. Talento local, problemas reales.",
        ig="""🤝 Convenio firmado.
Prácticas y proyectos conjuntos de innovación con un instituto técnico de Trujillo.""",
        tt=[("Dos manos firmando un documento", "Firmamos un convenio de cooperación."),
            ("Estudiantes en un laboratorio (sin rostros)", "Con un instituto técnico de Trujillo."),
            ("Prototipo en la mesa", "Para prácticas y proyectos reales de innovación.")],
        tit="Convenio firmado", bul=[("Prácticas", "Para estudiantes."),
                                     ("Proyectos conjuntos", "De innovación."),
                                     ("Talento local", "Problemas reales.")],
        dato=None, cta="Conoce más",
        tags=["#Innovación", "#Educación", "#Convenio", "#Trujillo"],
        vis="Handshake silhouette over a technical classroom lab background with red overlay",
    ),
    dict(
        id="in10", area="innovacion", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Recorrido por la planta de empaque de un cliente agroexportador para levantar el mapa de procesos; se identificaron 4 puntos donde se pierde información. El cliente autorizó compartir el aprendizaje sin su nombre",
        fuente="Mapa de procesos en una planta de empaque", valor=4,
        razon="Servicio terminado con autorización; se comparte el aprendizaje sin datos del cliente.",
        li="""En una planta de empaque, la información se pierde en lugares que nadie mira.

Recorrimos la planta de una empresa agroexportadora para levantar su mapa de procesos, desde la recepción hasta el despacho. Encontramos 4 puntos donde la información se pierde: anotaciones en papel, pasos que se repiten y datos que nadie consolida.

Ver el proceso completo es el primer paso para decidir qué digitalizar.

¿Sabes dónde se pierde la información en tu planta? Conversemos.""",
        fb="Levantamos el mapa de procesos de una planta de empaque y encontramos 4 puntos donde se pierde información. Ver el proceso es el primer paso.",
        ig="""🔍 ¿Dónde se pierde la información?
Mapa de procesos en una planta de empaque: 4 puntos críticos identificados.""",
        tt=[("Recepción de fruta en planta", "Recorrimos una planta de empaque de punta a punta."),
            ("Cuaderno de anotaciones en papel", "Y encontramos 4 puntos donde se pierde información."),
            ("Diagrama de procesos con marcas", "Ver el proceso completo es el primer paso.")],
        tit="¿Dónde se pierde el dato?", bul=[("Mapa de procesos", "De recepción a despacho."),
                                              ("4 puntos críticos", "Donde se pierde información."),
                                              ("Primer paso", "Para digitalizar.")],
        dato="4 puntos críticos identificados", cta="Conversemos",
        tags=["#Agroexportación", "#MejoraDeProcesos", "#TransformaciónDigital", "#Innovación"],
        vis="Fruit packing plant interior with a translucent process flow diagram overlay",
        adj="campo",
    ),
    dict(
        id="in11", area="innovacion", sector="logística y transporte", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se elaboró material sobre cómo priorizar proyectos tecnológicos: matriz de impacto y esfuerzo, empezar por los de alto impacto y bajo esfuerzo",
        fuente="Cómo priorizar proyectos tecnológicos", valor=3,
        razon="Contenido educativo general para empresas.",
        li="""Tienes diez ideas de mejora y presupuesto para dos. ¿Cuáles eliges?

Una herramienta simple que usamos con nuestros clientes es la matriz de impacto y esfuerzo:

- Alto impacto, bajo esfuerzo: empieza por aquí.
- Alto impacto, alto esfuerzo: planifícalo por etapas.
- Bajo impacto, bajo esfuerzo: hazlo si sobra tiempo.
- Bajo impacto, alto esfuerzo: descártalo.

Priorizar bien es avanzar rápido sin gastar de más. ¿Cómo priorizas tus proyectos?""",
        fb="¿Muchas ideas y poco presupuesto? Usa la matriz de impacto y esfuerzo: empieza por lo de alto impacto y bajo esfuerzo.",
        ig="""📐 ¿Qué proyecto hacer primero?
Matriz de impacto y esfuerzo: empieza por lo de alto impacto y bajo esfuerzo.""",
        tt=[("Lista larga de ideas", "Tienes muchas ideas y poco presupuesto."),
            ("Matriz de cuatro cuadrantes", "Ordénalas por impacto y esfuerzo."),
            ("Cuadrante resaltado", "Y empieza por lo de alto impacto y bajo esfuerzo.")],
        tit="¿Qué proyecto va primero?", bul=[("Alto impacto", "Bajo esfuerzo: primero."),
                                              ("Por etapas", "Si el esfuerzo es alto."),
                                              ("Descarta", "Lo de bajo impacto.")],
        dato=None, cta="Cuéntanos",
        tags=["#Innovación", "#GestiónDeProyectos", "#Pymes", "#BuenasPrácticas"],
        vis="3D illustration of a four-quadrant matrix with one quadrant glowing in brand red",
    ),
    dict(
        id="in12", area="innovacion", sector="minería", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Cierre del piloto de monitoreo ambiental de 3 meses con un cliente minero: se decidió escalar a toda la unidad. El cliente autorizó compartir el hito sin su nombre",
        fuente="Piloto de monitoreo ambiental que escala", valor=5,
        razon="Hito real con autorización; respalda la metodología de piloto antes de escalar.",
        li="""3 meses de piloto. Una decisión: escalar.

Cerramos un piloto de monitoreo ambiental con una empresa minera. Durante 3 meses medimos, ajustamos y revisamos los datos junto a su equipo.

Con esos resultados, la decisión fue llevar la solución a toda la unidad.

Así nos gusta trabajar: demostrar en campo antes de escalar. ¿Tienes un reto que quieras probar con un piloto? Conversemos.""",
        fb="Tras 3 meses de piloto de monitoreo ambiental, una empresa minera decidió escalar la solución a toda su unidad. Primero demostrar, después crecer.",
        ig="""⛏️ Del piloto a toda la unidad.
3 meses de monitoreo ambiental en campo y la decisión de escalar.""",
        tt=[("Calendario de 3 meses", "3 meses de piloto en una unidad minera."),
            ("Datos ambientales en pantalla", "Medimos, ajustamos y revisamos con su equipo."),
            ("Mapa de la unidad completa iluminándose", "Y la decisión fue escalar a toda la unidad.")],
        tit="Del piloto a toda la unidad", bul=[("3 meses de piloto", "En campo."),
                                                ("Datos revisados", "Con el cliente."),
                                                ("Decisión: escalar", "A toda la unidad.")],
        dato="3 meses de piloto", cta="Conversemos",
        tags=["#Minería", "#MonitoreoAmbiental", "#PilotoEnCampo", "#Innovación"],
        vis="High-altitude mining landscape at dawn with a network of small monitoring stations glowing",
        comp="línea de tiempo",
    ),
    dict(
        id="in13", area="innovacion", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Se realizó el desayuno de innovación con 18 empresarios de la región en la sede de CorAll; se conversó sobre retos de digitalización. Los asistentes aceptaron que se publiquen fotos generales sin identificarlos",
        fuente="Desayuno de innovación con empresarios", valor=4,
        razon="Evento realizado con autorización de fotos generales.",
        li="""18 empresarios, un desayuno y una conversación honesta sobre digitalización.

Esta semana recibimos en nuestra sede a 18 empresarios de la región para hablar de sus retos reales: procesos en papel, información dispersa y miedo a invertir en tecnología que no funcione.

Nos quedamos con muchas ideas y con la confirmación de que el primer paso es conversar.

Gracias a todos por venir. Pronto anunciaremos el próximo encuentro.""",
        fb="Gracias a los 18 empresarios que nos acompañaron en el desayuno de innovación. Conversamos de retos reales de digitalización. ¡Nos vemos en el próximo!",
        ig="""☕ Desayuno de innovación.
18 empresarios de la región conversando sobre sus retos de digitalización. ¡Gracias por venir!""",
        tt=[("Mesa de desayuno lista", "Un desayuno para hablar de innovación."),
            ("Conversación en grupo (de espaldas)", "18 empresarios compartieron sus retos de digitalización."),
            ("Tazas sobre la mesa al final", "El primer paso siempre es conversar.")],
        tit="Desayuno de innovación", bul=[("18 empresarios", "De la región."),
                                           ("Retos reales", "De digitalización."),
                                           ("Próximo encuentro", "Muy pronto.")],
        dato="18 empresarios participaron", cta="Conoce más",
        tags=["#Innovación", "#Empresarios", "#LaLibertad", "#TransformaciónDigital"],
        vis="Breakfast table set for a business meeting with coffee cups, notebooks and red accents",
        adj="campo",
    ),
    dict(
        id="in14", area="innovacion", sector="agroindustria", tipo="interno", pilar="producto",
        sec="matriz", mod="trazabilidad-agro",
        det="Se terminó el prototipo de trazabilidad por lote con QR: el productor registra cosecha y aplicación de insumos, y el comprador escanea el QR y ve la historia del lote. Se probó con 10 lotes simulados.",
        fuente="Prototipo de trazabilidad por lote con QR", valor=4,
        razon="Prototipo terminado y probado; se presenta como avance sin datos sensibles.",
        li="""¿Y si cada lote pudiera contar su historia con solo escanear un código?

Terminamos nuestro prototipo de trazabilidad: el productor registra la cosecha y la aplicación de insumos, y el comprador escanea un QR para ver la historia del lote.

Ya lo probamos con 10 lotes y está listo para su primer piloto en campo.

La confianza del comprador empieza en la información. ¿Te interesa probarlo? Escríbenos.""",
        fb="Prototipo de trazabilidad por lote: el productor registra cosecha e insumos y el comprador escanea un QR para ver la historia del lote.",
        ig="""📱 Cada lote cuenta su historia.
El productor registra cosecha e insumos; el comprador escanea un QR y lo ve todo.""",
        tt=[("Caja de fruta con un QR", "¿De dónde viene esta fruta?"),
            ("Celular escaneando el QR", "Escanea el código y lo sabrás."),
            ("Historia del lote en pantalla", "Cosecha, insumos y fechas, del campo a tus manos.")],
        tit="Cada lote cuenta su historia", bul=[("Registro del productor", "Cosecha e insumos."),
                                                 ("Código QR", "En cada lote."),
                                                 ("Confianza del comprador", "Información a la vista.")],
        dato=None, cta="Escríbenos",
        tags=["#Trazabilidad", "#Agroindustria", "#Innovación", "#Agroexportación"],
        vis="Smartphone scanning a QR label on a crate of fresh produce in a packing house",
    ),
    dict(
        id="in15", area="innovacion", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Aniversario de CorAll: el equipo celebró con un almuerzo y un repaso de los proyectos del año en las 4 áreas; foto grupal autorizada por todos",
        fuente="Aniversario de CorAll", valor=4,
        razon="Fecha especial de cultura con consentimiento para la foto grupal.",
        li="""Un año más construyendo tecnología desde Trujillo.

Hoy celebramos un nuevo aniversario de CorAll. Repasamos los proyectos del año en nuestras 4 áreas: innovación, software, inteligencia artificial y hardware.

Cada uno de ellos empezó con un problema real y terminó en algo que funciona gracias a un equipo comprometido.

Gracias a nuestros clientes, aliados y a todo el equipo. Seguimos.""",
        fb="¡Feliz aniversario, CorAll! Un año más de proyectos en innovación, software, inteligencia artificial y hardware desde Trujillo. Gracias a todos.",
        ig="""🎂 ¡Feliz aniversario, CorAll!
Un año más de innovación, software, IA y hardware desde Trujillo. Gracias, equipo.""",
        tt=[("Torta con el isotipo de coral", "Hoy celebramos un nuevo aniversario."),
            ("Collage de proyectos del año", "Proyectos en innovación, software, IA y hardware."),
            ("Foto grupal con overlay rojo", "Gracias a todo el equipo. Seguimos.")],
        tit="Feliz aniversario, CorAll", bul=[("4 áreas", "Un mismo equipo."),
                                              ("Problemas reales", "Soluciones que funcionan."),
                                              ("Gracias", "A clientes y aliados.")],
        dato=None, cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#Aniversario", "#EquipoCorAll", "#Trujillo"],
        vis="Celebration table with confetti in brand red and black, warm festive office ambience",
        adj="equipo",
    ),
    dict(
        id="in16", area="innovacion", sector="cuero y calzado", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Material para el sector calzado: tres señales de que una fábrica está lista para digitalizar su producción (pedidos que se pierden, inventario que no cuadra y tiempos de entrega que nadie puede estimar)",
        fuente="Señales para digitalizar una fábrica de calzado", valor=4,
        razon="Contenido educativo general para el sector.",
        li="""¿Tu fábrica de calzado está lista para digitalizarse? Estas tres señales dicen que sí.

1. Pedidos que se pierden entre cuadernos y mensajes.
2. Inventario de cuero que nunca cuadra con lo que hay en el almacén.
3. Tiempos de entrega que nadie puede estimar con seguridad.

Si reconoces al menos una, el primer paso no es comprar un sistema: es entender tu proceso. ¿Conversamos?""",
        fb="3 señales de que tu fábrica de calzado necesita digitalizarse: pedidos que se pierden, inventario que no cuadra y entregas que nadie puede estimar.",
        ig="""👞 3 señales para digitalizar tu fábrica.
Pedidos que se pierden, inventario que no cuadra y entregas que nadie puede estimar.""",
        tt=[("Cuaderno de pedidos lleno de tachones", "¿Se te pierden los pedidos?"),
            ("Almacén de cuero desordenado", "¿Tu inventario nunca cuadra?"),
            ("Reloj y calendario", "Si nadie sabe cuándo se entrega, es hora de digitalizar.")],
        tit="¿Lista para digitalizarte?", bul=[("Pedidos perdidos", "Entre cuadernos."),
                                               ("Inventario descuadrado", "Cuero que no aparece."),
                                               ("Entregas inciertas", "Sin fecha clara.")],
        dato=None, cta="Conversemos",
        tags=["#Calzado", "#TransformaciónDigital", "#Industria40", "#Pymes"],
        vis="3D illustration of a shoe workshop desk with a messy order notebook turning into a tablet",
    ),
    dict(
        id="in17", area="innovacion", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Sesión de cierre del diagnóstico logístico con una empresa de transporte, con autorización para publicar sin nombre: se presentaron 5 oportunidades de mejora y el cliente eligió 2 para empezar",
        fuente="Cierre de diagnóstico logístico", valor=4,
        razon="Servicio terminado con autorización para difundirlo sin nombre.",
        li="""5 oportunidades de mejora encontradas. 2 elegidas para empezar.

Cerramos el diagnóstico logístico de una empresa de transporte. Presentamos 5 oportunidades de mejora, desde la planificación de rutas hasta el control de mantenimiento, y el cliente eligió 2 para comenzar.

Empezar por pocas cosas y bien hechas es más efectivo que intentar cambiarlo todo a la vez.

¿Quieres saber dónde mejorar en tu operación? Conversemos.""",
        fb="Diagnóstico logístico cerrado: 5 oportunidades de mejora y 2 elegidas para empezar. Pocas cosas, bien hechas.",
        ig="""🚛 5 oportunidades, 2 para empezar.
Cerramos un diagnóstico logístico con una empresa de transporte. Empezar por pocas cosas y bien hechas.""",
        tt=[("Patio de camiones", "Hicimos un diagnóstico logístico."),
            ("Lista de 5 oportunidades", "Encontramos 5 oportunidades de mejora."),
            ("2 elementos resaltados", "Y el cliente eligió 2 para empezar.")],
        tit="5 oportunidades de mejora", bul=[("Diagnóstico", "De la operación."),
                                              ("5 oportunidades", "Identificadas."),
                                              ("2 para empezar", "Elegidas por el cliente.")],
        dato="5 oportunidades, 2 priorizadas", cta="Conversemos",
        tags=["#Logística", "#MejoraDeProcesos", "#Transporte", "#Innovación"],
        vis="Truck depot at golden hour with a clipboard checklist overlay showing five items",
    ),
    dict(
        id="in18", area="innovacion", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Contenido sobre fondos públicos de innovación para mypes: qué tipo de proyectos financian, cómo preparar una postulación y por qué conviene asociarse con una entidad técnica",
        fuente="Fondos públicos de innovación para mypes", valor=4,
        razon="Contenido educativo de interés general; sin montos ni datos internos.",
        li="""¿Sabías que tu mype puede postular a fondos públicos para innovar?

Existen programas que cofinancian proyectos de innovación. Tres consejos para empezar:

1. Define un problema concreto de tu negocio que la tecnología pueda resolver.
2. Prepara la postulación con tiempo: los requisitos suelen ser detallados.
3. Asóciate con una entidad técnica que te acompañe en el desarrollo.

Un buen proyecto bien planteado tiene más posibilidades. ¿Tienes una idea? Conversemos.""",
        fb="Tu mype puede postular a fondos públicos de innovación: define un problema concreto, prepara la postulación con tiempo y asóciate con una entidad técnica.",
        ig="""💰 Fondos para innovar.
Define un problema concreto, prepara tu postulación con tiempo y asóciate con una entidad técnica.""",
        tt=[("Emprendedor frente a una laptop (de espaldas)", "¿Sabías que tu mype puede recibir fondos para innovar?"),
            ("Documento de postulación", "Define un problema concreto y prepara la postulación con tiempo."),
            ("Dos piezas de rompecabezas uniéndose", "Y asóciate con una entidad técnica.")],
        tit="Fondos para innovar", bul=[("Problema concreto", "Que la tecnología resuelva."),
                                        ("Postula con tiempo", "Requisitos detallados."),
                                        ("Socio técnico", "Que te acompañe.")],
        dato=None, cta="Conversemos",
        tags=["#Innovación", "#Mypes", "#FondosConcursables", "#Emprendimiento"],
        vis="3D illustration of a lightbulb on top of a stack of documents with a coin icon",
    ),
    dict(
        id="in19", area="innovacion", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Una cooperativa agraria usó por primera vez el tablero de cosecha para pagar a sus 40 socios con base en datos registrados; la cooperativa autorizó compartir el hito sin su nombre",
        fuente="Pagos a socios con datos registrados", valor=5,
        razon="Hito con impacto social y autorización para compartirlo sin nombre.",
        li="""40 socios recibieron su pago con base en datos registrados, no en cálculos a mano.

Una cooperativa agraria usó por primera vez su tablero de cosecha para calcular el pago a sus 40 socios. Cada pesada estaba registrada y cada socio pudo ver de dónde salía su monto.

La transparencia también se construye con tecnología.

Gracias a la cooperativa por confiar en el proceso. ¿Tu organización quiere dar este paso? Conversemos.""",
        fb="Una cooperativa pagó por primera vez a sus 40 socios con base en datos registrados en su tablero de cosecha. Transparencia con tecnología.",
        ig="""🌱 Pagos transparentes.
40 socios de una cooperativa recibieron su pago con base en datos registrados de su cosecha.""",
        tt=[("Productores en el campo (de espaldas)", "40 socios de una cooperativa."),
            ("Tablero con pesadas registradas", "Por primera vez, su pago salió de datos registrados."),
            ("Recibo claro en pantalla", "Cada socio pudo ver de dónde salía su monto.")],
        tit="Pagos con datos claros", bul=[("40 socios", "De una cooperativa."),
                                           ("Datos registrados", "Cada pesada."),
                                           ("Transparencia", "En cada pago.")],
        dato="40 socios pagados con datos registrados", cta="Conversemos",
        tags=["#Cooperativas", "#Agroindustria", "#Transparencia", "#Innovación"],
        vis="Rural cooperative warehouse with crates and a tablet showing a clear payment summary",
        adj="campo",
    ),
    dict(
        id="in20", area="innovacion", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la jornada de puertas abiertas del laboratorio de CorAll para estudiantes universitarios: sábado 13 de diciembre, 10:00 a 13:00, ingreso libre con inscripción",
        fuente="Puertas abiertas del laboratorio", valor=4,
        razon="Evento confirmado con fecha, hora e inscripción.",
        li="""¿Quieres ver cómo se construye tecnología en Trujillo? Abrimos las puertas de nuestro laboratorio.

Te invitamos a nuestra jornada de puertas abiertas para estudiantes universitarios. Conocerás nuestros prototipos de hardware, demos de inteligencia artificial y cómo trabajamos los proyectos.

📅 Sábado 13 de diciembre
🕙 10:00 a 13:00
📍 Sede de CorAll, Trujillo

Ingreso libre con inscripción.""",
        fb="Puertas abiertas en nuestro laboratorio para universitarios: sábado 13 de diciembre, 10:00 a 13:00, sede de CorAll en Trujillo. Ingreso libre con inscripción.",
        ig="""🚪 Puertas abiertas.
Sábado 13 de diciembre, 10:00 a 13:00. Conoce nuestro laboratorio de hardware e IA. Ingreso libre con inscripción.""",
        tt=[("Puerta del laboratorio abriéndose", "Abrimos las puertas de nuestro laboratorio."),
            ("Prototipos y demos de IA", "Conoce nuestros prototipos y demos de inteligencia artificial."),
            ("Fecha en pantalla", "Sábado 13 de diciembre, 10:00. Ingreso libre con inscripción.")],
        tit="Conoce nuestro laboratorio", bul=[("Sábado 13 de diciembre", "De 10:00 a 13:00."),
                                               ("Hardware e IA", "Demos en vivo."),
                                               ("Ingreso libre", "Con inscripción.")],
        dato="Sábado 13 de diciembre, 10:00", cta="Inscríbete",
        tags=["#PuertasAbiertas", "#Universitarios", "#Innovación", "#Trujillo"],
        vis="Open laboratory door revealing workbenches with prototypes, bright inviting light",
    ),
    dict(
        id="in21", area="innovacion", sector="minería", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se actualizó el portafolio de servicios para el sector minero: monitoreo ambiental, telemetría de equipos, seguridad del personal y mantenimiento predictivo, cada uno con un caso de referencia anonimizado",
        fuente="Portafolio de soluciones para minería", valor=4,
        razon="Catálogo propio terminado; contenido comercial sin datos sensibles.",
        li="""Soluciones para minería, diseñadas e integradas en Trujillo.

Actualizamos nuestro portafolio para el sector minero con cuatro líneas de trabajo:

- Monitoreo ambiental
- Telemetría de equipos
- Seguridad del personal
- Mantenimiento predictivo

En cada una diseñamos el dispositivo, el modelo que interpreta el dato y la plataforma donde se decide. ¿Cuál es el reto de tu operación? Conversemos.""",
        fb="Nuestro portafolio para minería: monitoreo ambiental, telemetría de equipos, seguridad del personal y mantenimiento predictivo. ¿Cuál necesitas?",
        ig="""⛏️ Soluciones para minería.
Monitoreo ambiental, telemetría, seguridad del personal y mantenimiento predictivo.""",
        tt=[("Paisaje minero", "¿Qué necesita una operación minera?"),
            ("Íconos de las cuatro soluciones", "Monitoreo ambiental, telemetría, seguridad y mantenimiento predictivo."),
            ("Plataforma con datos", "Del dispositivo a la decisión, todo integrado.")],
        tit="Soluciones para minería", bul=[("Monitoreo ambiental", "Polvo y gases."),
                                            ("Telemetría", "Equipos conectados."),
                                            ("Seguridad y mantenimiento", "Personal y máquinas.")],
        dato=None, cta="Conversemos",
        tags=["#Minería", "#Innovación", "#IoT", "#SeguridadIndustrial"],
        vis="Grid of four line icons over a mining landscape background: dust cloud, truck, helmet, gear",
        comp="grilla",
    ),
    dict(
        id="in22", area="innovacion", sector="agroindustria", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se terminó el portafolio para agroindustria: sensores de campo, visión artificial en empaque, trazabilidad por lote y apps de cosecha, con un caso de referencia anonimizado por solución",
        fuente="Portafolio de soluciones para agroindustria", valor=4,
        razon="Catálogo propio terminado; contenido comercial sin riesgos.",
        li="""Del campo a la planta de empaque: tecnología para la agroindustria.

Ordenamos nuestro portafolio para el sector agro en cuatro soluciones:

- Sensores de campo para clima, suelo y riego
- Visión artificial en la línea de empaque
- Trazabilidad por lote
- Apps de registro de cosecha

Cada una ya tiene un caso de referencia en la región. ¿Cuál necesita tu operación? Escríbenos.""",
        fb="Nuestro portafolio para agroindustria: sensores de campo, visión artificial en empaque, trazabilidad por lote y apps de cosecha.",
        ig="""🌿 Tecnología para la agroindustria.
Sensores de campo, visión artificial en empaque, trazabilidad por lote y apps de cosecha.""",
        tt=[("Campo agrícola al amanecer", "Del campo..."),
            ("Línea de empaque con cámaras", "...a la planta de empaque."),
            ("Íconos de las cuatro soluciones", "Sensores, visión artificial, trazabilidad y apps de cosecha.")],
        tit="Tecnología para el agro", bul=[("Sensores de campo", "Clima, suelo y riego."),
                                            ("Visión en empaque", "Conteo y calibre."),
                                            ("Trazabilidad y cosecha", "Por lote.")],
        dato=None, cta="Escríbenos",
        tags=["#Agroindustria", "#AgriculturaDePrecisión", "#Innovación", "#Trazabilidad"],
        vis="Split composition of a green field with sensors and a packing line with cameras",
        comp="grilla",
    ),
    dict(
        id="in23", area="innovacion", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Celebración del Día del Ingeniero con el equipo: reconocimiento a los ingenieros de las 4 áreas; foto grupal autorizada",
        fuente="Día del Ingeniero", valor=3,
        razon="Fecha especial de cultura con consentimiento para la foto.",
        li="""Feliz Día del Ingeniero.

A quienes diseñan, prueban, fallan, ajustan y vuelven a probar hasta que funciona.

Hoy celebramos a los ingenieros de nuestras 4 áreas: innovación, software, inteligencia artificial y hardware. Gracias por convertir los problemas de nuestros clientes en soluciones reales.

¡Feliz día, equipo!""",
        fb="¡Feliz Día del Ingeniero! Gracias a los ingenieros de nuestras 4 áreas por convertir problemas en soluciones reales.",
        ig="""🛠️ ¡Feliz Día del Ingeniero!
A quienes diseñan, prueban, ajustan y vuelven a probar hasta que funciona.""",
        tt=[("Planos y herramientas sobre una mesa", "Diseñar, probar, ajustar..."),
            ("Prototipo funcionando", "...y volver a probar hasta que funciona."),
            ("Foto grupal con overlay rojo", "¡Feliz Día del Ingeniero, equipo!")],
        tit="Feliz Día del Ingeniero", bul=[("Diseñar", "Con propósito."),
                                            ("Probar", "Una y otra vez."),
                                            ("Resolver", "Problemas reales.")],
        dato=None, cta="Conoce al equipo",
        tags=["#DíaDelIngeniero", "#CulturaCorAll", "#Ingeniería", "#EquipoCorAll"],
        vis="Engineering blueprints, calipers and a small prototype on a desk with celebratory red accents",
        adj="equipo",
    ),
    dict(
        id="in24", area="innovacion", sector="logística y transporte", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Primer año de trabajo con un cliente de transporte con autorización para mencionarlo sin nombre: de un piloto de telemetría a 3 soluciones en operación (telemetría, app de despachos y mantenimiento predictivo)",
        fuente="Un año de trabajo con un cliente de transporte", valor=4,
        razon="Hito de relación comercial con autorización; se cuenta sin nombre.",
        li="""Un año juntos: de un piloto a 3 soluciones en operación.

Hace un año empezamos con una empresa de transporte con un piloto de telemetría. Hoy trabajamos con 3 soluciones en operación: telemetría de flota, app de despachos y mantenimiento predictivo.

Cada paso se dio después de demostrar resultados en el anterior.

Gracias por la confianza. Las relaciones de largo plazo se construyen con resultados.""",
        fb="Un año con una empresa de transporte: empezamos con un piloto y hoy son 3 soluciones en operación. Gracias por la confianza.",
        ig="""🤝 Un año juntos.
De un piloto de telemetría a 3 soluciones en operación con una empresa de transporte.""",
        tt=[("Un solo camión con un equipo instalado", "Hace un año empezamos con un piloto."),
            ("Tres íconos apareciendo", "Hoy son 3 soluciones en operación."),
            ("Flota en ruta", "Telemetría, despachos y mantenimiento predictivo.")],
        tit="Un año, 3 soluciones", bul=[("Piloto inicial", "Telemetría."),
                                         ("3 soluciones", "En operación."),
                                         ("Resultados", "En cada paso.")],
        dato="De un piloto a 3 soluciones", cta="Conversemos",
        tags=["#Logística", "#Transporte", "#Innovación", "#Telemetría"],
        vis="Fleet of trucks on a highway at sunset with three glowing icons above them",
        comp="línea de tiempo",
    ),
    dict(
        id="in25", area="innovacion", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Contenido sobre cómo elegir un proveedor de tecnología: que muestre casos reales, que proponga un piloto antes de un contrato grande y que explique con claridad qué no puede hacer",
        fuente="Cómo elegir un proveedor de tecnología", valor=4,
        razon="Contenido educativo general y honesto para potenciales clientes.",
        li="""Antes de contratar a un proveedor de tecnología, hazle estas tres preguntas.

1. ¿Puedes mostrarme un caso real parecido al mío?
2. ¿Podemos empezar con un piloto antes de un contrato grande?
3. ¿Qué no puede hacer tu solución?

Un buen proveedor responde las tres con claridad, incluida la tercera. ¿Qué otra pregunta harías tú?""",
        fb="3 preguntas para elegir un proveedor de tecnología: ¿tienes un caso real?, ¿empezamos con un piloto? y ¿qué no puede hacer tu solución?",
        ig="""❓ 3 preguntas antes de contratar tecnología.
¿Tienes un caso real? ¿Empezamos con un piloto? ¿Qué no puede hacer tu solución?""",
        tt=[("Reunión con laptop (sin rostros)", "Antes de contratar a un proveedor de tecnología..."),
            ("Tres preguntas apareciendo", "Pregunta por un caso real y por un piloto."),
            ("Pregunta final resaltada", "Y pregunta qué no puede hacer su solución.")],
        tit="Antes de contratar tecnología", bul=[("Caso real", "Parecido al tuyo."),
                                                  ("Piloto primero", "Antes del contrato."),
                                                  ("Qué no puede hacer", "Con claridad.")],
        dato=None, cta="Cuéntanos",
        tags=["#TransformaciónDigital", "#Pymes", "#Innovación", "#BuenasPrácticas"],
        vis="3D illustration of three speech bubbles with question marks over a meeting table",
    ),
]
