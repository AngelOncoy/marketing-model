"""Publishable AI tasks with their reference proposal content."""

CARDS = [
    dict(
        id="ia01", area="ia", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="vision-conteo-fruta",
        det="Se entregó el modelo de conteo de fruta por cámara para la línea de empaque de {cliente}: cuenta paltas en la faja a 25 cuadros por segundo; en la validación con 3 lotes el error fue de 2 %.",
        fuente="Conteo de fruta por visión artificial", valor=5,
        razon="Modelo entregado con validación medible; se describe sin identificar al cliente.",
        li="""Contar fruta a mano en una faja que no se detiene es casi imposible. Una cámara sí puede.

Entregamos un modelo de visión artificial que cuenta paltas en la faja de empaque a 25 cuadros por segundo. En la validación con 3 lotes, el error fue de 2 %.

Así la planta sabe cuánto entra a cada línea sin detener la producción ni sumar personal.

Diseñamos el modelo y lo integramos con la cámara y la plataforma. ¿Qué te gustaría contar en tu línea? Conversemos.""",
        fb="Visión artificial en empaque: contamos paltas en la faja a 25 cuadros por segundo, con 2 % de error en la validación. ¿Qué necesitas contar?",
        ig="""🥑 Cada palta, contada.
Visión artificial en la faja de empaque: 25 cuadros por segundo y 2 % de error en la validación.""",
        tt=[("Faja con paltas en movimiento", "¿Cómo cuentas fruta en una faja que no se detiene?"),
            ("Cajas de detección sobre cada palta", "Con visión artificial, a 25 cuadros por segundo."),
            ("Contador en pantalla", "En la validación, el error fue de solo 2 %.")],
        tit="Cada palta, contada", bul=[("Cámara en la faja", "Sin detener la línea."),
                                        ("25 cuadros por segundo", "Conteo continuo."),
                                        ("Error de 2 %", "Validado con 3 lotes.")],
        dato="2 % de error en la validación", cta="Conversemos",
        tags=["#VisiónArtificial", "#Agroindustria", "#InteligenciaArtificial", "#Palta"],
        vis="Conveyor belt with avocados seen from above with clean bounding box overlays, industrial lighting",
    ),
    dict(
        id="ia02", area="ia", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="asistente-erp",
        det="Despliegue del asistente de búsqueda en el ERP: el usuario pregunta en lenguaje natural ('¿qué tickets siguen abiertos de esta semana?') y recibe la lista con enlaces. 9 de cada 10 consultas de prueba devolvieron el resultado correcto.",
        fuente="Asistente de búsqueda en lenguaje natural", valor=4,
        razon="Funcionalidad terminada con resultado de prueba; muestra IA aplicada al producto propio.",
        li="""¿Y si pudieras preguntarle a tu sistema como le preguntas a un compañero?

Desplegamos en nuestro ERP un asistente de búsqueda en lenguaje natural. Escribes "¿qué tickets siguen abiertos de esta semana?" y recibes la lista con enlaces directos.

En las pruebas, 9 de cada 10 consultas devolvieron el resultado correcto.

Menos filtros, menos clics y más tiempo para lo importante. ¿Te gustaría algo así en tu sistema? Conversemos.""",
        fb="Nuestro ERP ahora entiende preguntas en lenguaje natural: escribes lo que buscas y recibes la lista con enlaces. 9 de cada 10 consultas de prueba fueron correctas.",
        ig="""💬 Pregúntale a tu sistema.
Nuestro ERP entiende lenguaje natural: escribes lo que buscas y te responde con la lista y los enlaces.""",
        tt=[("Pantalla llena de filtros", "¿Pierdes tiempo buscando entre filtros?"),
            ("Alguien escribiendo una pregunta", "Ahora solo pregúntale al sistema."),
            ("Respuesta con lista y enlaces", "Y te responde con la lista y los enlaces.")],
        tit="Pregúntale a tu sistema", bul=[("Lenguaje natural", "Escribe como hablas."),
                                            ("Enlaces directos", "Llega al dato en un clic."),
                                            ("Menos filtros", "Más tiempo libre.")],
        dato="9 de cada 10 consultas correctas", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#ERP", "#Productividad", "#IA"],
        vis="Laptop mockup with a chat-style search bar and a result list, soft red highlight",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="ia03", area="ia", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="vision-calzado",
        det="Se cerró el piloto de inspección visual de costuras en la línea de {cliente}: el modelo marca costuras irregulares para revisión; en 600 piezas detectó 47 de las 52 fallas marcadas por el supervisor.",
        fuente="Inspección visual de costuras en calzado", valor=5,
        razon="Piloto terminado con resultado verificable; se cuenta sin identificar a la fábrica.",
        li="""Un ojo extra en la línea de costura, que no se cansa al final del turno.

Cerramos el piloto de inspección visual de costuras en una fábrica de calzado. El modelo marca las costuras irregulares para que el supervisor las revise.

En 600 piezas, detectó 47 de las 52 fallas que marcó el supervisor.

No reemplaza al supervisor: le ayuda a mirar donde más importa. ¿Te interesa un piloto en tu línea? Conversemos.""",
        fb="Piloto de inspección de costuras con IA: en 600 piezas detectó 47 de las 52 fallas marcadas por el supervisor. Un apoyo para el control de calidad.",
        ig="""🧵 Un ojo extra en la línea.
Inspección de costuras con IA: 47 de 52 fallas detectadas en 600 piezas del piloto.""",
        tt=[("Primer plano de una costura de zapato", "Al final del turno, cualquier ojo se cansa."),
            ("Cámara sobre la mesa de costura", "Este modelo marca las costuras irregulares."),
            ("Supervisor revisando la marca (sin rostro)", "En 600 piezas detectó 47 de 52 fallas. El supervisor decide.")],
        tit="Un ojo extra en la línea", bul=[("Marca costuras irregulares", "Para revisión."),
                                             ("No se cansa", "Todo el turno."),
                                             ("El supervisor decide", "La IA apoya.")],
        dato="47 de 52 fallas detectadas en 600 piezas", cta="Conversemos",
        tags=["#VisiónArtificial", "#Calzado", "#ControlDeCalidad", "#InteligenciaArtificial"],
        vis="Close-up of a shoe upper under a camera with a soft highlight on the stitching line",
    ),
    dict(
        id="ia04", area="ia", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="ocr-guias",
        det="Entrega del lector automático de guías de remisión para {cliente}: se fotografía la guía y el sistema extrae RUC, fecha y productos; reduce la digitación manual. En 400 guías de prueba extrajo bien el 94 % de los campos.",
        fuente="Lectura automática de guías de remisión", valor=4,
        razon="Producto entregado con resultado de prueba; sin datos del cliente.",
        li="""Digitar guías de remisión a mano es lento y se presta a errores.

Entregamos un lector automático de guías: tomas una foto y el sistema extrae RUC, fecha y productos para registrarlos.

En 400 guías de prueba, extrajo correctamente el 94 % de los campos. El resto queda marcado para revisión humana.

Menos digitación, más tiempo para lo que importa. ¿Cuántos documentos digita tu equipo al día? Conversemos.""",
        fb="Lector automático de guías de remisión: foto, extracción de RUC, fecha y productos, y 94 % de campos correctos en 400 guías de prueba.",
        ig="""📄 Una foto en lugar de digitar.
Nuestro lector de guías extrae RUC, fecha y productos. 94 % de campos correctos en 400 guías de prueba.""",
        tt=[("Pila de guías de remisión", "¿Tu equipo digita guías todo el día?"),
            ("Celular fotografiando una guía", "Ahora basta una foto."),
            ("Campos llenándose solos", "El sistema extrae RUC, fecha y productos. 94 % correcto en pruebas.")],
        tit="Una foto en vez de digitar", bul=[("Foto de la guía", "Desde el celular."),
                                               ("Campos extraídos", "RUC, fecha y productos."),
                                               ("Revisión humana", "Para los casos dudosos.")],
        dato="94 % de campos correctos en 400 guías", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#Logística", "#AutomatizaciónDeProcesos", "#OCR"],
        vis="Smartphone photographing a printed delivery document with fields being highlighted",
    ),
    dict(
        id="ia05", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Charla interna: cómo evaluar un modelo de IA antes de ponerlo en producción (conjunto de prueba separado, comparar contra una línea base y revisar casos de error); se decidió publicarlo como guía",
        fuente="Cómo evaluar un modelo de IA", valor=4,
        razon="Contenido educativo general sobre IA responsable; no contiene datos internos.",
        li="""Que un modelo de IA "funcione en la demo" no significa que funcione en tu operación.

Antes de llevar un modelo a producción, aplicamos tres pasos:

1. Probarlo con datos que nunca vio durante el entrenamiento.
2. Compararlo contra una línea base: el proceso actual o un método simple.
3. Revisar uno por uno los casos en los que falla.

Si no supera a la línea base, todavía no está listo. ¿Cómo evalúas tú la IA que usas?""",
        fb="3 pasos antes de llevar un modelo de IA a producción: probarlo con datos nuevos, compararlo con una línea base y revisar sus errores.",
        ig="""🧪 ¿Tu IA está lista para producción?
Pruébala con datos nuevos, compárala con una línea base y revisa sus errores uno por uno.""",
        tt=[("Demo exitosa en pantalla", "Que funcione en la demo no basta."),
            ("Gráfico comparando dos barras", "Pruébalo con datos nuevos y compáralo con una línea base."),
            ("Lista de errores revisándose", "Y revisa cada caso en que falla.")],
        tit="¿Tu IA está lista?", bul=[("Datos nuevos", "Que nunca vio."),
                                       ("Línea base", "Para comparar."),
                                       ("Revisa los errores", "Uno por uno.")],
        dato=None, cta="Cuéntanos",
        tags=["#InteligenciaArtificial", "#IAResponsable", "#CienciaDeDatos", "#BuenasPrácticas"],
        vis="3D illustration of a magnifying glass over a bar chart comparing two models",
    ),
    dict(
        id="ia06", area="ia", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="prediccion-riego",
        det="Se entregó el modelo de recomendación de riego para {cliente}: combina humedad de suelo y pronóstico de clima para sugerir el riego del día siguiente por sector. En el piloto de 4 semanas el consumo de agua bajó 15 % sin afectar el rendimiento.",
        fuente="Recomendación de riego con IA", valor=5,
        razon="Resultado medible de piloto terminado; se presenta sin identificar el fundo.",
        li="""Regar lo justo es ahorrar agua sin arriesgar la cosecha.

Entregamos un modelo que combina la humedad del suelo con el pronóstico del clima para sugerir el riego del día siguiente en cada sector del fundo.

En un piloto de 4 semanas, el consumo de agua bajó 15 % sin afectar el rendimiento.

Sensores, modelo y plataforma trabajando juntos. ¿Quieres probarlo en tu campo? Conversemos.""",
        fb="Riego recomendado por IA: humedad de suelo más pronóstico de clima. En 4 semanas de piloto, 15 % menos agua sin afectar el rendimiento.",
        ig="""💧 Regar lo justo.
Humedad de suelo + pronóstico de clima = riego sugerido por sector. Piloto: 15 % menos agua sin afectar el rendimiento.""",
        tt=[("Aspersores regando un campo", "¿Riegas más de lo que tu campo necesita?"),
            ("Mapa por sectores con recomendaciones", "Este modelo sugiere el riego por sector."),
            ("Indicador de agua bajando", "En 4 semanas de piloto, 15 % menos agua.")],
        tit="Regar lo justo", bul=[("Humedad de suelo", "Dato de campo."),
                                   ("Pronóstico de clima", "Lo que viene."),
                                   ("Riego por sector", "Sugerido cada día.")],
        dato="15 % menos agua en 4 semanas", cta="Conversemos",
        tags=["#AgriculturaDePrecisión", "#InteligenciaArtificial", "#GestiónDelAgua", "#Agroindustria"],
        vis="Irrigated crop field divided in sectors with subtle data overlay icons, golden hour light",
    ),
    dict(
        id="ia07", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó contenido sobre cuándo NO usar inteligencia artificial: cuando una regla simple resuelve el problema, cuando no hay datos suficientes o cuando el error no es aceptable sin revisión humana",
        fuente="Cuándo no usar inteligencia artificial", valor=4,
        razon="Contenido educativo honesto y general; refuerza la confianza en la marca.",
        li="""No todo problema necesita inteligencia artificial. Y decirlo también es parte de nuestro trabajo.

Tres casos en los que solemos recomendar otra solución:

1. Cuando una regla simple ya resuelve el problema.
2. Cuando no hay datos suficientes para entrenar ni para evaluar.
3. Cuando un error no es aceptable y no hay una persona que revise.

La tecnología correcta es la que resuelve tu problema, no la más llamativa. ¿Tienes un caso en mente? Conversemos.""",
        fb="¿Necesitas IA? A veces no: si una regla simple lo resuelve, si no hay datos o si el error no es aceptable sin revisión humana. Te ayudamos a decidir.",
        ig="""🤖 ¿De verdad necesitas IA?
No si una regla simple lo resuelve, si no hay datos o si el error no se puede revisar.""",
        tt=[("Pregunta en pantalla: ¿necesitas IA?", "¿De verdad necesitas inteligencia artificial?"),
            ("Una regla simple en una pizarra", "Si una regla simple lo resuelve, no."),
            ("Persona revisando resultados (sin rostro)", "Y si el error no se puede revisar, tampoco.")],
        tit="¿De verdad necesitas IA?", bul=[("Regla simple", "A veces basta."),
                                             ("Sin datos", "No hay modelo."),
                                             ("Sin revisión humana", "Riesgo alto.")],
        dato=None, cta="Conversemos",
        tags=["#InteligenciaArtificial", "#IAResponsable", "#TransformaciónDigital", "#BuenasPrácticas"],
        vis="3D illustration of a robot head icon next to a simple checklist, balanced minimal composition",
    ),
    dict(
        id="ia08", area="ia", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="mantenimiento-predictivo",
        det="Entrega del modelo de alerta temprana por vibración para 5 bombas de {cliente}: analiza la vibración cada hora y avisa cuando el patrón se aleja de lo normal. En el periodo de prueba anticipó 2 paradas con varios días de margen.",
        fuente="Alerta temprana por vibración en bombas", valor=5,
        razon="Modelo entregado con resultado real en prueba; sin identificar al cliente.",
        li="""Una bomba casi siempre avisa antes de fallar. El problema es escucharla a tiempo.

Entregamos un modelo de alerta temprana que analiza la vibración de 5 bombas cada hora y avisa cuando el patrón se aleja de lo normal.

En el periodo de prueba, anticipó 2 paradas con varios días de margen para programar el mantenimiento.

Sensores, modelo y plataforma diseñados por nuestro equipo. ¿Qué equipo crítico te gustaría vigilar? Conversemos.""",
        fb="Mantenimiento predictivo: analizamos la vibración de 5 bombas cada hora y el modelo anticipó 2 paradas con días de margen.",
        ig="""⚙️ Escuchar a las máquinas a tiempo.
Analizamos la vibración de 5 bombas cada hora. En prueba, el modelo anticipó 2 paradas con días de margen.""",
        tt=[("Bomba industrial funcionando", "Una bomba casi siempre avisa antes de fallar."),
            ("Gráfico de vibración con una anomalía", "Este modelo analiza su vibración cada hora."),
            ("Alerta de mantenimiento programado", "En prueba, anticipó 2 paradas con días de margen.")],
        tit="Antes de que la bomba falle", bul=[("Vibración cada hora", "Monitoreo continuo."),
                                                ("Patrón anormal", "Alerta temprana."),
                                                ("Mantenimiento programado", "Sin paradas sorpresa.")],
        dato="2 paradas anticipadas en el periodo de prueba", cta="Conversemos",
        tags=["#MantenimientoPredictivo", "#Minería", "#InteligenciaArtificial", "#IoT"],
        vis="Industrial pump with a small vibration sensor and an abstract waveform glowing beside it",
    ),
    dict(
        id="ia09", area="ia", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la charla abierta 'IA para tu negocio sin humo': viernes 4 de diciembre, 18:30, transmisión en vivo por las redes de CorAll; dirigida a mypes y estudiantes",
        fuente="Charla abierta sobre IA para negocios", valor=4,
        razon="Evento propio confirmado con fecha y canal; ideal para convocatoria.",
        li="""Inteligencia artificial para tu negocio, sin humo.

Te invitamos a nuestra charla abierta para mypes y estudiantes, donde hablaremos con ejemplos reales de qué puede hacer la IA hoy, qué no y cómo empezar con poco.

📅 Viernes 4 de diciembre
🕡 18:30
📍 En vivo por nuestras redes

Trae tus preguntas. Te esperamos.""",
        fb="Charla abierta 'IA para tu negocio sin humo': viernes 4 de diciembre, 18:30, en vivo por nuestras redes. Para mypes y estudiantes.",
        ig="""🎙️ IA para tu negocio, sin humo.
Charla abierta, viernes 4 de diciembre, 18:30, en vivo por nuestras redes. Trae tus preguntas.""",
        tt=[("Palabras de moda sobre IA tachándose", "¿Cansado de promesas sobre inteligencia artificial?"),
            ("Ejemplos reales en pantalla", "Hablemos con ejemplos reales de lo que sí puede hacer."),
            ("Fecha en pantalla", "Viernes 4 de diciembre, 18:30, en vivo.")],
        tit="IA para tu negocio, sin humo", bul=[("Viernes 4 de diciembre", "A las 18:30."),
                                                 ("En vivo", "Por nuestras redes."),
                                                 ("Ejemplos reales", "Para mypes y estudiantes.")],
        dato="Viernes 4 de diciembre, 18:30", cta="Agenda la fecha",
        tags=["#InteligenciaArtificial", "#Mypes", "#CharlaGratuita", "#Emprendimiento"],
        vis="Microphone and laptop on a stage with soft red spotlight and abstract neural network lines",
    ),
    dict(
        id="ia10", area="ia", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="clasificador-tickets",
        det="Se desplegó el clasificador automático de tickets en el ERP: sugiere categoría y prioridad al crear el ticket; en 500 tickets históricos acertó la categoría en 88 % de los casos y el agente puede corregirla.",
        fuente="Clasificación automática de tickets", valor=4,
        razon="Funcionalidad terminada con métrica de prueba y supervisión humana.",
        li="""Cada ticket nuevo llega ya clasificado. Y si el sistema se equivoca, una persona lo corrige.

Desplegamos en nuestro ERP un clasificador que sugiere la categoría y la prioridad de cada ticket al momento de crearlo.

Probado con 500 tickets históricos, acertó la categoría en el 88 % de los casos. El agente de soporte siempre puede corregir la sugerencia.

Menos tiempo ordenando, más tiempo resolviendo. ¿Te interesa para tu mesa de ayuda? Conversemos.""",
        fb="Clasificación automática de tickets en nuestro ERP: 88 % de aciertos en 500 tickets históricos, con corrección humana siempre disponible.",
        ig="""🏷️ Tickets que llegan ordenados.
Categoría y prioridad sugeridas al crear el ticket. 88 % de aciertos en 500 tickets históricos.""",
        tt=[("Bandeja de tickets sin orden", "¿Pierdes tiempo clasificando tickets?"),
            ("Etiquetas apareciendo en cada ticket", "Ahora el sistema sugiere categoría y prioridad."),
            ("Agente corrigiendo una etiqueta (sin rostro)", "Y si se equivoca, el agente la corrige.")],
        tit="Tickets que llegan ordenados", bul=[("Categoría sugerida", "Al crear el ticket."),
                                                 ("Prioridad sugerida", "Lo urgente primero."),
                                                 ("Corrección humana", "Siempre disponible.")],
        dato="88 % de aciertos en 500 tickets", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#AtenciónAlCliente", "#ERP", "#Automatización"],
        vis="Laptop mockup of a helpdesk inbox where tickets show colored category tags",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="ia11", area="ia", sector="agroindustria", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Visita al fundo para recolectar 1200 fotos de hojas de arándano con y sin plaga, con autorización del cliente para publicar sin nombre; las fotos servirán para entrenar el modelo de detección",
        fuente="Recolección de imágenes en campo", valor=3,
        razon="Trabajo de campo terminado con autorización; muestra el proceso real detrás de la IA.",
        li="""Detrás de cada modelo de IA hay mucho trabajo de campo.

Esta semana visitamos un fundo de arándanos para tomar 1200 fotos de hojas, con y sin plaga. Con ellas entrenaremos un modelo que ayude a detectar la plaga a tiempo.

Un buen modelo empieza con buenos datos, tomados en las condiciones reales del cultivo: con su luz, su polvo y sus hojas.

¿Tu cultivo tiene un problema que se ve a simple vista? Conversemos.""",
        fb="Detrás de la IA hay trabajo de campo: tomamos 1200 fotos de hojas de arándano para entrenar un modelo de detección de plagas.",
        ig="""📸 La IA empieza en el campo.
1200 fotos de hojas de arándano, con y sin plaga, tomadas en condiciones reales del cultivo.""",
        tt=[("Hileras de arándanos", "¿Cómo se entrena una IA para detectar plagas?"),
            ("Celular fotografiando hojas", "Empieza aquí: tomamos 1200 fotos de hojas en el campo."),
            ("Grilla de fotos de hojas", "Con y sin plaga, en condiciones reales.")],
        tit="La IA empieza en el campo", bul=[("1200 fotos", "De hojas de arándano."),
                                              ("Condiciones reales", "Luz y polvo del cultivo."),
                                              ("Buenos datos", "Base de un buen modelo.")],
        dato="1200 fotos de hojas", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#Arándanos", "#Agroindustria", "#DatosDeCampo"],
        vis="Close-up of blueberry leaves in a field with a smartphone camera frame overlay",
        adj="campo",
    ),
    dict(
        id="ia12", area="ia", sector="educación", tipo="interno", pilar="hito",
        sec="matriz", mod="propuestas-ia",
        det="Se completó la validación automática de propuestas de marketing: cada cifra del texto se compara con el reporte de origen y se bloquean frases exageradas antes de que la propuesta llegue a revisión.",
        fuente="Validación automática de propuestas generadas", valor=4,
        razon="Hito propio de IA responsable; se describe sin detalles internos.",
        li="""Si la IA escribe un número, ese número tiene que existir.

Completamos la validación automática de nuestras propuestas de marketing generadas con IA: cada cifra del texto se compara con el reporte de origen y las frases exageradas se bloquean antes de que la propuesta llegue a revisión.

Usar IA no significa publicar sin control. Significa poner reglas claras y una persona que apruebe.

¿Cómo controlas lo que genera la IA en tu empresa?""",
        fb="Nuestras propuestas generadas con IA pasan por validación: cada cifra se compara con el reporte de origen y se bloquean las exageraciones.",
        ig="""✅ Si la IA escribe un número, debe existir.
Cada cifra se compara con su fuente y las exageraciones se bloquean antes de la revisión humana.""",
        tt=[("Texto generado con un número resaltado", "Si la IA escribe un número, ¿de dónde sale?"),
            ("El número comparándose con su fuente", "Nuestro sistema compara cada cifra con el reporte de origen."),
            ("Frase exagerada tachada", "Y bloquea las exageraciones antes de la revisión.")],
        tit="Cifras con respaldo", bul=[("Cifras verificadas", "Contra su fuente."),
                                        ("Sin exageraciones", "Frases bloqueadas."),
                                        ("Revisión humana", "Antes de publicar.")],
        dato=None, cta="Cuéntanos",
        tags=["#IAResponsable", "#InteligenciaArtificial", "#Marketing", "#Transparencia"],
        vis="3D illustration of a document with a highlighted number connected by a line to a source document",
    ),
    dict(
        id="ia13", area="ia", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="prediccion-demanda",
        det="Entrega del modelo de predicción de demanda semanal para el almacén de {cliente}: pronostica 60 productos con 4 semanas de anticipación; en la validación del último trimestre el error promedio fue 11 %.",
        fuente="Predicción de demanda semanal", valor=4,
        razon="Modelo entregado con validación; sin identificar al cliente.",
        li="""Comprar de más inmoviliza dinero. Comprar de menos deja estantes vacíos.

Entregamos un modelo que pronostica la demanda semanal de 60 productos con 4 semanas de anticipación para el almacén de un distribuidor.

En la validación con el último trimestre, el error promedio fue de 11 %.

Con esa información, el área de compras planifica mejor y reacciona antes. ¿Quieres pronosticar tu demanda? Conversemos.""",
        fb="Predicción de demanda semanal: 60 productos con 4 semanas de anticipación y 11 % de error promedio en la validación.",
        ig="""📦 Compra lo que vas a vender.
Pronóstico semanal de 60 productos con 4 semanas de anticipación. Error promedio de 11 % en la validación.""",
        tt=[("Estante vacío y otro lleno", "Comprar de más o de menos cuesta dinero."),
            ("Gráfico de pronóstico", "Este modelo pronostica la demanda con 4 semanas de anticipación."),
            ("Área de compras planificando (sin rostros)", "60 productos, 11 % de error promedio en la validación.")],
        tit="Compra lo que vas a vender", bul=[("4 semanas antes", "Pronóstico semanal."),
                                               ("60 productos", "Del almacén."),
                                               ("Mejor planificación", "Para compras.")],
        dato="11 % de error promedio", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#Logística", "#PredicciónDeDemanda", "#Inventarios"],
        vis="Warehouse shelves with a translucent forecast line chart overlay, clean light",
    ),
    dict(
        id="ia14", area="ia", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Club de lectura técnica del equipo de IA: se cumplieron 10 sesiones en el año revisando papers y aplicándolos a proyectos reales",
        fuente="Club de lectura técnica", valor=3,
        razon="Contenido de cultura de aprendizaje sin datos sensibles.",
        li="""10 sesiones, muchos papers y una regla: si lo leemos, intentamos aplicarlo.

Este año nuestro equipo de IA cumplió 10 sesiones de su club de lectura técnica. Cada sesión revisamos un artículo y discutimos cómo podría ayudar en un proyecto real.

Aprender juntos nos mantiene al día y nos obliga a explicar con claridad lo que entendemos.

¿Tu equipo tiene un espacio para aprender así?""",
        fb="Nuestro club de lectura técnica cumplió 10 sesiones este año: leemos artículos de IA y buscamos cómo aplicarlos en proyectos reales.",
        ig="""📖 Aprender juntos.
10 sesiones de nuestro club de lectura técnica: si lo leemos, intentamos aplicarlo.""",
        tt=[("Artículos impresos sobre una mesa", "Este año leímos muchos artículos de IA."),
            ("Equipo conversando (sin rostros)", "En 10 sesiones del club de lectura."),
            ("Pizarra con un diagrama", "Y una regla: si lo leemos, intentamos aplicarlo.")],
        tit="Aprender juntos", bul=[("10 sesiones", "En el año."),
                                    ("Artículos reales", "Discutidos en equipo."),
                                    ("Aplicación", "En proyectos reales.")],
        dato="10 sesiones en el año", cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#AprendizajeContinuo", "#InteligenciaArtificial", "#EquipoCorAll"],
        vis="Table with printed research papers, highlighters and coffee, whiteboard diagrams behind",
    ),
    dict(
        id="ia15", area="ia", sector="minería", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Guía interna sobre datos para mantenimiento predictivo: qué sensores instalar, cuánto historial se necesita y por qué registrar cada falla con fecha; se acordó compartirla como contenido",
        fuente="Datos necesarios para mantenimiento predictivo", valor=3,
        razon="Contenido educativo general para el sector industrial.",
        li="""¿Quieres mantenimiento predictivo? Empieza registrando tus fallas hoy.

Un modelo predictivo aprende del pasado. Por eso, antes de hablar de IA, revisamos tres cosas con cada cliente:

1. Qué variables se miden: vibración, temperatura, corriente.
2. Cuánto historial existe y con qué frecuencia se registra.
3. Si cada falla quedó registrada con fecha y causa.

Sin ese historial, ningún modelo puede anticipar nada. ¿Tu operación ya registra sus fallas? Conversemos.""",
        fb="Para tener mantenimiento predictivo necesitas datos: variables medidas, historial suficiente y fallas registradas con fecha y causa. Empieza hoy.",
        ig="""📝 La IA aprende de tu historial.
Mide vibración, temperatura o corriente, guarda el historial y registra cada falla con fecha y causa.""",
        tt=[("Máquina industrial con sensores", "¿Quieres que la IA anticipe fallas?"),
            ("Cuaderno de mantenimiento", "Primero necesitas historial: qué mides y cada cuánto."),
            ("Registro digital de una falla", "Y cada falla registrada con fecha y causa.")],
        tit="Registra tus fallas hoy", bul=[("Mide variables", "Vibración y temperatura."),
                                            ("Guarda historial", "Con frecuencia fija."),
                                            ("Registra fallas", "Con fecha y causa.")],
        dato=None, cta="Conversemos",
        tags=["#MantenimientoPredictivo", "#InteligenciaArtificial", "#Industria40", "#BuenasPrácticas"],
        vis="3D illustration of a machine with a clipboard and a timeline of maintenance events",
    ),
    dict(
        id="ia16", area="ia", sector="agroindustria", tipo="interno", pilar="hito",
        sec="matriz", mod="vision-calibre",
        det="Se terminó la primera versión del clasificador de calibre de mango por imagen: separa 4 calibres; en 300 frutos de prueba coincidió con la balanza en 91 % de los casos.",
        fuente="Clasificador de calibre de mango por imagen", valor=4,
        razon="Hito propio con validación medible.",
        li="""Clasificar mango por calibre, solo con una foto.

Terminamos la primera versión de nuestro clasificador de calibre por imagen: separa la fruta en 4 calibres sin necesidad de pesarla una por una.

En una prueba con 300 frutos, coincidió con la balanza en el 91 % de los casos.

Es el primer paso de una línea de clasificación más rápida. ¿Te interesa probarlo en tu empacadora? Conversemos.""",
        fb="Primera versión de nuestro clasificador de calibre de mango por imagen: 4 calibres y 91 % de coincidencia con la balanza en 300 frutos.",
        ig="""🥭 Calibre con una foto.
Nuestro clasificador separa mango en 4 calibres: 91 % de coincidencia con la balanza en 300 frutos.""",
        tt=[("Mangos sobre una mesa", "¿Y si pudieras clasificar mango solo con una foto?"),
            ("Cámara clasificando por tamaño", "Nuestro modelo separa 4 calibres."),
            ("Comparación con la balanza", "En 300 frutos, 91 % de coincidencia.")],
        tit="Calibre con una foto", bul=[("4 calibres", "Separados por imagen."),
                                         ("Sin pesar cada fruta", "Más rapidez."),
                                         ("91 % de coincidencia", "Contra la balanza.")],
        dato="91 % de coincidencia en 300 frutos", cta="Conversemos",
        tags=["#VisiónArtificial", "#Mango", "#Agroindustria", "#InteligenciaArtificial"],
        vis="Mangoes of different sizes in a row on a white surface with subtle measurement overlays",
    ),
    dict(
        id="ia17", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Contenido sobre privacidad al usar IA: no pegar datos de clientes en herramientas externas, anonimizar antes de procesar y preferir modelos que se ejecuten en infraestructura propia cuando hay datos sensibles",
        fuente="Privacidad al usar herramientas de IA", valor=4,
        razon="Contenido educativo alineado con la Ley 29733; sin datos internos.",
        li="""Antes de pegar información en una herramienta de IA, piensa a dónde va.

Tres prácticas que aplicamos y recomendamos:

1. No pegues datos de clientes o de personal en herramientas externas.
2. Anonimiza antes de procesar: nombres, documentos, teléfonos y correos fuera.
3. Si los datos son sensibles, prefiere modelos que se ejecuten en tu propia infraestructura.

La IA ahorra tiempo, pero los datos de tus clientes son tu responsabilidad. ¿Cómo lo manejas en tu empresa?""",
        fb="Antes de usar IA con datos de clientes: no los pegues en herramientas externas, anonimiza y prefiere modelos propios para datos sensibles.",
        ig="""🔒 ¿A dónde van tus datos?
No pegues datos de clientes en herramientas externas, anonimiza y usa modelos propios si son sensibles.""",
        tt=[("Mano a punto de pegar texto en un chat", "Antes de pegar datos en una IA, piensa a dónde van."),
            ("Nombres reemplazándose por etiquetas", "Anonimiza: nombres, documentos y teléfonos fuera."),
            ("Servidor propio con candado", "Y si son sensibles, usa modelos propios.")],
        tit="¿A dónde van tus datos?", bul=[("No pegues datos", "En herramientas externas."),
                                            ("Anonimiza primero", "Nombres y documentos fuera."),
                                            ("Modelos propios", "Para datos sensibles.")],
        dato=None, cta="Cuéntanos",
        tags=["#ProtecciónDeDatos", "#IAResponsable", "#InteligenciaArtificial", "#Privacidad"],
        vis="3D illustration of a document passing through a filter that replaces names with blank tags",
    ),
    dict(
        id="ia18", area="ia", sector="cuero y calzado", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmada la demostración de visión artificial para el sector calzado en la sede de CorAll: miércoles 2 de diciembre, 10:00 a 12:00, cupo de 25 personas, inscripción previa",
        fuente="Demostración de visión artificial para calzado", valor=4,
        razon="Evento confirmado con fecha, lugar y cupo.",
        li="""¿Cómo puede ayudar la visión artificial en tu fábrica de calzado? Ven a verlo funcionando.

Organizamos una demostración práctica para el sector calzado, con ejemplos de inspección de costuras y conteo de pares.

📅 Miércoles 2 de diciembre
🕙 10:00 a 12:00
📍 Sede de CorAll, Trujillo
👥 Cupo: 25 personas

Inscripción previa en el enlace.""",
        fb="Demostración de visión artificial para calzado: miércoles 2 de diciembre, 10:00 a 12:00, en nuestra sede de Trujillo. Solo 25 cupos.",
        ig="""👞 Visión artificial para calzado, en vivo.
Miércoles 2 de diciembre, 10:00 a 12:00, sede de CorAll en Trujillo. 25 cupos con inscripción previa.""",
        tt=[("Pares de calzado en una línea", "¿Qué puede hacer la visión artificial en tu fábrica?"),
            ("Cámara marcando costuras", "Ven a ver inspección de costuras y conteo de pares."),
            ("Fecha en pantalla", "Miércoles 2 de diciembre, 10:00. Solo 25 cupos.")],
        tit="Visión artificial para calzado", bul=[("Miércoles 2 de diciembre", "De 10:00 a 12:00."),
                                                   ("Sede de CorAll", "Trujillo."),
                                                   ("25 cupos", "Inscripción previa.")],
        dato="Miércoles 2 de diciembre, 10:00", cta="Inscríbete",
        tags=["#Calzado", "#VisiónArtificial", "#Trujillo", "#Industria40"],
        vis="Demo table with a camera on a stand pointing at a shoe, red and black geometric shapes",
    ),
    dict(
        id="ia19", area="ia", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="matriz", mod="rutas-optimizacion",
        det="Entrega del optimizador de rutas de reparto para {cliente}: ordena las paradas del día considerando ventanas de horario; en 2 semanas de uso redujo el recorrido total 12 %.",
        fuente="Optimización de rutas de reparto", valor=4,
        razon="Solución entregada con mejora medible; sin identificar al cliente.",
        li="""Menos kilómetros, mismas entregas.

Entregamos un optimizador de rutas de reparto que ordena las paradas del día considerando el horario en que cada cliente puede recibir.

En 2 semanas de uso, el recorrido total se redujo 12 %.

Menos combustible, menos horas en ruta y conductores que llegan a tiempo. ¿Tu operación de reparto podría ahorrar kilómetros? Conversemos.""",
        fb="Optimizador de rutas de reparto: paradas ordenadas según ventanas de horario y 12 % menos de recorrido en 2 semanas de uso.",
        ig="""🗺️ Menos kilómetros, mismas entregas.
Nuestro optimizador ordena las paradas según el horario de cada cliente: 12 % menos de recorrido en 2 semanas.""",
        tt=[("Mapa con una ruta enredada", "¿Tus rutas de reparto dan demasiadas vueltas?"),
            ("La ruta reordenándose", "Este optimizador ordena las paradas según el horario de cada cliente."),
            ("Indicador de kilómetros bajando", "En 2 semanas, 12 % menos de recorrido.")],
        tit="Menos kilómetros, mismas entregas", bul=[("Paradas ordenadas", "Cada día."),
                                                      ("Ventanas de horario", "Del cliente."),
                                                      ("12 % menos recorrido", "En 2 semanas.")],
        dato="12 % menos de recorrido", cta="Conversemos",
        tags=["#Logística", "#OptimizaciónDeRutas", "#InteligenciaArtificial", "#ÚltimaMilla"],
        vis="Stylized city map with a clean optimized delivery route line in red connecting stops",
        comp="antes / después",
    ),
    dict(
        id="ia20", area="ia", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó una explicación simple de qué es un modelo de lenguaje y por qué puede inventar datos, para compartir con clientes que usan asistentes de IA",
        fuente="Por qué la IA puede inventar datos", valor=4,
        razon="Contenido educativo general y transparente sobre IA.",
        li="""¿Por qué una IA puede responder con total seguridad algo que no es cierto?

Un modelo de lenguaje no "busca" la respuesta: predice el texto más probable. Por eso, a veces, completa con datos que suenan bien pero no existen.

Cómo reducir el riesgo:
- Dale la información de origen y pídele que se limite a ella.
- Verifica cifras, nombres y fechas.
- Deja que una persona apruebe antes de publicar.

La IA es una gran asistente, no una fuente. ¿Cómo la usas tú?""",
        fb="Una IA puede inventar datos porque predice el texto más probable. Dale la fuente, verifica cifras y deja que una persona apruebe.",
        ig="""🧠 ¿Por qué la IA inventa?
Predice el texto más probable, no busca la verdad. Dale la fuente, verifica cifras y revisa antes de publicar.""",
        tt=[("Respuesta de IA con un dato resaltado", "¿Por qué una IA inventa datos?"),
            ("Palabras apareciendo una por una", "Porque predice el texto más probable."),
            ("Persona verificando con un documento (sin rostro)", "Dale la fuente y verifica antes de publicar.")],
        tit="¿Por qué la IA inventa?", bul=[("Dale la fuente", "Y que se limite a ella."),
                                            ("Verifica cifras", "Nombres y fechas."),
                                            ("Aprobación humana", "Antes de publicar.")],
        dato=None, cta="Cuéntanos",
        tags=["#InteligenciaArtificial", "#IAResponsable", "#AlfabetizaciónDigital", "#BuenasPrácticas"],
        vis="3D illustration of a speech bubble with a question mark and a magnifying glass checking it",
    ),
    dict(
        id="ia21", area="ia", sector="agroindustria", tipo="cliente", pilar="hito",
        sec="matriz", mod="vision-plagas",
        det="Primer modelo de detección de plaga en hojas de arándano entregado a {cliente}: entrenado con 1200 fotos de campo; en el conjunto de prueba identificó correctamente 86 % de las hojas afectadas.",
        fuente="Detección de plaga en hojas de arándano", valor=5,
        razon="Hito entregado con métrica de prueba; sin identificar al cliente.",
        li="""De 1200 fotos de campo a un modelo que ayuda a detectar plaga a tiempo.

Entregamos el primer modelo de detección de plaga en hojas de arándano. Lo entrenamos con 1200 fotos tomadas en el propio cultivo.

En el conjunto de prueba, identificó correctamente el 86 % de las hojas afectadas. El equipo agrícola revisa cada alerta antes de actuar.

Detectar antes significa tratar menos y a tiempo. ¿Tu cultivo enfrenta un problema parecido? Conversemos.""",
        fb="Primer modelo de detección de plaga en arándano: entrenado con 1200 fotos de campo, identificó el 86 % de las hojas afectadas en prueba.",
        ig="""🫐 Detectar la plaga a tiempo.
Modelo entrenado con 1200 fotos de campo: 86 % de hojas afectadas identificadas en prueba.""",
        tt=[("Hoja de arándano con manchas", "Detectar una plaga a tiempo lo cambia todo."),
            ("Fotos de campo pasando rápido", "Entrenamos un modelo con 1200 fotos del cultivo."),
            ("Alerta en el celular del ingeniero", "En prueba identificó el 86 % de hojas afectadas.")],
        tit="Detectar la plaga a tiempo", bul=[("1200 fotos de campo", "Datos reales."),
                                               ("86 % identificadas", "En prueba."),
                                               ("Revisión del agrónomo", "Antes de actuar.")],
        dato="86 % de hojas afectadas identificadas", cta="Conversemos",
        tags=["#InteligenciaArtificial", "#Arándanos", "#SanidadVegetal", "#Agroindustria"],
        vis="Blueberry leaf close-up with a subtle highlight circle over a small affected area",
    ),
    dict(
        id="ia22", area="ia", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="asistente-matriculas",
        det="Se entregó el asistente de preguntas frecuentes de matrícula para un instituto, con autorización para difundir sin nombre: responde requisitos, fechas y costos desde la información oficial; deriva a una persona si no sabe la respuesta. Atendió 430 consultas en su primera semana.",
        fuente="Asistente de preguntas frecuentes de matrícula", valor=4,
        razon="Producto entregado con autorización y uso medible.",
        li="""En época de matrícula, las mismas preguntas llegan cientos de veces.

Entregamos a un instituto un asistente que responde requisitos, fechas y costos usando solo la información oficial. Si no sabe la respuesta, deriva la consulta a una persona del equipo.

En su primera semana atendió 430 consultas.

El equipo de admisión dedica su tiempo a los casos que de verdad necesitan atención. ¿Tu institución recibe muchas consultas repetidas? Conversemos.""",
        fb="Asistente de matrícula para un instituto: responde con información oficial y deriva a una persona si no sabe. 430 consultas en su primera semana.",
        ig="""🎓 Matrícula sin colas de mensajes.
Un asistente que responde con información oficial y deriva a una persona si no sabe. 430 consultas en la primera semana.""",
        tt=[("Celular con muchos mensajes sin leer", "En matrícula, las mismas preguntas llegan cientos de veces."),
            ("Asistente respondiendo requisitos", "Este asistente responde con la información oficial."),
            ("Mensaje derivado a una persona", "Y si no sabe, deriva a una persona. 430 consultas en una semana.")],
        tit="Matrícula sin colas de mensajes", bul=[("Información oficial", "Requisitos, fechas y costos."),
                                                    ("Deriva a una persona", "Si no sabe."),
                                                    ("Admisión libre", "Para casos importantes.")],
        dato="430 consultas en la primera semana", cta="Conversemos",
        tags=["#Educación", "#Chatbot", "#InteligenciaArtificial", "#AtenciónAlCliente"],
        vis="Smartphone mockup showing a friendly chat assistant answering enrollment questions",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="ia23", area="ia", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Una integrante del equipo de IA presentó una ponencia sobre visión artificial aplicada al agro en un congreso universitario regional; autorizó mencionar el logro sin publicar su foto",
        fuente="Ponencia del equipo en un congreso", valor=3,
        razon="Logro del equipo con autorización; se menciona sin datos personales.",
        li="""Orgullosos de compartir lo que aprendemos.

Una integrante de nuestro equipo de inteligencia artificial presentó una ponencia sobre visión artificial aplicada al agro en un congreso universitario regional.

Llevar nuestra experiencia de campo a las aulas es parte de cómo entendemos la innovación: aprender, aplicar y compartir.

¡Felicitaciones por representar al equipo!""",
        fb="Una integrante de nuestro equipo de IA presentó una ponencia sobre visión artificial en el agro en un congreso universitario regional. ¡Felicitaciones!",
        ig="""🎤 Compartir lo que aprendemos.
Nuestro equipo de IA presentó una ponencia sobre visión artificial en el agro en un congreso universitario.""",
        tt=[("Auditorio universitario vacío", "Hoy el aula escuchó nuestra experiencia de campo."),
            ("Diapositiva sobre visión artificial en el agro", "Una integrante del equipo presentó una ponencia."),
            ("Aplausos sobre fondo rojo", "Aprender, aplicar y compartir. ¡Felicitaciones!")],
        tit="Compartir lo que aprendemos", bul=[("Ponencia", "En un congreso regional."),
                                                ("Visión artificial", "Aplicada al agro."),
                                                ("Del campo al aula", "Experiencia real.")],
        dato=None, cta="Conoce al equipo",
        tags=["#CulturaCorAll", "#InteligenciaArtificial", "#Universidad", "#EquipoCorAll"],
        vis="Empty university auditorium with a projector screen showing an agricultural vision diagram",
    ),
    dict(
        id="ia24", area="ia", sector="minería", tipo="cliente", pilar="producto",
        sec="matriz", mod="vision-epp",
        det="Se entregó el detector de uso de casco y chaleco en el ingreso a planta de {cliente}: analiza la imagen en el punto de acceso sin guardar rostros y alerta al supervisor; en la prueba de 5 días detectó 95 % de los ingresos sin equipo completo.",
        fuente="Detección de equipo de protección en el ingreso", valor=4,
        razon="Producto entregado con métrica de prueba y diseño respetuoso de la privacidad.",
        li="""El equipo de protección se verifica en la puerta, no después del incidente.

Entregamos un detector que revisa el uso de casco y chaleco en el ingreso a planta. Analiza la imagen en el punto de acceso, no guarda rostros y alerta al supervisor cuando alguien entra sin su equipo completo.

En una prueba de 5 días, detectó el 95 % de los ingresos sin equipo completo.

Seguridad con IA y con respeto por la privacidad. ¿Quieres reforzar tus controles de ingreso? Conversemos.""",
        fb="Detector de casco y chaleco en el ingreso a planta: no guarda rostros y alerta al supervisor. En 5 días de prueba detectó el 95 % de los casos.",
        ig="""🦺 Casco y chaleco, verificados en la puerta.
El detector no guarda rostros y alerta al supervisor. En 5 días de prueba detectó el 95 % de los casos.""",
        tt=[("Puerta de ingreso a planta", "La seguridad empieza en la puerta."),
            ("Íconos de casco y chaleco con check", "Este detector verifica casco y chaleco al ingresar."),
            ("Alerta al supervisor", "Sin guardar rostros. En 5 días detectó el 95 % de los casos.")],
        tit="Seguridad desde la puerta", bul=[("Casco y chaleco", "Verificados al ingresar."),
                                              ("Sin guardar rostros", "Privacidad primero."),
                                              ("Alerta al supervisor", "En el momento.")],
        dato="95 % de casos detectados en 5 días", cta="Conversemos",
        tags=["#SeguridadIndustrial", "#VisiónArtificial", "#Minería", "#InteligenciaArtificial"],
        vis="Plant entrance gate with a mounted camera and floating helmet and vest icons, no people",
    ),
    dict(
        id="ia25", area="ia", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Material para clientes del agro: qué se necesita para empezar con visión artificial (buena iluminación, cámara fija y fotos etiquetadas de los casos que interesan)",
        fuente="Cómo empezar con visión artificial en el agro", valor=3,
        razon="Contenido educativo general para clientes potenciales.",
        li="""¿Quieres usar visión artificial en tu planta? Antes del modelo, revisa esto.

1. Iluminación constante: la misma luz a toda hora evita sorpresas.
2. Cámara fija: siempre en el mismo ángulo y a la misma distancia.
3. Fotos etiquetadas: ejemplos reales de lo que quieres detectar.

Con estas tres bases, un piloto puede dar resultados en semanas. Sin ellas, cualquier modelo se complica. ¿Tienes un caso en mente? Conversemos.""",
        fb="Para empezar con visión artificial: iluminación constante, cámara fija y fotos etiquetadas de lo que quieres detectar. Con eso, un piloto avanza rápido.",
        ig="""📷 Antes del modelo, la base.
Iluminación constante, cámara fija y fotos etiquetadas. Así empieza un buen piloto de visión artificial.""",
        tt=[("Faja con fruta bajo una luz irregular", "¿Quieres usar visión artificial? Empieza por la luz."),
            ("Cámara fija en un soporte", "Luego, una cámara fija, siempre en el mismo ángulo."),
            ("Fotos con etiquetas", "Y fotos etiquetadas de lo que quieres detectar.")],
        tit="Antes del modelo, la base", bul=[("Iluminación constante", "La misma luz siempre."),
                                              ("Cámara fija", "Mismo ángulo y distancia."),
                                              ("Fotos etiquetadas", "Ejemplos reales.")],
        dato=None, cta="Conversemos",
        tags=["#VisiónArtificial", "#Agroindustria", "#InteligenciaArtificial", "#BuenasPrácticas"],
        vis="3D illustration of a camera on a fixed mount above a conveyor with a soft even light panel",
    ),
]
