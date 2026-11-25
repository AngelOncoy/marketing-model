"""Second set of publishable tasks (v0.2): AI and innovation."""

CARDS = [
    # ---------------- ia ----------------
    dict(
        id="ia26", area="ia", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="vision-grado-cuero",
        det="Entrega del modelo de clasificación de cuero por calidad para {cliente}: separa 3 grados a partir de una foto de la pieza; en 250 piezas coincidió con el clasificador experto en 87 % de los casos.",
        fuente="Clasificación de cuero por calidad con visión artificial", valor=5,
        razon="Modelo entregado con validación medible; se cuenta sin nombrar al cliente.",
        li="""Clasificar cuero por calidad depende del ojo de un experto. Ahora también de una cámara.

Entregamos a una curtiembre un modelo de visión artificial que separa el cuero en 3 grados a partir de una foto de la pieza.

En una prueba con 250 piezas, coincidió con el clasificador experto en el 87 % de los casos.

El experto sigue decidiendo; el modelo le ahorra la primera revisión. ¿Tu planta clasifica a ojo? Cuéntanos tu caso.""",
        fb="Modelo de visión artificial para clasificar cuero en 3 grados: en 250 piezas coincidió con el experto en el 87 % de los casos.",
        ig="""🐄 Calidad de cuero, vista por una cámara.
3 grados de calidad a partir de una foto. 87 % de coincidencia con el experto en 250 piezas.""",
        tt=[("Pieza de cuero bajo una cámara", "¿Se puede clasificar cuero con una foto?"),
            ("Pantalla con el grado asignado", "Nuestro modelo separa 3 grados de calidad."),
            ("Experto revisando piezas, sin rostro", "En 250 piezas coincidió con el experto en 87 % de los casos.")],
        tit="Calidad de cuero con una foto", bul=[("Tres grados", "Clasificación automática."),
                                                  ("Primera revisión rápida", "El experto confirma."),
                                                  ("Validado con expertos", "Comparado pieza por pieza.")],
        dato="87 % de coincidencia en 250 piezas", cta="Cuéntanos tu caso",
        tags=["#VisiónArtificial", "#Cuero", "#Calzado", "#InteligenciaArtificial"],
        vis="Leather hide on an inspection table under an overhead camera with subtle grading overlay boxes",
    ),
    dict(
        id="ia27", area="ia", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="prediccion-combustible",
        det="Modelo de predicción de consumo de combustible para la flota de {cliente}: estima el consumo por ruta y carga; con 2 meses de datos, el error promedio fue de 6 %.",
        fuente="Predicción de consumo de combustible", valor=4,
        razon="Modelo con resultado medible; útil para el sector sin datos del cliente.",
        li="""¿Cuánto combustible debería gastar un camión en esta ruta, con esta carga?

Entregamos a una operación minera un modelo que estima el consumo de combustible por ruta y por carga.

Con 2 meses de datos, el error promedio fue de 6 %. Eso permite detectar consumos fuera de lo esperado y planificar mejor el abastecimiento.

¿Tu flota tiene datos que todavía no estás usando? Conversemos.""",
        fb="Modelo de IA que estima el consumo de combustible por ruta y carga para una flota minera, con 6 % de error promedio.",
        ig="""⛽ Combustible estimado, no adivinado.
Un modelo que predice el consumo por ruta y carga, con 6 % de error promedio.""",
        tt=[("Camión minero cargado en ruta", "¿Cuánto debería gastar este camión?"),
            ("Gráfico de consumo por ruta", "Nuestro modelo lo estima por ruta y por carga."),
            ("Alerta de consumo inusual", "Y ayuda a detectar consumos fuera de lo esperado.")],
        tit="Combustible estimado con IA", bul=[("Por ruta y carga", "Estimación a medida."),
                                                ("Consumos inusuales", "Detectados a tiempo."),
                                                ("Mejor abastecimiento", "Planificado con datos.")],
        dato="6 % de error promedio", cta="Conversemos",
        tags=["#Minería", "#InteligenciaArtificial", "#AnálisisDeDatos", "#GestiónDeFlotas"],
        vis="Mining haul trucks on a dusty road with a translucent line chart overlay of fuel consumption",
    ),
    dict(
        id="ia28", area="ia", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="lectura-placas",
        det="Lectura automática de placas en la garita de {cliente}: registra el ingreso y la salida de los camiones sin digitación y no guarda imágenes de personas; en la prueba de 1 semana leyó bien el 96 % de las placas.",
        fuente="Lectura automática de placas en garita", valor=5,
        razon="Solución entregada con resultado medible y cuidado de la privacidad.",
        li="""En la garita, cada camión que entra se anotaba a mano. Ya no.

Instalamos para una empresa de transporte un sistema que lee automáticamente las placas y registra el ingreso y la salida de cada camión. No guarda imágenes de personas.

En la prueba de 1 semana leyó bien el 96 % de las placas.

Menos colas en la garita y un registro confiable. ¿Te interesa para tu patio? Conversemos.""",
        fb="Lectura automática de placas en garita: ingreso y salida de camiones sin digitación, con 96 % de lecturas correctas en la prueba.",
        ig="""🚛 La garita que anota sola.
Lectura automática de placas: 96 % de acierto en la prueba, sin guardar imágenes de personas.""",
        tt=[("Camión llegando a una garita", "¿Todavía anotas a mano cada camión que entra?"),
            ("Cámara leyendo una placa", "Este sistema lee la placa y registra el ingreso."),
            ("Registro en pantalla", "En la prueba leyó bien el 96 % de las placas.")],
        tit="La garita que anota sola", bul=[("Lectura de placas", "Sin digitación."),
                                             ("Ingreso y salida", "Registro automático."),
                                             ("Sin imágenes personales", "Privacidad cuidada.")],
        dato="96 % de placas leídas correctamente", cta="Conversemos",
        tags=["#VisiónArtificial", "#Logística", "#InteligenciaArtificial", "#Automatización"],
        vis="Truck entering a logistics yard gate with a mounted camera and a subtle recognition frame over a blank plate",
    ),
    dict(
        id="ia29", area="ia", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/resumenes",
        det="Resumen automático de reportes diarios en el ERP: cada jefe de proyecto recibe por la tarde un resumen de 5 líneas por proyecto; 12 proyectos activos ya usan la función.",
        fuente="Resumen automático de reportes en el ERP", valor=4,
        razon="Función propia terminada y en uso; no expone datos de clientes.",
        li="""Leer todos los reportes del día no debería ser otra tarea más.

En nuestro ERP, cada jefe de proyecto recibe ahora por la tarde un resumen de 5 líneas por proyecto, generado con IA a partir de los reportes del equipo.

Ya lo usan 12 proyectos activos.

Lo construimos primero para nosotros. ¿Tu equipo también se ahoga en reportes? Conversemos.""",
        fb="Nuestro ERP ahora resume con IA los reportes diarios: 5 líneas por proyecto para cada jefe. Ya lo usan 12 proyectos.",
        ig="""🧠 Reportes resumidos con IA.
5 líneas por proyecto cada tarde. Ya lo usan 12 proyectos en nuestro ERP.""",
        tt=[("Pila de reportes en pantalla", "¿Cuánto tiempo pasas leyendo reportes?"),
            ("Resumen corto en el celular", "Nuestro ERP los resume en 5 líneas por proyecto."),
            ("Equipo revisando el resumen", "Ya lo usan 12 proyectos.")],
        tit="Reportes resumidos con IA", bul=[("Cinco líneas", "Por proyecto."),
                                              ("Cada tarde", "Automático."),
                                              ("Hecho en casa", "Lo usamos a diario.")],
        dato="12 proyectos usando la función", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#ERP", "#Productividad", "#IA"],
        vis="Laptop mockup of an ERP screen showing short project summaries in cards with a soft red highlight",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="ia30", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó un artículo para redes: qué es el ajuste fino de un modelo de lenguaje y cuándo conviene frente a escribir mejores instrucciones",
        fuente="Ajuste fino o mejores instrucciones", valor=3,
        razon="Contenido educativo sobre IA; no revela información interna.",
        li="""¿Entrenar tu propio modelo de IA o escribir mejores instrucciones?

Escribir mejores instrucciones es rápido y barato: sirve cuando la tarea es general y los ejemplos caben en el mensaje.

El ajuste fino entrena el modelo con cientos de ejemplos tuyos: conviene cuando necesitas un formato fijo, un tono propio o que los datos no salgan de tu empresa.

Casi siempre se empieza por las instrucciones. ¿Quieres saber cuál te conviene? Escríbenos.""",
        fb="¿Ajuste fino o mejores instrucciones? Empieza por las instrucciones; el ajuste fino conviene cuando necesitas formato fijo, tono propio o privacidad.",
        ig="""🤖 ¿Entrenar tu modelo o mejorar tus instrucciones?
Casi siempre se empieza por las instrucciones. El ajuste fino llega después.""",
        tt=[("Persona escribiendo en un chat de IA", "¿Necesitas entrenar tu propio modelo de IA?"),
            ("Instrucción clara en pantalla", "Muchas veces basta con escribir mejores instrucciones."),
            ("Carpeta con ejemplos", "El ajuste fino conviene cuando necesitas formato, tono o privacidad.")],
        tit="¿Entrenar o instruir mejor?", bul=[("Instrucciones primero", "Rápido y barato."),
                                                ("Ajuste fino después", "Con ejemplos propios."),
                                                ("Privacidad de datos", "Un motivo clave.")],
        dato=None, cta="Escríbenos",
        tags=["#InteligenciaArtificial", "#IA", "#Tips", "#ModelosDeLenguaje"],
        vis="3D illustration of a chat bubble on one side and a small neural network with a gear on the other, balanced composition",
    ),
    dict(
        id="ia31", area="ia", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó un post explicativo: cuándo conviene procesar la IA en el propio celular o equipo de campo, sin internet, y cuándo enviarla a la nube",
        fuente="IA en el dispositivo o en la nube", valor=3,
        razon="Contenido educativo útil para clientes de campo; sin datos internos.",
        li="""En el campo no siempre hay señal. ¿Puede funcionar la IA igual?

Sí: un modelo pequeño puede correr en el propio celular o en un equipo de campo, sin internet. Es ideal para contar, detectar o clasificar en el momento.

Cuando el análisis es pesado o junta datos de muchos lugares, conviene enviarlo a la nube cuando vuelve la señal.

Lo más práctico suele ser combinar ambas. ¿Tu operación está lejos de la señal? Escríbenos.""",
        fb="¿IA sin internet? Un modelo pequeño puede correr en el celular o en un equipo de campo; lo pesado se envía a la nube cuando vuelve la señal.",
        ig="""📵 IA sin señal.
Modelos pequeños que corren en el celular o en equipos de campo, sin internet.""",
        tt=[("Celular sin señal en el campo", "¿Y si en el campo no hay internet?"),
            ("Celular detectando hojas", "Un modelo pequeño puede correr en el mismo celular."),
            ("Ícono de nube", "Y lo pesado se envía a la nube cuando vuelve la señal.")],
        tit="IA que funciona sin señal", bul=[("En el dispositivo", "Sin internet."),
                                              ("En la nube", "Análisis pesados."),
                                              ("Combinadas", "Lo más práctico.")],
        dato=None, cta="Escríbenos",
        tags=["#InteligenciaArtificial", "#Agroindustria", "#Tips", "#IA"],
        vis="3D illustration of a smartphone in a field with a crossed signal icon and a small cloud waiting above",
    ),
    dict(
        id="ia32", area="ia", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Se cerró una campaña completa del conteo de palta por cámara en la planta de {cliente}; el cliente autorizó compartir sin su nombre que se contaron más de 4 millones de frutos",
        fuente="Una campaña completa de conteo por cámara", valor=5,
        razon="Hito autorizado por el cliente con una cifra clara.",
        li="""Más de 4 millones de paltas contadas por una cámara.

Cerramos una campaña completa de nuestro sistema de conteo por visión artificial en una planta de empaque de la región.

Fruta por fruta, sin detener la faja y con un registro para cada lote.

Gracias al equipo de planta por confiar en la IA hecha en Trujillo. Vamos por la siguiente campaña.""",
        fb="Una campaña completa de conteo de palta por visión artificial: más de 4 millones de frutos contados en una planta de empaque.",
        ig="""🥑 Más de 4 millones de paltas contadas.
Una campaña completa de conteo por cámara, sin detener la faja.""",
        tt=[("Faja con paltas en movimiento", "¿Cuántas paltas pasan por esta faja?"),
            ("Recuadros sobre cada fruta", "Nuestro sistema las cuenta una por una."),
            ("Contador final en pantalla", "Esta campaña: más de 4 millones.")],
        tit="Millones de paltas contadas", bul=[("Campaña completa", "Sin detener la faja."),
                                                ("Registro por lote", "Datos para la planta."),
                                                ("IA hecha en Trujillo", "Diseño propio.")],
        dato="Más de 4 millones de frutos", cta="Conoce más",
        tags=["#VisiónArtificial", "#Palta", "#Agroindustria", "#InteligenciaArtificial"],
        vis="Avocado packing line seen from above with many fruits and subtle bounding boxes, a large counter glow",
    ),
    dict(
        id="ia33", area="ia", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller virtual 'IA para tu negocio sin programar': martes 1 de diciembre, 19:00, gratuito, inscripción por mensaje directo",
        fuente="Taller virtual de IA sin programar", valor=4,
        razon="Evento propio confirmado con fecha y modalidad.",
        li="""¿Quieres usar IA en tu negocio pero no sabes programar?

Te invitamos a nuestro taller virtual y gratuito "IA para tu negocio sin programar". Veremos ejemplos prácticos para responder clientes, ordenar información y redactar mejor.

📅 Martes 1 de diciembre
🕖 19:00
💻 Virtual

Inscríbete por mensaje directo.""",
        fb="Taller virtual gratuito 'IA para tu negocio sin programar': martes 1 de diciembre, 19:00. Inscríbete por mensaje directo.",
        ig="""🤖 IA para tu negocio, sin programar.
Taller virtual gratuito: martes 1 de diciembre, 19:00.""",
        tt=[("Emprendedora frente a su laptop, sin rostro", "¿Quieres usar IA sin saber programar?"),
            ("Ejemplos de IA en pantalla", "Te mostramos ejemplos prácticos para tu negocio."),
            ("Fecha en pantalla", "Martes 1 de diciembre, 19:00, gratis.")],
        tit="IA sin programar", bul=[("Martes 1 de diciembre", "A las 19:00."),
                                     ("Virtual y gratuito", "Desde donde estés."),
                                     ("Ejemplos prácticos", "Para tu negocio.")],
        dato="Martes 1 de diciembre, 19:00", cta="Inscríbete",
        tags=["#InteligenciaArtificial", "#Mypes", "#TallerGratuito", "#IA"],
        vis="Laptop on a small business counter showing a friendly AI chat, warm light and red geometric accents",
    ),
    dict(
        id="ia34", area="ia", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Sesión interna de demos del mes: cada integrante del equipo de IA mostró en 5 minutos lo que construyó y lo que aprendió",
        fuente="Sesión mensual de demos del equipo de IA", valor=3,
        razon="Actividad de cultura interna sin información sensible.",
        li="""5 minutos para mostrar lo que construiste en el mes.

Así son las sesiones de demos de nuestro equipo de IA: cada integrante muestra un avance terminado y cuenta qué aprendió, incluso de lo que no salió como esperaba.

Compartir lo aprendido evita que dos personas tropiecen con la misma piedra.

Así trabajamos en CorAll.""",
        fb="Sesión de demos del equipo de IA: 5 minutos por persona para mostrar lo construido y lo aprendido en el mes.",
        ig="""🎤 5 minutos, una demo.
Cada mes, el equipo de IA muestra lo que construyó y lo que aprendió.""",
        tt=[("Proyector encendido en una sala", "5 minutos para mostrar lo que construiste."),
            ("Demo en pantalla", "Cada integrante muestra un avance terminado."),
            ("Equipo aplaudiendo, sin rostros", "Y cuenta lo que aprendió en el camino.")],
        tit="Cinco minutos, una demo", bul=[("Demos mensuales", "Cada integrante."),
                                            ("Lo construido", "Avances terminados."),
                                            ("Lo aprendido", "Incluso los tropiezos.")],
        dato=None, cta="Conoce más",
        tags=["#CulturaCorAll", "#InteligenciaArtificial", "#Aprendizaje", "#TrabajoEnEquipo"],
        vis="Small meeting room with a projector showing an abstract AI demo screen, chairs and laptops, no faces",
    ),
    dict(
        id="ia35", area="ia", sector="minería", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Instalación en sitio de las cámaras del detector de casco y chaleco en 2 accesos de {cliente}; el cliente autorizó publicar fotos de los equipos, sin rostros y sin su nombre",
        fuente="Instalación en sitio del detector de equipo de protección", valor=4,
        razon="Trabajo en sitio autorizado; las fotos no muestran personas.",
        li="""La IA también se instala con casco y chaleco.

Esta semana nuestro equipo estuvo en una operación minera instalando las cámaras del detector de equipo de protección en 2 accesos.

Ajustamos ángulos, iluminación y la alerta al supervisor en el mismo punto de ingreso.

Llevar un modelo del laboratorio al campo es parte del trabajo. ¿Hablamos de tu operación?""",
        fb="Instalamos en sitio las cámaras del detector de casco y chaleco en 2 accesos de una operación minera.",
        ig="""⛑️ IA instalada en el punto de ingreso.
Cámaras del detector de casco y chaleco en 2 accesos de una operación minera.""",
        tt=[("Acceso de una planta minera", "Instalamos IA en el punto de ingreso."),
            ("Técnico ajustando una cámara", "Ajustamos ángulos e iluminación."),
            ("Alerta en la tablet del supervisor", "Para avisar si alguien entra sin equipo completo.")],
        tit="IA en el punto de ingreso", bul=[("Dos accesos", "Cámaras instaladas."),
                                              ("Ajuste en sitio", "Ángulo e iluminación."),
                                              ("Alerta al supervisor", "En el mismo ingreso.")],
        dato=None, cta="Conversemos",
        tags=["#VisiónArtificial", "#Minería", "#SeguridadIndustrial", "#InteligenciaArtificial"],
        vis="Mining site entrance gate with a mounted camera and a technician's gloved hands adjusting it, no faces",
        adj="campo",
    ),
    dict(
        id="ia36", area="ia", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="corrector-informes",
        det="Corrector de redacción para los informes de prácticas de {cliente}: sugiere mejoras de claridad y ortografía sin escribir por el alumno; 180 alumnos lo usaron en el primer mes. La institución autorizó compartirlo sin su nombre.",
        fuente="Corrector de redacción para informes de prácticas", valor=4,
        razon="Producto entregado con uso real y autorización para difundir sin nombre.",
        li="""Una IA que ayuda a escribir mejor, sin escribir por el alumno.

Entregamos a una institución educativa un corrector para los informes de prácticas: señala frases poco claras y errores de ortografía, y sugiere cómo mejorarlas. El texto lo sigue escribiendo el alumno.

En el primer mes lo usaron 180 alumnos.

IA para aprender, no para copiar. ¿Te interesa para tu institución? Conversemos.""",
        fb="Corrector de redacción con IA para informes de prácticas: sugiere mejoras sin escribir por el alumno. 180 alumnos lo usaron en el primer mes.",
        ig="""✍️ IA para escribir mejor, no para copiar.
Sugiere mejoras de claridad y ortografía. 180 alumnos en el primer mes.""",
        tt=[("Alumno escribiendo en la laptop", "¿Una IA que no escribe por ti?"),
            ("Sugerencias subrayadas en el texto", "Señala lo poco claro y sugiere cómo mejorarlo."),
            ("Contador de usuarios", "180 alumnos lo usaron en el primer mes.")],
        tit="Escribir mejor, no copiar", bul=[("Claridad", "Frases más simples."),
                                              ("Ortografía", "Errores señalados."),
                                              ("El alumno escribe", "La IA solo sugiere.")],
        dato="180 alumnos en el primer mes", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#Educación", "#Redacción", "#IA"],
        vis="Laptop mockup showing a document with gentle highlighted suggestions in the margin, student desk with notebooks",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="ia37", area="ia", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="pronostico-cosecha",
        det="Modelo de pronóstico de cosecha semanal para {cliente}: estima los kilos por lote con 3 semanas de anticipación; en la campaña pasada el error fue de 9 %.",
        fuente="Pronóstico semanal de cosecha", valor=5,
        razon="Modelo entregado con validación sobre una campaña real; sin datos del cliente.",
        li="""¿Cuántos kilos vas a cosechar dentro de 3 semanas?

Entregamos a una empresa agroexportadora un modelo que pronostica los kilos por lote con 3 semanas de anticipación.

Validado con la campaña pasada, el error fue de 9 %. Con ese margen ya se pueden planificar cuadrillas, jabas y transporte.

Planificar con datos, no con intuición. ¿Hablamos de tu campaña?""",
        fb="Modelo de IA que pronostica la cosecha por lote con 3 semanas de anticipación, con 9 % de error en la campaña pasada.",
        ig="""📈 Tu cosecha, 3 semanas antes.
Pronóstico de kilos por lote con 9 % de error en la campaña pasada.""",
        tt=[("Campo de cultivo con lotes", "¿Cuánto vas a cosechar en 3 semanas?"),
            ("Gráfico de pronóstico por lote", "Nuestro modelo lo estima por lote."),
            ("Camiones y jabas listos", "Para planificar cuadrillas, jabas y transporte.")],
        tit="Tu cosecha, antes de tiempo", bul=[("Kilos por lote", "Pronóstico semanal."),
                                                ("Tres semanas antes", "Tiempo para planificar."),
                                                ("Validado en campaña", "Con datos reales.")],
        dato="9 % de error en la campaña pasada", cta="Conversemos",
        tags=["#Agroindustria", "#InteligenciaArtificial", "#AnálisisDeDatos", "#Agroexportación"],
        vis="Aerial view of crop lots with a translucent weekly forecast bar chart rising over the field, golden hour",
    ),
    dict(
        id="ia38", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó una guía corta para clientes: cómo escribir una buena instrucción para un asistente de IA (contexto, tarea, formato y un ejemplo)",
        fuente="Cómo escribir una buena instrucción para la IA", valor=3,
        razon="Contenido educativo general; no revela nada interno.",
        li="""La respuesta de una IA mejora mucho cuando la pregunta está bien hecha.

Una buena instrucción tiene 4 partes:
1. Contexto: quién eres y para qué lo necesitas.
2. Tarea: qué quieres exactamente.
3. Formato: lista, tabla, correo, cuántas líneas.
4. Un ejemplo de lo que esperas.

Pruébalo hoy con tu próxima consulta. ¿Quieres llevar esto a tu equipo? Escríbenos.""",
        fb="Una buena instrucción para la IA tiene contexto, tarea, formato y un ejemplo. Pruébalo en tu próxima consulta.",
        ig="""💬 Pregunta mejor, obtén mejores respuestas.
Contexto, tarea, formato y un ejemplo: las 4 partes de una buena instrucción.""",
        tt=[("Persona escribiendo una pregunta corta", "¿La IA te responde cosas genéricas?"),
            ("Instrucción con cuatro partes", "Agrega contexto, tarea, formato y un ejemplo."),
            ("Respuesta clara en pantalla", "Y la respuesta mejora al momento.")],
        tit="Pregunta mejor a la IA", bul=[("Contexto", "Quién y para qué."),
                                           ("Tarea y formato", "Qué y cómo."),
                                           ("Un ejemplo", "Lo que esperas.")],
        dato=None, cta="Escríbenos",
        tags=["#InteligenciaArtificial", "#Tips", "#Productividad", "#IA"],
        vis="3D illustration of a chat window with four stacked colored blocks forming a well structured message",
    ),
    dict(
        id="ia39", area="ia", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se preparó la ficha comercial de asistentes de IA: atención de preguntas frecuentes, búsqueda en documentos internos y clasificación de correos entrantes",
        fuente="Ficha comercial de asistentes de IA", valor=4,
        razon="Catálogo propio de servicios; contenido comercial público.",
        li="""Tres asistentes de IA que ya podemos poner a trabajar en tu empresa.

💬 Preguntas frecuentes: responde a tus clientes con tu información oficial y deriva a una persona cuando no sabe.
📂 Búsqueda en documentos: encuentra la respuesta en tus manuales y procedimientos.
📧 Clasificación de correos: ordena los mensajes que llegan y los envía al área correcta.

Hechos a medida y con tus datos bajo control. ¿Cuál necesitas? Escríbenos.""",
        fb="Asistentes de IA a medida: preguntas frecuentes, búsqueda en documentos y clasificación de correos, con tus datos bajo control.",
        ig="""🤖 Asistentes de IA para tu empresa.
Preguntas frecuentes, búsqueda en documentos y clasificación de correos.""",
        tt=[("Bandeja de correos llena", "Tres asistentes de IA para tu empresa."),
            ("Chat respondiendo una pregunta", "Uno responde preguntas frecuentes, otro busca en tus documentos."),
            ("Correos ordenados por área", "Y otro clasifica tus correos.")],
        tit="Asistentes de IA a medida", bul=[("Preguntas frecuentes", "Respuestas oficiales."),
                                              ("Búsqueda en documentos", "Manuales al instante."),
                                              ("Clasificación de correos", "Al área correcta.")],
        dato=None, cta="Escríbenos",
        tags=["#InteligenciaArtificial", "#Asistentes", "#Automatización", "#IA"],
        vis="Grid of three clean line icons for a chat bubble, a document folder and an envelope over a soft gradient",
        comp="grilla",
    ),
    dict(
        id="ia40", area="ia", sector="cuero y calzado", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Toma de 900 fotos de cortes de cuero en la planta de {cliente} para entrenar el modelo de defectos; el cliente autorizó compartir el trabajo sin su nombre",
        fuente="Toma de fotos en planta para entrenar un modelo", valor=3,
        razon="Trabajo de campo autorizado; muestra cómo se construye un modelo.",
        li="""Antes de entrenar un modelo, hay que salir a tomar fotos. Muchas fotos.

Esta semana estuvimos en una planta de cuero de la región y tomamos 900 fotos de cortes, con distinta luz, ángulo y tipo de defecto.

Un modelo solo aprende lo que ve. Por eso el trabajo empieza en la planta, no en la computadora.

¿Quieres saber qué datos necesitaría tu proceso? Conversemos.""",
        fb="900 fotos de cortes de cuero tomadas en planta para entrenar un modelo de detección de defectos.",
        ig="""📸 Un modelo aprende lo que ve.
Tomamos 900 fotos de cortes de cuero en planta para entrenar un modelo de defectos.""",
        tt=[("Cámara sobre un corte de cuero", "¿Cómo se entrena un modelo de visión?"),
            ("Fotos con distinta luz", "Primero se toman cientos de fotos en la planta."),
            ("Galería de fotos en la laptop", "Esta semana tomamos 900.")],
        tit="Un modelo aprende lo que ve", bul=[("Fotos en planta", "Condiciones reales."),
                                                ("Distinta luz", "Y distintos ángulos."),
                                                ("Defectos variados", "Para aprender bien.")],
        dato="900 fotos tomadas en planta", cta="Conversemos",
        tags=["#VisiónArtificial", "#Cuero", "#DatosDeEntrenamiento", "#InteligenciaArtificial"],
        vis="Leather cutting table under a camera on a tripod with soft even lighting, several leather pieces laid out",
    ),
    # ---------------- innovacion ----------------
    dict(
        id="in26", area="innovacion", sector="minería", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Taller de identificación de oportunidades digitales con 12 supervisores de {cliente}; se priorizaron 4 proyectos y el cliente autorizó compartir el trabajo sin su nombre",
        fuente="Taller de oportunidades digitales con supervisores", valor=4,
        razon="Servicio autorizado por el cliente; no expone su información.",
        li="""Las mejores ideas para digitalizar una operación las tiene quien la vive todos los días.

Esta semana facilitamos un taller con 12 supervisores de una operación minera para identificar oportunidades digitales en su trabajo diario.

Salieron muchas ideas y se priorizaron 4 proyectos con impacto claro y factibles de empezar.

Innovar empieza por escuchar. ¿Hacemos este ejercicio con tu equipo?""",
        fb="Taller de oportunidades digitales con 12 supervisores de una operación minera: 4 proyectos priorizados.",
        ig="""💡 Innovar empieza por escuchar.
12 supervisores, muchas ideas y 4 proyectos priorizados.""",
        tt=[("Pizarra llena de notas", "¿Quién sabe qué digitalizar en una operación?"),
            ("Supervisores trabajando en grupo, sin rostros", "Quienes la viven todos los días."),
            ("Cuatro tarjetas destacadas", "De este taller salieron 4 proyectos priorizados.")],
        tit="Innovar empieza por escuchar", bul=[("Doce supervisores", "Experiencia de campo."),
                                                 ("Ideas priorizadas", "Impacto y factibilidad."),
                                                 ("Cuatro proyectos", "Listos para empezar.")],
        dato="4 proyectos priorizados", cta="Conversemos",
        tags=["#Innovación", "#Minería", "#TransformaciónDigital", "#Talleres"],
        vis="Meeting room at a mining camp with a wall full of sticky notes and safety helmets on a side table, no faces",
    ),
    dict(
        id="in27", area="innovacion", sector="educación", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="CorAll fue seleccionada en una convocatoria regional de innovación para cofinanciar el piloto de trazabilidad por lote con QR; la convocatoria publicó los resultados",
        fuente="Selección en una convocatoria regional de innovación", valor=5,
        razon="Hito público e institucional; los resultados ya son públicos.",
        li="""Fuimos seleccionados en una convocatoria regional de innovación.

El proyecto que presentamos, un piloto de trazabilidad por lote con código QR para productores, recibirá cofinanciamiento para llevarlo a campo.

Es un reconocimiento al trabajo del equipo y una oportunidad para probar la solución con productores reales.

Gracias a todos los que nos ayudaron a preparar la propuesta. Ahora, a trabajar.""",
        fb="¡Fuimos seleccionados en una convocatoria regional de innovación para cofinanciar nuestro piloto de trazabilidad por lote con QR!",
        ig="""🏆 Seleccionados.
Nuestro piloto de trazabilidad por lote con QR recibirá cofinanciamiento regional.""",
        tt=[("Equipo celebrando, sin rostros", "Fuimos seleccionados en una convocatoria de innovación."),
            ("Caja con código QR", "Para nuestro piloto de trazabilidad por lote."),
            ("Campo de cultivo", "Ahora lo llevaremos a campo con productores.")],
        tit="Seleccionados para innovar", bul=[("Convocatoria regional", "De innovación."),
                                               ("Trazabilidad con QR", "El proyecto."),
                                               ("Piloto en campo", "Con productores.")],
        dato=None, cta="Conoce más",
        tags=["#Innovación", "#Trazabilidad", "#Agroindustria", "#HechoEnTrujillo"],
        vis="Crate of fresh produce with a QR label in soft light and a subtle award ribbon icon in brand red",
    ),
    dict(
        id="in28", area="innovacion", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se escribió un artículo: qué es un producto mínimo viable y cómo lo usamos con clientes para validar una idea antes de construir todo el sistema",
        fuente="Qué es un producto mínimo viable", valor=3,
        razon="Contenido educativo sobre la metodología propia; sin datos de clientes.",
        li="""Antes de construir todo el sistema, construimos lo mínimo para probar la idea.

Eso es un producto mínimo viable: la versión más simple que permite saber si la solución resuelve el problema.

Por ejemplo, antes de una app completa de pedidos, probamos con un formulario y una hoja compartida durante dos semanas. Si funciona, crecemos; si no, ajustamos sin haber gastado de más.

¿Tienes una idea que quieres validar? Conversemos.""",
        fb="Un producto mínimo viable es la versión más simple para probar si una idea funciona antes de construir todo el sistema.",
        ig="""🧪 Prueba la idea antes de construirla entera.
Eso es un producto mínimo viable: lo más simple que te dice si la solución funciona.""",
        tt=[("Boceto en papel de una app", "¿Vas a construir todo el sistema de una vez?"),
            ("Formulario simple en el celular", "Primero prueba la idea con lo mínimo."),
            ("Gráfico de crecimiento", "Si funciona, crece. Si no, ajusta sin gastar de más.")],
        tit="Prueba antes de construir", bul=[("Lo mínimo primero", "Para validar."),
                                              ("Aprender rápido", "Con usuarios reales."),
                                              ("Crecer con datos", "Sin gastar de más.")],
        dato=None, cta="Conversemos",
        tags=["#Innovación", "#Emprendimiento", "#Tips", "#TransformaciónDigital"],
        vis="3D illustration of a small paper prototype growing step by step into a complete app screen",
    ),
    dict(
        id="in29", area="innovacion", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el conversatorio 'Industria 4.0 en el norte del Perú': jueves 3 de diciembre, 17:00, en las oficinas de CorAll, cupos limitados",
        fuente="Conversatorio sobre Industria 4.0", valor=4,
        razon="Evento propio confirmado con fecha, hora y lugar.",
        li="""¿Cómo se ve la Industria 4.0 en las empresas del norte del Perú?

Te invitamos al conversatorio "Industria 4.0 en el norte del Perú", donde compartiremos casos reales de sensores, datos e IA aplicados en la región.

📅 Jueves 3 de diciembre
🕔 17:00
📍 Oficinas de CorAll, Trujillo

Cupos limitados. Escríbenos para reservar tu lugar.""",
        fb="Conversatorio 'Industria 4.0 en el norte del Perú': jueves 3 de diciembre, 17:00, en nuestras oficinas de Trujillo. Cupos limitados.",
        ig="""🏭 Industria 4.0 en el norte del Perú.
Conversatorio: jueves 3 de diciembre, 17:00, en nuestras oficinas de Trujillo.""",
        tt=[("Planta industrial con sensores", "¿Cómo se ve la Industria 4.0 en el norte?"),
            ("Sala preparada para el conversatorio", "Te contamos casos reales de la región."),
            ("Fecha en pantalla", "Jueves 3 de diciembre, 17:00.")],
        tit="Industria 4.0 en el norte", bul=[("Jueves 3 de diciembre", "A las 17:00."),
                                              ("Casos reales", "De la región."),
                                              ("Cupos limitados", "Reserva tu lugar.")],
        dato="Jueves 3 de diciembre, 17:00", cta="Reserva tu lugar",
        tags=["#Industria40", "#Innovación", "#Trujillo", "#Conversatorio"],
        vis="Modern meeting room arranged for a talk with empty chairs, a screen with an abstract factory diagram and red accents",
    ),
    dict(
        id="in30", area="innovacion", sector="cuero y calzado", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Mapeo del proceso de producción en la fábrica de {cliente}: se identificaron 3 cuellos de botella entre corte y aparado; el cliente autorizó compartir el trabajo sin su nombre",
        fuente="Mapeo de procesos en una fábrica de calzado", valor=4,
        razon="Servicio autorizado por el cliente, sin datos que lo identifiquen.",
        li="""Antes de digitalizar un proceso, hay que verlo completo.

Esta semana recorrimos con el equipo de una fábrica de calzado todo su proceso de producción, del corte al despacho.

Encontramos 3 cuellos de botella entre corte y aparado: esperas, traslados y pedidos que se reordenaban a mano.

Con ese mapa ya se sabe dónde la tecnología ayuda de verdad. ¿Hacemos lo mismo en tu planta?""",
        fb="Mapeamos el proceso de una fábrica de calzado y encontramos 3 cuellos de botella entre corte y aparado.",
        ig="""👞 Ver el proceso completo.
Encontramos 3 cuellos de botella entre corte y aparado en una fábrica de calzado.""",
        tt=[("Zona de corte de cuero", "¿Dónde se pierde tiempo en una fábrica de calzado?"),
            ("Diagrama de proceso en una pizarra", "Recorrimos el proceso del corte al despacho."),
            ("Tres puntos rojos en el diagrama", "Y encontramos 3 cuellos de botella.")],
        tit="Ver el proceso completo", bul=[("Del corte al despacho", "Todo el recorrido."),
                                            ("Cuellos de botella", "Identificados."),
                                            ("Tecnología donde ayuda", "No en todas partes.")],
        dato="3 cuellos de botella identificados", cta="Conversemos",
        tags=["#Calzado", "#Innovación", "#MejoraDeProcesos", "#TransformaciónDigital"],
        vis="Shoe factory floor with cutting and stitching stations and a translucent process flow diagram with three red markers",
    ),
    dict(
        id="in31", area="innovacion", sector="agroindustria", tipo="interno", pilar="producto",
        sec="matriz", mod="alerta-heladas",
        det="Prototipo de alerta de heladas por SMS para pequeños productores: combina el pronóstico del tiempo con una estación cercana y envía el aviso la tarde anterior; probado con 15 productores durante 2 semanas.",
        fuente="Prototipo de alerta de heladas por SMS", valor=4,
        razon="Prototipo propio probado con usuarios reales; aporta al sector.",
        li="""Una helada avisada la tarde anterior es una helada que se puede enfrentar.

Probamos un prototipo de alerta de heladas para pequeños productores: combina el pronóstico del tiempo con una estación cercana y envía el aviso por SMS la tarde anterior.

Lo usaron 15 productores durante 2 semanas, con un celular simple y sin internet.

Innovación que llega a quien más la necesita. ¿Trabajas con productores? Conversemos.""",
        fb="Prototipo de alerta de heladas por SMS para pequeños productores: aviso la tarde anterior, probado con 15 productores.",
        ig="""❄️ La helada, avisada a tiempo.
Alerta por SMS la tarde anterior, probada con 15 productores.""",
        tt=[("Campo al amanecer con escarcha", "¿Y si supieras de la helada un día antes?"),
            ("Celular simple recibiendo un SMS", "Este prototipo avisa por SMS la tarde anterior."),
            ("Productor revisando su cultivo, sin rostro", "Lo probamos con 15 productores.")],
        tit="La helada, avisada a tiempo", bul=[("Aviso por SMS", "Sin internet."),
                                                ("La tarde anterior", "Tiempo para actuar."),
                                                ("Para pequeños productores", "Celular simple.")],
        dato="Probado con 15 productores", cta="Conversemos",
        tags=["#Innovación", "#Agroindustria", "#Clima", "#PequeñosProductores"],
        vis="Frosted crop field at dawn with a simple mobile phone in the foreground showing a message icon",
    ),
    dict(
        id="in32", area="innovacion", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Arrancó el programa de mentoría interna: cada practicante tiene un mentor del equipo para su primer semestre; empezó con 5 parejas",
        fuente="Programa de mentoría interna", valor=3,
        razon="Iniciativa de cultura interna sin información sensible.",
        li="""Nadie debería aprender solo en su primer trabajo.

Arrancamos nuestro programa de mentoría interna: cada practicante tiene un mentor del equipo que lo acompaña durante su primer semestre.

Empezamos con 5 parejas, con reuniones semanales para revisar avances, dudas y objetivos.

Así formamos el talento que la región necesita.""",
        fb="Arrancó nuestro programa de mentoría interna: cada practicante con un mentor durante su primer semestre. Empezamos con 5 parejas.",
        ig="""🤝 Nadie aprende solo.
Cada practicante tiene un mentor durante su primer semestre en CorAll.""",
        tt=[("Dos personas frente a una laptop, sin rostros", "En CorAll nadie aprende solo."),
            ("Agenda con reuniones semanales", "Cada practicante tiene un mentor del equipo."),
            ("Equipo trabajando", "Empezamos con 5 parejas.")],
        tit="Nadie aprende solo", bul=[("Un mentor por practicante", "Durante el semestre."),
                                       ("Reuniones semanales", "Avances y dudas."),
                                       ("Talento local", "Formado en casa.")],
        dato=None, cta="Conoce más",
        tags=["#CulturaCorAll", "#Mentoría", "#Practicantes", "#TalentoLocal"],
        vis="Two coffee cups, a notebook with a weekly plan and a laptop on a shared desk, warm welcoming light",
    ),
    dict(
        id="in33", area="innovacion", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="anexado", mod="-",
        det="Se entregó la hoja de ruta digital a {cliente}; el cliente autorizó compartir sin su nombre que 2 de los 5 proyectos propuestos ya fueron aprobados para el próximo año",
        fuente="Hoja de ruta digital aprobada por un cliente", valor=4,
        razon="Hito autorizado por el cliente con un resultado concreto.",
        li="""Una hoja de ruta sirve cuando se convierte en proyectos aprobados.

Entregamos a una empresa agroindustrial de la región su hoja de ruta de transformación digital, con 5 proyectos priorizados.

2 de ellos ya fueron aprobados para el próximo año.

Gracias por la confianza. Ahora toca pasar del plan a la cancha.""",
        fb="Entregamos una hoja de ruta digital a una empresa agroindustrial: 2 de los 5 proyectos propuestos ya fueron aprobados.",
        ig="""🗺️ Del plan a los proyectos.
Hoja de ruta digital entregada: 2 de 5 proyectos ya aprobados.""",
        tt=[("Documento de hoja de ruta sobre la mesa", "Entregamos una hoja de ruta digital."),
            ("Cinco tarjetas de proyectos", "Con 5 proyectos priorizados."),
            ("Dos tarjetas marcadas como aprobadas", "Y 2 ya fueron aprobados.")],
        tit="Del plan a los proyectos", bul=[("Hoja de ruta", "Transformación digital."),
                                             ("Proyectos priorizados", "Con impacto claro."),
                                             ("Dos aprobados", "Para el próximo año.")],
        dato="2 de 5 proyectos aprobados", cta="Conoce más",
        tags=["#Innovación", "#Agroindustria", "#TransformaciónDigital", "#HojaDeRuta"],
        vis="Printed roadmap with five project cards on a wooden table, two of them marked with a red check, packing house behind",
    ),
    dict(
        id="in34", area="innovacion", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó una guía: 4 pasos para digitalizar un proceso sin detener la operación (empezar pequeño, convivir con el papel, medir y escalar)",
        fuente="Cómo digitalizar sin detener la operación", valor=3,
        razon="Contenido educativo sobre metodología; sin datos de clientes.",
        li="""Digitalizar un proceso no significa apagar todo y empezar de cero.

4 pasos para hacerlo sin detener la operación:
1. Empieza pequeño: un área, un proceso.
2. Convive con el papel unas semanas, como respaldo.
3. Mide: tiempo, errores y uso real.
4. Escala solo lo que funcionó.

Así el equipo se adapta y la operación sigue. ¿Por dónde empezaría tu empresa? Conversemos.""",
        fb="4 pasos para digitalizar sin detener la operación: empieza pequeño, convive con el papel, mide y escala lo que funcionó.",
        ig="""🔄 Digitalizar sin detenerse.
Empieza pequeño, convive con el papel, mide y escala lo que funcionó.""",
        tt=[("Oficina con papeles y una laptop", "¿Digitalizar significa empezar de cero?"),
            ("Un área usando una tablet", "No: empieza pequeño y convive con el papel."),
            ("Gráfico de avance", "Mide, y escala solo lo que funcionó.")],
        tit="Digitalizar sin detenerse", bul=[("Empieza pequeño", "Un solo proceso."),
                                              ("Convive con el papel", "Como respaldo."),
                                              ("Mide y escala", "Lo que funcionó.")],
        dato=None, cta="Conversemos",
        tags=["#TransformaciónDigital", "#Innovación", "#Tips", "#Mypes"],
        vis="3D illustration of a paper form gradually turning into a tablet screen across four small steps",
    ),
    dict(
        id="in35", area="innovacion", sector="educación", tipo="interno", pilar="catalogo",
        sec="anexado", mod="-",
        det="Se preparó la ficha de talleres para empresas: IA aplicada, sensores e IoT, ventas digitales y uso de datos para decidir",
        fuente="Ficha de talleres para empresas", valor=4,
        razon="Catálogo propio de servicios de capacitación.",
        li="""Cuatro talleres para que tu equipo aproveche la tecnología.

🤖 IA aplicada: herramientas para el trabajo diario.
📡 Sensores e IoT: qué se puede medir y cómo.
🛒 Ventas digitales: redes, WhatsApp y tienda en línea.
📊 Datos para decidir: de la hoja de cálculo al tablero.

Presenciales o virtuales, adaptados a tu empresa. ¿Cuál necesita tu equipo? Escríbenos.""",
        fb="Talleres para empresas: IA aplicada, sensores e IoT, ventas digitales y datos para decidir. Presenciales o virtuales.",
        ig="""🎓 Talleres para tu equipo.
IA aplicada, sensores e IoT, ventas digitales y datos para decidir.""",
        tt=[("Sala de capacitación", "Cuatro talleres para tu equipo."),
            ("Íconos de IA y sensores", "IA aplicada y sensores e IoT."),
            ("Íconos de ventas y datos", "Ventas digitales y datos para decidir.")],
        tit="Talleres para tu equipo", bul=[("IA aplicada", "Trabajo diario."),
                                            ("Sensores e IoT", "Qué medir."),
                                            ("Ventas y datos", "Para decidir mejor.")],
        dato=None, cta="Escríbenos",
        tags=["#Capacitación", "#Innovación", "#Empresas", "#TransformaciónDigital"],
        vis="Grid of four clean line icons for AI, a sensor, a shopping cart and a chart on a white background with red shapes",
        comp="grilla",
    ),
    dict(
        id="in36", area="innovacion", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="plataforma-proyectos",
        det="Plataforma de proyectos de innovación para {cliente}: los alumnos registran sus ideas, reciben comentarios de los docentes y votan las mejores; 46 proyectos registrados en la primera convocatoria. La institución autorizó difundir sin su nombre.",
        fuente="Plataforma de proyectos de innovación estudiantil", valor=4,
        razon="Plataforma entregada con uso real y autorización de difusión sin nombre.",
        li="""Las ideas de los alumnos merecen algo más que una carpeta olvidada.

Entregamos a una institución educativa una plataforma de proyectos de innovación: los alumnos registran sus ideas, los docentes las comentan y la comunidad vota.

En la primera convocatoria se registraron 46 proyectos.

¿Tu institución quiere ordenar y dar visibilidad a sus proyectos? Conversemos.""",
        fb="Plataforma de proyectos de innovación para una institución educativa: ideas, comentarios de docentes y votación. 46 proyectos en la primera convocatoria.",
        ig="""💡 Ideas que no se pierden.
46 proyectos de alumnos registrados, comentados y votados en una sola plataforma.""",
        tt=[("Carpeta llena de papeles", "¿Dónde terminan las ideas de los alumnos?"),
            ("Plataforma con tarjetas de proyectos", "Ahora se registran, se comentan y se votan."),
            ("Contador de proyectos", "46 proyectos en la primera convocatoria.")],
        tit="Ideas que no se pierden", bul=[("Registro de ideas", "Por los alumnos."),
                                            ("Comentarios docentes", "Para mejorar."),
                                            ("Votación abierta", "La comunidad decide.")],
        dato="46 proyectos en la primera convocatoria", cta="Conversemos",
        tags=["#Innovación", "#Educación", "#Emprendimiento", "#SoftwareAMedida"],
        vis="Laptop mockup of a project ideas board with cards and vote counters, classroom background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="in37", area="innovacion", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Jornada de validación del prototipo de alerta de heladas con los socios de {cliente} en campo; el cliente autorizó fotos del campo, sin rostros y sin su nombre",
        fuente="Validación en campo de la alerta de heladas", valor=4,
        razon="Trabajo de campo autorizado; las fotos no identifican a personas.",
        li="""Un prototipo se valida donde se va a usar.

Esta semana llevamos nuestro prototipo de alerta de heladas a campo, con los socios de una cooperativa agraria de la región.

Probamos el aviso por SMS en sus propios celulares y anotamos cada comentario: horario del mensaje, palabras más claras y qué hacer al recibirlo.

Innovar es escuchar antes de escalar.""",
        fb="Validamos en campo el prototipo de alerta de heladas con los socios de una cooperativa agraria.",
        ig="""🌾 Validado en campo.
Probamos la alerta de heladas por SMS con los socios de una cooperativa.""",
        tt=[("Camino rural hacia el campo", "Llevamos nuestro prototipo al campo."),
            ("Celular simple con un SMS", "Probamos el aviso en los celulares de los socios."),
            ("Libreta con comentarios", "Y anotamos cada comentario para mejorarlo.")],
        tit="Validado en campo", bul=[("Prueba con socios", "En su propio campo."),
                                      ("Sus celulares", "Condiciones reales."),
                                      ("Cada comentario", "Para mejorar.")],
        dato=None, cta="Conoce más",
        tags=["#Innovación", "#Agroindustria", "#Cooperativas", "#Clima"],
        vis="Rural field path at morning with a notebook and a simple phone resting on a wooden fence post",
        adj="campo",
    ),
    dict(
        id="in38", area="innovacion", sector="cuero y calzado", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó un post para talleres de calzado: cómo calcular el costo real de un par con datos del propio taller (materiales, mano de obra, mermas y gastos fijos)",
        fuente="Cómo calcular el costo real de un par", valor=3,
        razon="Contenido educativo útil para el sector; no usa datos de clientes.",
        li="""¿Sabes cuánto te cuesta realmente producir un par de zapatos?

Para calcularlo con datos de tu propio taller, suma:
• Materiales: cuero, forro, suela, insumos.
• Mano de obra por par, según los pares del día.
• Mermas: el cuero que se pierde en el corte.
• Gastos fijos repartidos: alquiler, luz, mantenimiento.

Con ese número sabes qué precio te deja ganancia. ¿Te ayudamos a armar tu tabla? Escríbenos.""",
        fb="El costo real de un par incluye materiales, mano de obra, mermas y gastos fijos repartidos. Con ese número defines un precio con ganancia.",
        ig="""👞 ¿Cuánto te cuesta un par?
Materiales, mano de obra, mermas y gastos fijos. Súmalos antes de poner precio.""",
        tt=[("Zapatos terminados en un estante", "¿Cuánto te cuesta realmente un par?"),
            ("Cortes de cuero y retazos", "Suma materiales, mano de obra y mermas."),
            ("Calculadora y cuaderno", "Y reparte tus gastos fijos antes de poner precio.")],
        tit="¿Cuánto te cuesta un par?", bul=[("Materiales", "Cuero, suela e insumos."),
                                              ("Mano de obra", "Por par."),
                                              ("Mermas y gastos", "Lo que no se ve.")],
        dato=None, cta="Escríbenos",
        tags=["#Calzado", "#Mypes", "#Costos", "#Tips"],
        vis="3D illustration of a shoe on a scale balanced against stacked icons of leather, tools and a coin",
    ),
    dict(
        id="in39", area="innovacion", sector="agroindustria", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la participación de CorAll en la feria agroexportadora regional: stand 22, miércoles 9 y jueves 10 de diciembre, con demostraciones de sensores y visión artificial",
        fuente="Participación en la feria agroexportadora regional", valor=4,
        razon="Evento confirmado con fecha y ubicación del stand.",
        li="""Nos vemos en la feria agroexportadora regional.

Estaremos con demostraciones de sensores de campo y visión artificial para empaque. Ven a ver los equipos funcionando y conversemos sobre tu campaña.

📅 Miércoles 9 y jueves 10 de diciembre
📍 Stand 22

Te esperamos.""",
        fb="Estaremos en la feria agroexportadora regional, stand 22, el miércoles 9 y jueves 10 de diciembre, con demostraciones de sensores y visión artificial.",
        ig="""🌿 Nos vemos en la feria.
Stand 22, miércoles 9 y jueves 10 de diciembre. Sensores y visión artificial en vivo.""",
        tt=[("Pasillo de una feria agrícola", "¿Vas a la feria agroexportadora?"),
            ("Equipos en exhibición", "Ven a ver nuestros sensores y la visión artificial en vivo."),
            ("Número de stand en pantalla", "Stand 22, 9 y 10 de diciembre.")],
        tit="Nos vemos en la feria", bul=[("Stand 22", "Feria agroexportadora."),
                                          ("Dos días de feria", "Miércoles 9 y jueves 10 de diciembre."),
                                          ("Demos en vivo", "Sensores y visión.")],
        dato="Stand 22, 9 y 10 de diciembre", cta="Agenda la fecha",
        tags=["#Agroexportación", "#Feria", "#Agroindustria", "#Innovación"],
        vis="Trade fair booth with red and black panels, a soil sensor and a camera on display counters, no people",
    ),
    dict(
        id="in40", area="innovacion", sector="educación", tipo="interno", pilar="hito",
        sec="anexado", mod="-",
        det="Se registró en el ERP el proyecto número 20 entregado a clientes de la región desde la fundación de CorAll",
        fuente="Veinte proyectos entregados en la región", valor=4,
        razon="Hito propio sin datos de clientes.",
        li="""20 proyectos entregados a empresas de la región.

Software, hardware, inteligencia artificial y acompañamiento en innovación: cada proyecto empezó con una conversación sobre un problema real.

Llegar a 20 es una forma de decir gracias a quienes confiaron en un equipo de Trujillo para resolverlo.

Vamos por los siguientes.""",
        fb="¡Llegamos a 20 proyectos entregados a empresas de la región! Gracias por confiar en tecnología hecha en Trujillo.",
        ig="""🎉 20 proyectos entregados.
Software, hardware, IA e innovación para empresas de la región.""",
        tt=[("Collage de equipos y pantallas", "Llegamos a 20 proyectos entregados."),
            ("Mapa de la región", "Para empresas de la región."),
            ("Equipo celebrando, sin rostros", "Gracias por confiar en un equipo de Trujillo.")],
        tit="20 proyectos en la región", bul=[("Software y hardware", "Hechos a medida."),
                                              ("IA e innovación", "Con impacto real."),
                                              ("Empresas de la región", "Gracias por confiar.")],
        dato="20 proyectos entregados", cta="Conoce más",
        tags=["#HechoEnTrujillo", "#Innovación", "#TransformaciónDigital", "#Gracias"],
        vis="Stylized map of northern Peru with twenty small glowing points connected by subtle red lines",
    ),
]
