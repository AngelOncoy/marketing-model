"""Publishable software tasks with their reference proposal content."""

CARDS = [
    dict(
        id="sw01", area="software", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="tienda-online/pedidos",
        det="Se terminó el flujo de pedido en 4 pasos para la tienda de {cliente}: elegir producto, personalizar, revisar y enviar el pedido por WhatsApp, sin pago en línea por ahora.",
        fuente="Flujo de pedido simplificado en la tienda", valor=4,
        razon="Funcionalidad terminada y visible para el cliente final; se describe el beneficio sin nombrar la tienda.",
        li="""Comprar en línea no tiene que ser complicado: 4 pasos y listo.

Muchos negocios pierden ventas porque su tienda pide demasiados datos antes de cerrar un pedido. Desarrollamos un flujo de compra en 4 pasos: eliges el producto, lo personalizas, revisas tu pedido y lo envías por WhatsApp.

El negocio recibe el pedido completo en el canal que ya usa todos los días para atender.

Desarrollo a medida para que vender sea más simple. ¿Tu tienda necesita algo así? Cuéntanos.""",
        fb="Un pedido en 4 pasos: eliges, personalizas, revisas y lo envías por WhatsApp. Así de simple es comprar en la tienda que desarrollamos. ¿Quieres una para tu negocio?",
        ig="""🛒 Comprar en 4 pasos.
Eliges, personalizas, revisas y envías tu pedido por WhatsApp. Una tienda pensada para vender sin complicaciones.""",
        tt=[("Celular mostrando el catálogo de una tienda", "¿Tu tienda en línea pide demasiados pasos?"),
            ("Dedo eligiendo y personalizando un producto", "Aquí eliges, personalizas y revisas tu pedido."),
            ("El pedido llegando por WhatsApp", "Y lo envías por WhatsApp. Solo 4 pasos.")],
        tit="Tu pedido en 4 pasos", bul=[("Elige y personaliza", "El producto a tu gusto."),
                                         ("Revisa tu pedido", "Todo claro antes de enviar."),
                                         ("Envía por WhatsApp", "El canal que ya usas.")],
        dato=None, cta="Cuéntanos",
        tags=["#ComercioElectrónico", "#TiendaOnline", "#DesarrolloWeb", "#Pymes"],
        vis="Smartphone mockup showing a simple online store checkout with four step indicators",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw02", area="software", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/rrhh",
        det="Despliegue del módulo de solicitudes de vacaciones en el ERP: el colaborador solicita desde el celular, el jefe aprueba con un clic y el saldo se actualiza solo. Usado por 18 colaboradores en la primera semana.",
        fuente="Módulo de solicitudes de vacaciones del ERP", valor=4,
        razon="Funcionalidad terminada y en uso real; se presenta sin datos personales.",
        li="""Pedir vacaciones ya no requiere un formato impreso ni tres correos.

En nuestro ERP desplegamos el módulo de solicitudes de vacaciones: el colaborador lo pide desde el celular, el jefe lo aprueba con un clic y el saldo de días se actualiza solo.

En la primera semana ya lo usaron 18 colaboradores.

Construimos herramientas que primero usamos nosotros. Si tu equipo aún gestiona esto en papel o en hojas sueltas, conversemos.""",
        fb="Vacaciones en un clic: el colaborador solicita desde el celular, el jefe aprueba y el saldo se actualiza solo. Ya lo usaron 18 colaboradores en la primera semana.",
        ig="""🌴 Vacaciones en un clic.
Solicitas desde el celular, tu jefe aprueba y el saldo se actualiza solo. 18 colaboradores ya lo usaron en la primera semana.""",
        tt=[("Formato impreso de vacaciones arrugado", "¿Todavía pides vacaciones con un formato impreso?"),
            ("Celular enviando la solicitud", "Ahora se solicita desde el celular."),
            ("Notificación de aprobación", "El jefe aprueba con un clic y el saldo se actualiza solo.")],
        tit="Vacaciones en un clic", bul=[("Solicita desde el celular", "Sin formatos impresos."),
                                          ("Aprobación en un clic", "El jefe responde al instante."),
                                          ("Saldo automático", "Siempre al día.")],
        dato="18 colaboradores en la primera semana", cta="Conversemos",
        tags=["#RecursosHumanos", "#ERP", "#TransformaciónDigital", "#SoftwareAMedida"],
        vis="Smartphone mockup with a vacation request approval screen, beach icon accent, office desk background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw03", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="corall-app/api",
        det="Se completó la revisión de permisos en /api/v1/tickets y /api/v1/pedidos: validación del propietario en el servidor, pruebas automáticas por rol y registro de accesos denegados.",
        fuente="Revisión de permisos por rol", valor=3, riesgo=3,
        razon="Se publica solo como consejo general de buenas prácticas, sin rutas ni detalles del trabajo interno.",
        li="""¿Cada usuario ve solo lo que le corresponde? Tres claves para lograrlo.

Cuando un sistema atiende a varias empresas o áreas, la seguridad no se resuelve solo con una pantalla de inicio de sesión. Estas son prácticas que aplicamos en nuestros desarrollos:

1. Validar en el servidor quién es el dueño de cada dato, no solo en la pantalla.
2. Probar automáticamente qué puede hacer cada rol.
3. Registrar los accesos denegados para detectar comportamientos extraños.

¿Tu sistema ya cumple con estas tres? Si tienes dudas, conversemos.""",
        fb="3 claves para que cada usuario vea solo lo suyo: validar en el servidor, probar cada rol automáticamente y registrar los accesos denegados. ¿Tu sistema las cumple?",
        ig="""🔐 3 claves para que cada usuario vea solo lo suyo.
Valida en el servidor, prueba cada rol y registra los accesos denegados. Seguridad que no depende de la pantalla.""",
        tt=[("Pantalla de inicio de sesión", "Un login no basta para proteger tus datos."),
            ("Diagrama simple de roles", "Valida en el servidor y prueba qué puede hacer cada rol."),
            ("Registro con accesos denegados", "Y registra los accesos denegados para detectar algo raro.")],
        tit="Que cada usuario vea lo suyo", bul=[("Valida en el servidor", "No solo en la pantalla."),
                                                 ("Prueba cada rol", "Con pruebas automáticas."),
                                                 ("Registra los rechazos", "Para detectar anomalías.")],
        dato=None, cta="Conversemos",
        tags=["#Ciberseguridad", "#BuenasPrácticas", "#DesarrolloDeSoftware", "#ProtecciónDeDatos"],
        vis="3D illustration of a shield with user profile icons separated into individual secure compartments",
    ),
    dict(
        id="sw04", area="software", sector="logística y transporte", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/tickets",
        det="Despliegue del tablero de tickets de soporte: estados por color, tiempo de primera respuesta y filtro por cliente. El tiempo promedio de primera respuesta bajó de 9 a 3 horas en 2 semanas.",
        fuente="Tablero de tickets de soporte", valor=4,
        razon="Funcionalidad terminada con mejora medible; se cuenta como beneficio, sin datos de clientes.",
        li="""Responder rápido también se diseña.

Desplegamos en nuestro ERP un tablero de tickets de soporte con estados por color, tiempo de primera respuesta visible y filtros para encontrar cada caso en segundos.

En 2 semanas, el tiempo promedio de primera respuesta bajó de 9 a 3 horas.

Cuando el equipo ve qué está pendiente, actúa antes. ¿Cómo gestionas hoy las solicitudes de tus clientes? Conversemos.""",
        fb="Nuevo tablero de tickets en nuestro ERP: en 2 semanas, la primera respuesta pasó de 9 a 3 horas en promedio. Ver lo pendiente ayuda a actuar antes.",
        ig="""⏱️ De 9 a 3 horas.
Así bajó el tiempo promedio de primera respuesta con nuestro nuevo tablero de tickets, en solo 2 semanas.""",
        tt=[("Bandeja de correo desordenada", "¿Tus solicitudes de soporte se pierden entre correos?"),
            ("Tablero con tickets por color", "Con este tablero, cada caso tiene estado y tiempo visible."),
            ("Indicador bajando de 9 a 3", "En 2 semanas, la primera respuesta bajó de 9 a 3 horas.")],
        tit="Respuestas más rápidas", bul=[("Estados por color", "Lo pendiente salta a la vista."),
                                           ("Tiempo visible", "Primera respuesta medida."),
                                           ("Filtros rápidos", "Cada caso en segundos.")],
        dato="De 9 a 3 horas de primera respuesta", cta="Conversemos",
        tags=["#AtenciónAlCliente", "#ERP", "#Productividad", "#SoftwareAMedida"],
        vis="Laptop mockup with a kanban support ticket board using red, grey and black status colors",
        vis_es="mockup de interfaz", comp="antes / después",
    ),
    dict(
        id="sw05", area="software", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="landing-exportador",
        det="Entrega de la versión en inglés y español de la landing de {cliente}, con autorización para mostrarla sin nombre: formulario de cotización y carga 40 % más rápida tras optimizar imágenes.",
        fuente="Landing bilingüe para un exportador", valor=4,
        razon="Entrega terminada con autorización para mostrarla sin nombre; resultado medible.",
        li="""Si exportas, tu web también tiene que hablar el idioma de tu comprador.

Entregamos la versión bilingüe, en inglés y español, de la landing de una empresa agroexportadora. Incluye un formulario de cotización directo y, tras optimizar las imágenes, carga un 40 % más rápido.

Un comprador internacional decide en segundos si sigue leyendo. Cada segundo cuenta.

¿Tu web está lista para el mercado exterior? Conversemos.""",
        fb="Landing bilingüe para una agroexportadora: inglés y español, formulario de cotización y carga 40 % más rápida. ¿Tu web está lista para exportar?",
        ig="""🌎 Tu web, lista para exportar.
Landing en inglés y español con formulario de cotización y carga 40 % más rápida.""",
        tt=[("Comprador revisando webs en una laptop (sin rostro)", "Un comprador internacional decide en segundos."),
            ("Landing cambiando de idioma", "Por eso la hicimos en inglés y español."),
            ("Indicador de velocidad mejorando", "Y ahora carga 40 % más rápido.")],
        tit="Tu web lista para exportar", bul=[("Inglés y español", "Para compradores de todo el mundo."),
                                               ("Cotización directa", "Un formulario simple."),
                                               ("Más rápida", "Carga 40 % más veloz.")],
        dato="40 % más rápida", cta="Conversemos",
        tags=["#Exportación", "#Agroexportación", "#DesarrolloWeb", "#Agroindustria"],
        vis="Desktop and mobile website mockups for an agricultural exporter with fresh produce imagery",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw06", area="software", sector="educación", tipo="interno", pilar="hito",
        sec="matriz", mod="corall-app",
        det="Cierre del sprint 10 del ERP: con el módulo de CRM, el sistema ya integra RR. HH., CRM, tickets y propuestas de marketing en una sola plataforma usada por todo el equipo.",
        fuente="ERP interno con cuatro módulos integrados", valor=4,
        razon="Hito interno terminado; muestra capacidad de desarrollo sin datos sensibles.",
        li="""Cuatro áreas, una sola plataforma.

Con el cierre de nuestro último sprint, el ERP que desarrollamos para nuestro propio equipo ya integra recursos humanos, CRM, tickets de soporte y propuestas de marketing.

Ya no saltamos entre hojas de cálculo, correos y chats para saber en qué va cada cosa: todo está en un mismo lugar.

Lo construimos para nosotros y hoy sabemos que puede ayudar a otras empresas. ¿Te gustaría conocerlo? Escríbenos.""",
        fb="Nuestro ERP ya integra recursos humanos, CRM, tickets y propuestas de marketing en una sola plataforma. Lo construimos para nosotros y puede ayudarte a ti.",
        ig="""🧩 Cuatro áreas, una plataforma.
Nuestro ERP ya integra recursos humanos, CRM, tickets y marketing. Todo en un mismo lugar.""",
        tt=[("Escritorio lleno de hojas y pestañas", "¿Trabajas saltando entre hojas, correos y chats?"),
            ("Pantalla del ERP con cuatro módulos", "Nuestro ERP integra recursos humanos, CRM, tickets y marketing."),
            ("Equipo trabajando ordenado (sin rostros)", "Todo en un solo lugar.")],
        tit="Cuatro áreas, una plataforma", bul=[("Recursos humanos", "Personas y solicitudes."),
                                                 ("CRM y tickets", "Clientes y soporte."),
                                                 ("Marketing", "Propuestas de contenido.")],
        dato=None, cta="Escríbenos",
        tags=["#ERP", "#TransformaciónDigital", "#SoftwareAMedida", "#Productividad"],
        vis="Laptop mockup of an ERP dashboard with four module tiles, clean modern office",
        vis_es="mockup de interfaz", comp="lista de 3 beneficios",
    ),
    dict(
        id="sw07", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Charla interna de buenas prácticas de Git: ramas por tarea, commits pequeños y revisión de código antes de integrar; se acordó compartir la guía como contenido educativo",
        fuente="Buenas prácticas de control de versiones", valor=3,
        razon="Contenido educativo general, sin datos internos.",
        li="""Un buen código empieza por un buen historial.

Esta semana repasamos con el equipo las prácticas de control de versiones que nos ayudan a trabajar sin pisarnos:

1. Una rama por tarea.
2. Commits pequeños y con mensajes claros.
3. Revisión de código antes de integrar.

Parecen reglas simples, pero son las que permiten volver atrás sin miedo y entender por qué se hizo cada cambio. ¿Cuál aplicas en tu equipo?""",
        fb="3 prácticas de Git que usamos a diario: una rama por tarea, commits pequeños y revisión de código antes de integrar. ¿Cuál aplicas tú?",
        ig="""🌿 3 prácticas para un historial limpio.
Una rama por tarea, commits pequeños y revisión antes de integrar.""",
        tt=[("Pantalla con un historial desordenado", "¿Tu historial de código es un caos?"),
            ("Diagrama de ramas limpio", "Usa una rama por tarea y commits pequeños."),
            ("Dos personas revisando código (sin rostros)", "Y revisa antes de integrar.")],
        tit="Un historial que se entiende", bul=[("Una rama por tarea", "Trabajo ordenado."),
                                                 ("Commits pequeños", "Cambios fáciles de revisar."),
                                                 ("Revisión de código", "Antes de integrar.")],
        dato=None, cta="Cuéntanos",
        tags=["#Git", "#BuenasPrácticas", "#DesarrolloDeSoftware", "#Programación"],
        vis="3D illustration of clean branching lines merging into a main line, minimalist tech style",
    ),
    dict(
        id="sw08", area="software", sector="cuero y calzado", tipo="cliente", pilar="producto",
        sec="matriz", mod="portal-clientes",
        det="Se desplegó el seguimiento de pedidos en el portal de {cliente}: el comprador ve en qué etapa está su pedido (corte, aparado, armado, despacho) sin llamar a la fábrica.",
        fuente="Seguimiento de pedidos por etapa", valor=4,
        razon="Funcionalidad terminada y visible para el cliente final; se cuenta sin nombrar a la fábrica.",
        li=""""¿En qué va mi pedido?" Ahora la respuesta está en la pantalla.

En una fábrica de calzado, cada llamada de un comprador interrumpe la producción. Desplegamos en su portal el seguimiento de pedidos por etapa: corte, aparado, armado y despacho.

El comprador revisa el avance cuando quiere y el equipo de planta se concentra en producir.

Software a medida para la industria del calzado. ¿Tus clientes preguntan lo mismo todos los días? Conversemos.""",
        fb="Seguimiento de pedidos para una fábrica de calzado: corte, aparado, armado y despacho visibles en el portal. Menos llamadas, más producción.",
        ig="""👟 ¿En qué va mi pedido?
Corte, aparado, armado y despacho: tu comprador lo ve en el portal sin llamar a la fábrica.""",
        tt=[("Teléfono sonando en una fábrica", "¿Tus compradores llaman todo el día para preguntar por su pedido?"),
            ("Portal con las etapas del pedido", "Ahora ven en qué etapa está: corte, aparado, armado o despacho."),
            ("Operario trabajando tranquilo (sin rostro)", "Y tu equipo se concentra en producir.")],
        tit="Tu pedido, etapa por etapa", bul=[("Cuatro etapas", "De corte a despacho."),
                                               ("Sin llamadas", "El comprador consulta solo."),
                                               ("Más foco", "Planta concentrada en producir.")],
        dato=None, cta="Conversemos",
        tags=["#Calzado", "#SoftwareAMedida", "#Trazabilidad", "#Industria40"],
        vis="Tablet mockup showing an order tracking timeline with four stages, leather workshop background",
        vis_es="mockup de interfaz", comp="línea de tiempo",
    ),
    dict(
        id="sw09", area="software", sector="educación", tipo="interno", pilar="evento",
        sec="anexado", mod="-",
        det="Confirmado el taller de difusión del ERP para mypes: jueves 27 de noviembre, 16:00 a 18:00, en la sede de CorAll en Trujillo; ingreso libre con registro previo; cofinanciado por un programa público de innovación",
        fuente="Taller de difusión del ERP para mypes", valor=5,
        razon="Evento confirmado con fecha, hora, lugar y registro; ideal para convocatoria.",
        li="""¿Tu mype sigue gestionando todo en hojas de cálculo? Te invitamos a ver otra forma de hacerlo.

Realizaremos el taller de difusión de nuestro ERP para mypes, donde mostraremos cómo ordenar personal, clientes y soporte en una sola plataforma.

📅 Jueves 27 de noviembre
🕓 16:00 a 18:00
📍 Sede de CorAll, Trujillo

Ingreso libre con registro previo. Te esperamos.""",
        fb="Taller gratuito de difusión del ERP para mypes: jueves 27 de noviembre, 16:00 a 18:00, en nuestra sede de Trujillo. Regístrate en el enlace.",
        ig="""📣 Taller ERP para mypes.
Jueves 27 de noviembre, 16:00 a 18:00, sede de CorAll en Trujillo. Ingreso libre con registro previo.""",
        tt=[("Hojas de cálculo desordenadas", "¿Tu negocio vive en hojas de cálculo?"),
            ("Pantalla del ERP ordenada", "Ven a conocer nuestro ERP para mypes."),
            ("Sala preparada para el taller", "Jueves 27 de noviembre, 16:00. Ingreso libre con registro.")],
        tit="Taller ERP para mypes", bul=[("Jueves 27 de noviembre", "De 16:00 a 18:00."),
                                          ("Sede de CorAll", "Trujillo."),
                                          ("Ingreso libre", "Con registro previo.")],
        dato="Jueves 27 de noviembre, 16:00", cta="Regístrate",
        tags=["#Mypes", "#ERP", "#TallerGratuito", "#Trujillo"],
        vis="Modern seminar room with a projector screen and empty chairs, red and black geometric accents",
    ),
    dict(
        id="sw10", area="software", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="portal-clientes/reportes",
        det="Se entregaron los reportes descargables en PDF y Excel para el portal de {cliente}: ventas por día, por producto y por vendedor, generados en menos de 5 segundos.",
        fuente="Reportes descargables en el portal", valor=3,
        razon="Funcionalidad terminada y visible para el usuario; beneficio claro sin datos del cliente.",
        li="""El reporte que pedías cada lunes ahora sale en segundos.

Entregamos reportes descargables en PDF y Excel dentro del portal de un cliente: ventas por día, por producto y por vendedor.

Ya no hay que pedirle a nadie que arme el archivo: el usuario lo genera cuando lo necesita.

Datos a la mano para decidir más rápido. ¿Qué reporte te gustaría tener en un clic? Cuéntanos.""",
        fb="Reportes en PDF y Excel en un clic: ventas por día, por producto y por vendedor, listos cuando los necesitas. ¿Qué reporte te falta?",
        ig="""📊 Tu reporte, en un clic.
Ventas por día, por producto y por vendedor, en PDF o Excel, listos cuando los necesitas.""",
        tt=[("Persona esperando un correo con un archivo (sin rostro)", "¿Esperas cada lunes a que te envíen el reporte?"),
            ("Botón de descarga en el portal", "Ahora lo descargas en PDF o Excel."),
            ("Reporte abierto con gráficos", "Ventas por día, producto y vendedor, en segundos.")],
        tit="Tu reporte en un clic", bul=[("PDF o Excel", "El formato que prefieras."),
                                          ("Tres vistas", "Día, producto y vendedor."),
                                          ("En segundos", "Sin pedirlo a nadie.")],
        dato=None, cta="Cuéntanos",
        tags=["#Reportes", "#AnálisisDeDatos", "#SoftwareAMedida", "#Ventas"],
        vis="Laptop mockup with a sales report and charts, PDF and spreadsheet icons floating nearby",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw11", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="corall-app/auth",
        det="Se activó el doble factor de autenticación para todas las cuentas del ERP con aplicación autenticadora; se escribió una guía para el equipo.",
        fuente="Doble factor de autenticación en el ERP", valor=3, riesgo=2,
        razon="Se puede compartir como recomendación general de seguridad sin detalles internos.",
        li="""Una contraseña sola ya no es suficiente.

Activamos el doble factor de autenticación en todas las cuentas de nuestro ERP. Así, aunque alguien conozca una contraseña, necesita también un código que solo tiene el usuario en su celular.

Si tu empresa usa sistemas con datos de clientes o de personal, te recomendamos:

- Activar el doble factor en todas las cuentas.
- Usar una aplicación autenticadora en lugar de SMS cuando sea posible.
- Explicarle al equipo por qué es importante.

¿Ya lo activaste? Si necesitas ayuda, conversemos.""",
        fb="¿Tus sistemas tienen doble factor de autenticación? Nosotros lo activamos en todas las cuentas del ERP. Te recomendamos hacerlo también.",
        ig="""🔑 Una contraseña ya no basta.
Activa el doble factor de autenticación y usa una aplicación autenticadora. Tus datos te lo agradecerán.""",
        tt=[("Pantalla de contraseña", "¿Solo una contraseña protege tus sistemas?"),
            ("Celular mostrando un código", "Con el doble factor, también necesitas un código del celular."),
            ("Candado cerrándose en pantalla", "Actívalo en todas las cuentas.")],
        tit="Una contraseña ya no basta", bul=[("Activa el doble factor", "En todas las cuentas."),
                                               ("Usa una app", "Mejor que SMS."),
                                               ("Explica al equipo", "La seguridad es de todos.")],
        dato=None, cta="Conversemos",
        tags=["#Ciberseguridad", "#BuenasPrácticas", "#ProtecciónDeDatos", "#Seguridad"],
        vis="3D illustration of a smartphone showing a one-time code next to a padlock, clean background",
    ),
    dict(
        id="sw12", area="software", sector="agroindustria", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/crm",
        det="Despliegue del embudo de oportunidades en el CRM del ERP: etapas arrastrables, recordatorios de seguimiento y vista de oportunidades por sector. El equipo comercial registró 35 oportunidades en la primera semana.",
        fuente="Embudo de oportunidades en el CRM", valor=4,
        razon="Funcionalidad terminada y en uso interno; se presenta como capacidad del producto.",
        li="""Una oportunidad sin seguimiento es una venta perdida.

Desplegamos en nuestro ERP el embudo de oportunidades del CRM: etapas que se mueven arrastrando, recordatorios de seguimiento y una vista por sector.

En la primera semana, nuestro equipo comercial registró 35 oportunidades y sabe en qué etapa está cada una.

¿Tu equipo comercial trabaja con una hoja de cálculo que nadie actualiza? Conversemos.""",
        fb="Nuevo embudo de oportunidades en nuestro CRM: etapas arrastrables, recordatorios y vista por sector. 35 oportunidades registradas en la primera semana.",
        ig="""🎯 Cada oportunidad, con seguimiento.
Embudo con etapas arrastrables y recordatorios. 35 oportunidades registradas en la primera semana.""",
        tt=[("Hoja de cálculo desactualizada", "¿Tu equipo comercial pierde oportunidades por falta de seguimiento?"),
            ("Tarjetas moviéndose entre etapas", "En nuestro CRM, cada oportunidad avanza arrastrando."),
            ("Recordatorio en pantalla", "Con recordatorios, nadie se olvida de llamar.")],
        tit="Ninguna oportunidad olvidada", bul=[("Etapas arrastrables", "Avance visible."),
                                                 ("Recordatorios", "Seguimiento a tiempo."),
                                                 ("Vista por sector", "Dónde está la demanda.")],
        dato="35 oportunidades en la primera semana", cta="Conversemos",
        tags=["#CRM", "#Ventas", "#ERP", "#SoftwareAMedida"],
        vis="Laptop mockup of a sales pipeline board with cards in columns, red accent color",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw13", area="software", sector="educación", tipo="cliente", pilar="producto",
        sec="matriz", mod="plataforma-colegio",
        det="Entrega de la libreta de notas digital para un colegio con autorización para difundir sin nombre: los padres consultan notas y asistencia desde el celular; 320 familias activaron su cuenta en la primera semana.",
        fuente="Libreta de notas digital para un colegio", valor=4,
        razon="Proyecto entregado con autorización y adopción medible.",
        li="""Las notas ya no esperan al fin del bimestre.

Entregamos a un colegio su libreta de notas digital: madres y padres consultan notas y asistencia desde el celular, cuando lo necesitan.

En la primera semana, 320 familias activaron su cuenta.

Cuando la información llega a tiempo, acompañar a los hijos es más fácil. ¿Tu institución quiere dar este paso? Conversemos.""",
        fb="Libreta de notas digital para un colegio: notas y asistencia desde el celular. 320 familias la activaron en la primera semana.",
        ig="""📚 Notas y asistencia en el celular.
Entregamos una libreta de notas digital: 320 familias activaron su cuenta en la primera semana.""",
        tt=[("Libreta de notas de papel", "¿Te enteras de las notas recién al final del bimestre?"),
            ("Celular con notas y asistencia", "Con la libreta digital, las ves cuando quieras."),
            ("Contador llegando a 320", "320 familias la activaron en la primera semana.")],
        tit="Las notas, siempre a la mano", bul=[("Notas en el celular", "Cuando las necesites."),
                                                 ("Asistencia diaria", "Información a tiempo."),
                                                 ("Fácil de activar", "Para cada familia.")],
        dato="320 familias en la primera semana", cta="Conversemos",
        tags=["#Educación", "#TecnologíaEducativa", "#Colegios", "#SoftwareAMedida"],
        vis="Smartphone mockup showing a school grades and attendance screen, school notebook in background",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw14", area="software", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Hackatón interno de un día: 3 equipos construyeron prototipos para el ERP; ganó un asistente de búsqueda de tickets. Todos aceptaron aparecer en la foto grupal",
        fuente="Hackatón interno del equipo", valor=4,
        razon="Contenido de cultura con consentimiento; muestra innovación del equipo.",
        li="""Un día, 3 equipos y una regla: terminar algo que funcione.

Realizamos nuestro primer hackatón interno. Los 3 equipos construyeron prototipos para nuestro ERP y el ganador fue un asistente para encontrar tickets de soporte más rápido.

Más allá del premio, nos llevamos ideas nuevas, mucho aprendizaje y la confirmación de que nuestro laboratorio más valioso es el propio equipo.

¡Gracias a todos por participar!""",
        fb="Primer hackatón interno: 3 equipos, prototipos para nuestro ERP y un ganador, un asistente para buscar tickets más rápido. ¡Gracias, equipo!",
        ig="""💡 Hackatón CorAll.
3 equipos, un día y prototipos que funcionan. Ganó un asistente para encontrar tickets más rápido.""",
        tt=[("Reloj marcando el inicio", "Un día para construir algo que funcione."),
            ("Equipos trabajando en laptops (sin rostros)", "3 equipos, prototipos para nuestro ERP."),
            ("Foto grupal con overlay rojo", "Y un ganador: un asistente para buscar tickets.")],
        tit="Nuestro primer hackatón", bul=[("3 equipos", "Un solo día."),
                                            ("Prototipos reales", "Para nuestro ERP."),
                                            ("Ideas nuevas", "Que seguiremos trabajando.")],
        dato=None, cta="Conoce al equipo",
        tags=["#Hackatón", "#CulturaCorAll", "#Innovación", "#EquipoCorAll"],
        vis="Office space with laptops, sticky notes and coffee cups during a hackathon, energetic lighting",
        adj="equipo",
    ),
    dict(
        id="sw15", area="software", sector="logística y transporte", tipo="cliente", pilar="producto",
        sec="matriz", mod="app-despachos",
        det="Entrega de la app de despachos para {cliente}: el conductor registra la entrega con foto y firma en el celular y funciona sin conexión; se sincroniza al recuperar señal. Probada en 150 entregas.",
        fuente="App de despachos con modo sin conexión", valor=4,
        razon="Producto entregado y probado en operación; se describe sin nombrar al cliente.",
        li="""La prueba de entrega no puede depender de la señal del celular.

Entregamos una app de despachos donde el conductor registra cada entrega con foto y firma. Si no hay señal, la app guarda todo y lo sincroniza apenas recupera conexión.

Ya la probamos en 150 entregas reales.

Menos papeles, menos reclamos y la central sabe qué se entregó. ¿Tu equipo de reparto necesita algo así? Conversemos.""",
        fb="App de despachos con foto y firma de entrega que funciona sin señal y se sincroniza sola. Probada en 150 entregas reales.",
        ig="""📦 Entregas con prueba, aun sin señal.
Foto y firma desde el celular; la app sincroniza sola al recuperar conexión. Probada en 150 entregas.""",
        tt=[("Conductor entregando un paquete (sin rostro)", "¿Cómo pruebas una entrega cuando no hay señal?"),
            ("Celular tomando foto y firma", "Con esta app registras foto y firma, sin conexión."),
            ("Ícono de sincronización completándose", "Y se sincroniza sola. Ya la probamos en 150 entregas.")],
        tit="Entregas con prueba", bul=[("Foto y firma", "Desde el celular."),
                                        ("Sin conexión", "Guarda y sincroniza después."),
                                        ("Menos reclamos", "Cada entrega registrada.")],
        dato="Probada en 150 entregas", cta="Conversemos",
        tags=["#Logística", "#AppMóvil", "#ÚltimaMilla", "#SoftwareAMedida"],
        vis="Smartphone mockup showing a delivery confirmation with photo and signature, delivery van behind",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw16", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="matriz", mod="infra/backups",
        det="Prueba de restauración del respaldo completada: se restauró la base de datos en un entorno aislado en 12 minutos y se documentó el procedimiento.",
        fuente="Prueba de restauración de respaldos", valor=3, riesgo=2,
        razon="Se comparte como buena práctica general (probar respaldos), sin detalles de infraestructura.",
        li="""Un respaldo que nunca restauraste es solo una esperanza.

Muchas empresas hacen copias de seguridad, pero pocas prueban si realmente pueden recuperarlas. Nosotros lo hicimos: restauramos nuestra base de datos en un entorno aislado en 12 minutos y documentamos cada paso.

Recomendación: programa una prueba de restauración periódica y mide cuánto tarda. El día que la necesites, sabrás exactamente qué hacer.

¿Cuándo fue la última vez que probaste tus respaldos?""",
        fb="¿Pruebas tus respaldos? Nosotros restauramos nuestra base de datos en 12 minutos en un entorno aislado. Haz tu prueba periódica.",
        ig="""💾 ¿Tu respaldo funciona de verdad?
Pruébalo. Nosotros restauramos nuestra base de datos en 12 minutos y documentamos cada paso.""",
        tt=[("Disco con etiqueta 'respaldo'", "¿Tienes respaldos? ¿Y ya probaste restaurarlos?"),
            ("Barra de progreso de restauración", "Nosotros lo probamos: 12 minutos en un entorno aislado."),
            ("Checklist completado", "Prueba tus respaldos de forma periódica.")],
        tit="¿Tu respaldo funciona?", bul=[("Restaura de prueba", "En un entorno aislado."),
                                           ("Mide el tiempo", "Saber cuánto tarda."),
                                           ("Documenta los pasos", "Para el día que lo necesites.")],
        dato="Restauración en 12 minutos", cta="Cuéntanos",
        tags=["#Ciberseguridad", "#BuenasPrácticas", "#Respaldo", "#ContinuidadDelNegocio"],
        vis="3D illustration of a database cylinder with a circular restore arrow and a stopwatch",
    ),
    dict(
        id="sw17", area="software", sector="cuero y calzado", tipo="cliente", pilar="catalogo",
        sec="matriz", mod="catalogo-digital",
        det="Se publicó el catálogo digital de {cliente} con autorización para mostrarlo sin nombre: 3 líneas de calzado, filtros por talla y color, y pedido mayorista por formulario.",
        fuente="Catálogo digital para una marca de calzado", valor=4,
        razon="Entrega terminada con autorización para mostrarla sin nombre.",
        li="""El catálogo de papel ya no alcanza para vender a todo el país.

Publicamos el catálogo digital de una marca de calzado de Trujillo: 3 líneas de producto, filtros por talla y color, y un formulario para pedidos mayoristas.

Ahora sus clientes revisan modelos y hacen pedidos desde cualquier ciudad, sin esperar la visita del vendedor.

¿Tu marca quiere vender más allá de su local? Conversemos.""",
        fb="Catálogo digital para una marca de calzado: 3 líneas, filtros por talla y color y pedidos mayoristas por formulario. Vende más allá de tu local.",
        ig="""👠 Tu catálogo, en todo el país.
3 líneas de calzado, filtros por talla y color y pedidos mayoristas en línea.""",
        tt=[("Catálogo de papel sobre un mostrador", "¿Todavía vendes con catálogo de papel?"),
            ("Celular filtrando calzado por talla", "Este catálogo digital filtra por talla y color."),
            ("Formulario de pedido mayorista", "Y recibe pedidos mayoristas desde cualquier ciudad.")],
        tit="Tu catálogo en todo el país", bul=[("Tres líneas", "Todos los modelos en línea."),
                                                ("Talla y color", "Filtros fáciles."),
                                                ("Pedido mayorista", "Por formulario.")],
        dato=None, cta="Conversemos",
        tags=["#Calzado", "#CatálogoDigital", "#ComercioElectrónico", "#HechoEnTrujillo"],
        vis="Tablet and phone mockups of a digital shoe catalog with product grid, leather textures",
        vis_es="mockup de interfaz", comp="grilla",
    ),
    dict(
        id="sw18", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se preparó contenido educativo sobre la Ley 29733 de protección de datos personales: qué datos pedir, para qué y cómo guardarlos, pensado para mypes que usan formularios web",
        fuente="Protección de datos personales para mypes", valor=4,
        razon="Contenido educativo de interés general; no contiene datos internos.",
        li="""¿Tu formulario web pide más datos de los que necesitas?

En el Perú, la Ley 29733 protege los datos personales. Para una mype que vende o atiende en línea, tres preguntas ayudan a empezar:

1. ¿Qué datos pido? Solo los necesarios.
2. ¿Para qué los uso? Dilo claramente y pide consentimiento.
3. ¿Dónde los guardo? Con acceso restringido y seguro.

Cuidar los datos de tus clientes también es cuidar tu reputación. ¿Quieres revisar tus formularios? Conversemos.""",
        fb="Ley 29733: pide solo los datos necesarios, explica para qué los usas y guárdalos de forma segura. Cuidar los datos de tus clientes es cuidar tu negocio.",
        ig="""🛡️ ¿Pides más datos de los que necesitas?
Ley 29733: pide lo necesario, explica para qué y guárdalo con acceso restringido.""",
        tt=[("Formulario web con muchos campos", "¿Tu formulario pide demasiados datos?"),
            ("Tres íconos: lista, objetivo y candado", "Pide solo lo necesario, explica para qué y guárdalo seguro."),
            ("Texto de la Ley 29733 en pantalla", "Así cumples con la Ley 29733.")],
        tit="Cuida los datos de tus clientes", bul=[("Pide lo necesario", "Solo los datos útiles."),
                                                    ("Explica para qué", "Y pide consentimiento."),
                                                    ("Guarda con seguridad", "Acceso restringido.")],
        dato=None, cta="Conversemos",
        tags=["#ProtecciónDeDatos", "#Ley29733", "#Mypes", "#BuenasPrácticas"],
        vis="3D illustration of a web form card protected by a shield and padlock, soft grey background",
    ),
    dict(
        id="sw19", area="software", sector="logística y transporte", tipo="cliente", pilar="servicio_territorio",
        sec="anexado", mod="-",
        det="Capacitación presencial a 12 operadores de un almacén sobre el uso del sistema de inventario, con autorización del cliente para publicar sin nombre ni fotos de personas",
        fuente="Capacitación en sistema de inventario", valor=3,
        razon="Servicio terminado con autorización para publicarlo sin nombres ni rostros.",
        li="""Un sistema solo funciona si el equipo sabe usarlo.

Capacitamos de forma presencial a 12 operadores de un almacén en el uso de su nuevo sistema de inventario: registro de ingresos, salidas y conteos, con práctica en sus propios equipos.

Acompañar la adopción es parte del proyecto, no un extra.

¿Tu equipo necesita apoyo para adoptar una herramienta nueva? Conversemos.""",
        fb="Capacitamos a 12 operadores de un almacén en su nuevo sistema de inventario. Acompañar la adopción es parte del proyecto.",
        ig="""🏭 Acompañamos la adopción.
Capacitamos a 12 operadores de un almacén en su nuevo sistema de inventario, con práctica en sus propios equipos.""",
        tt=[("Estantes de un almacén", "Un sistema nuevo no sirve si nadie sabe usarlo."),
            ("Pantalla del sistema de inventario", "Por eso capacitamos a 12 operadores en su propio almacén."),
            ("Lector de códigos registrando una caja", "Ingresos, salidas y conteos, practicando con sus equipos.")],
        tit="Acompañamos la adopción", bul=[("12 operadores", "Capacitados en sitio."),
                                            ("Práctica real", "En sus propios equipos."),
                                            ("Adopción", "Parte del proyecto.")],
        dato="12 operadores capacitados", cta="Conversemos",
        tags=["#Capacitación", "#Logística", "#Inventarios", "#TransformaciónDigital"],
        vis="Warehouse aisle with shelves and a tablet showing an inventory system, no people",
    ),
    dict(
        id="sw20", area="software", sector="educación", tipo="interno", pilar="producto",
        sec="matriz", mod="corall-app/propuestas-ia",
        det="Se habilitó la bandeja de revisión de propuestas de marketing en el ERP: cada propuesta queda en borrador, aprobada o rechazada con motivo, y puede editarse en línea antes de pasar a la parrilla.",
        fuente="Bandeja de revisión de propuestas de marketing", valor=3,
        razon="Funcionalidad terminada que muestra el enfoque de supervisión humana; sin datos internos.",
        li="""La inteligencia artificial propone; el equipo decide.

Habilitamos en nuestro ERP una bandeja de revisión para las propuestas de marketing: cada una queda como borrador, aprobada o rechazada con motivo, y se puede editar en línea antes de pasar a la parrilla de contenido.

Creemos que la IA ayuda a avanzar más rápido, pero la última palabra la tiene una persona.

¿Cómo revisa tu equipo lo que genera la IA? Cuéntanos.""",
        fb="En nuestro ERP, la IA propone y el equipo decide: cada propuesta de marketing se aprueba, se edita o se rechaza con motivo antes de publicarse.",
        ig="""🤝 La IA propone, el equipo decide.
Cada propuesta de marketing se aprueba, se edita o se rechaza con motivo antes de publicarse.""",
        tt=[("Pantalla con una propuesta generada", "La IA puede proponer contenido en segundos."),
            ("Botones aprobar, editar y rechazar", "Pero en nuestro ERP, cada propuesta pasa por revisión."),
            ("Persona editando el texto (sin rostro)", "La última palabra la tiene el equipo.")],
        tit="La IA propone, tú decides", bul=[("Borrador", "Toda propuesta empieza aquí."),
                                              ("Edición en línea", "Ajustes antes de publicar."),
                                              ("Aprobación humana", "Con motivo si se rechaza.")],
        dato=None, cta="Cuéntanos",
        tags=["#InteligenciaArtificial", "#Marketing", "#ERP", "#IAResponsable"],
        vis="Laptop mockup of a content review inbox with approve and reject states, soft red accents",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw21", area="software", sector="agroindustria", tipo="cliente", pilar="producto",
        sec="matriz", mod="app-cosecha",
        det="Entrega de la app de registro de cosecha para {cliente}: cada cuadrilla registra jabas por lote desde el celular y el ingeniero ve el avance del día en un tablero. Usada por 8 cuadrillas en la primera campaña.",
        fuente="App de registro de cosecha por lote", valor=4,
        razon="Producto entregado y en uso con cifras de adopción; sin datos del cliente.",
        li="""¿Cuántas jabas se cosecharon hoy en cada lote? El ingeniero ya no espera al final del día para saberlo.

Entregamos una app de registro de cosecha: cada cuadrilla registra sus jabas por lote desde el celular y el ingeniero de campo ve el avance en un tablero, en tiempo real.

En la primera campaña ya la usaron 8 cuadrillas.

Datos de campo para decidir en el momento. ¿Tu fundo aún registra la cosecha en papel? Conversemos.""",
        fb="App de registro de cosecha: cada cuadrilla registra jabas por lote y el ingeniero ve el avance en tiempo real. 8 cuadrillas la usaron en la primera campaña.",
        ig="""🍇 La cosecha, en tiempo real.
Cada cuadrilla registra sus jabas por lote desde el celular. 8 cuadrillas ya la usaron en la primera campaña.""",
        tt=[("Jabas apiladas en el campo", "¿Registras la cosecha en papel?"),
            ("Celular registrando jabas por lote", "Con esta app, cada cuadrilla registra desde el celular."),
            ("Tablero con el avance del día", "Y el ingeniero ve el avance en tiempo real.")],
        tit="La cosecha en tiempo real", bul=[("Registro por lote", "Desde el celular."),
                                              ("Tablero en vivo", "Avance del día."),
                                              ("Sin papeles", "Menos errores de digitación.")],
        dato="8 cuadrillas en la primera campaña", cta="Conversemos",
        tags=["#Agroindustria", "#AppMóvil", "#AgriculturaDigital", "#SoftwareAMedida"],
        vis="Smartphone mockup over a vineyard harvest scene with stacked crates, warm sunlight",
        vis_es="mockup de interfaz",
    ),
    dict(
        id="sw22", area="software", sector="educación", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se armó una guía para clientes sobre cómo pedir un software a medida: definir el problema, priorizar funciones y empezar por un piloto pequeño",
        fuente="Guía para pedir un software a medida", valor=4,
        razon="Contenido educativo útil para potenciales clientes; sin datos internos.",
        li="""Antes de pedir un software a medida, responde estas tres preguntas.

1. ¿Qué problema quiero resolver? No "quiero una app", sino "pierdo pedidos porque los anoto a mano".
2. ¿Qué es lo mínimo que necesito? Prioriza; lo demás puede esperar.
3. ¿Dónde lo pruebo primero? Un piloto pequeño muestra rápido si funciona.

Así se evitan proyectos largos que no resuelven lo importante. ¿Tienes un problema así en tu negocio? Cuéntanos.""",
        fb="Antes de pedir un software a medida: define el problema, prioriza lo mínimo y empieza por un piloto pequeño. ¿Te ayudamos a definirlo?",
        ig="""🧭 ¿Vas a pedir un software a medida?
Define el problema, prioriza lo mínimo y empieza con un piloto pequeño.""",
        tt=[("Persona frente a una pizarra en blanco (sin rostro)", "¿Quieres un software a medida? Primero define el problema."),
            ("Lista de funciones tachándose", "Luego prioriza lo mínimo que necesitas."),
            ("Pequeño piloto funcionando", "Y empieza con un piloto pequeño.")],
        tit="Antes de pedir tu software", bul=[("Define el problema", "No la solución."),
                                               ("Prioriza lo mínimo", "Lo demás puede esperar."),
                                               ("Empieza con un piloto", "Pequeño y medible.")],
        dato=None, cta="Cuéntanos",
        tags=["#SoftwareAMedida", "#Pymes", "#TransformaciónDigital", "#BuenasPrácticas"],
        vis="3D illustration of a compass over a simple project roadmap with three milestones",
    ),
    dict(
        id="sw23", area="software", sector="logística y transporte", tipo="cliente", pilar="hito",
        sec="matriz", mod="tienda-online",
        det="La tienda en línea de {cliente} cumplió su primer mes en producción: en 30 días recibió 210 pedidos por el nuevo flujo; el cliente autorizó compartir la cifra sin su nombre.",
        fuente="Primer mes de una tienda en línea", valor=5,
        razon="Hito con resultado real y autorización para compartir la cifra sin nombre.",
        li="""Primer mes en línea: 210 pedidos.

Hace un mes pusimos en producción la tienda en línea de un negocio local con un flujo de pedido simple y atención por WhatsApp. En sus primeros 30 días recibió 210 pedidos por el nuevo canal.

Cuando comprar es fácil, el cliente vuelve.

¿Tu negocio está listo para vender en línea? Conversemos.""",
        fb="Primer mes de una tienda en línea que desarrollamos: 210 pedidos en 30 días por el nuevo canal. ¿Empezamos la tuya?",
        ig="""🎉 210 pedidos en su primer mes.
Una tienda en línea simple, con atención por WhatsApp. Cuando comprar es fácil, el cliente vuelve.""",
        tt=[("Calendario pasando 30 días", "Un mes en línea."),
            ("Notificaciones de pedidos llegando", "210 pedidos por el nuevo canal."),
            ("Tienda en el celular", "Cuando comprar es fácil, el cliente vuelve.")],
        tit="210 pedidos en un mes", bul=[("Flujo simple", "Pedido en pocos pasos."),
                                          ("Atención por WhatsApp", "El canal del cliente."),
                                          ("30 días", "Resultados desde el inicio.")],
        dato="210 pedidos en 30 días", cta="Conversemos",
        tags=["#ComercioElectrónico", "#TiendaOnline", "#Pymes", "#DesarrolloWeb"],
        vis="Smartphone with an online store and a stream of order notification bubbles rising",
        comp="dato destacado",
    ),
    dict(
        id="sw24", area="software", sector="educación", tipo="interno", pilar="cultura",
        sec="anexado", mod="-",
        det="Celebración del Día del Programador con el equipo: desayuno y reconocimiento a quienes mentorearon practicantes este año; se tomó foto grupal con consentimiento",
        fuente="Día del Programador", valor=3,
        razon="Fecha especial de cultura con consentimiento para la foto.",
        li="""Feliz Día del Programador a quienes convierten problemas en soluciones.

Hoy celebramos con un desayuno y un reconocimiento especial a quienes, además de programar, dedicaron tiempo a guiar a nuestros practicantes este año.

Enseñar también es construir.

¡Gracias, equipo!""",
        fb="¡Feliz Día del Programador! Hoy reconocimos a quienes, además de programar, guiaron a nuestros practicantes este año. Enseñar también es construir.",
        ig="""💻 ¡Feliz Día del Programador!
Gracias a quienes convierten problemas en soluciones y además enseñan a los que vienen.""",
        tt=[("Taza de café junto a un teclado", "Hoy es el Día del Programador."),
            ("Desayuno del equipo (sin rostros)", "Lo celebramos con el equipo."),
            ("Foto grupal con overlay rojo", "Gracias a quienes enseñan mientras construyen.")],
        tit="Feliz Día del Programador", bul=[("Gracias, equipo", "Por cada solución."),
                                              ("Mentores", "Que guían a los que vienen."),
                                              ("Enseñar construye", "Equipo que crece.")],
        dato=None, cta="Conoce al equipo",
        tags=["#DíaDelProgramador", "#CulturaCorAll", "#EquipoCorAll", "#Programación"],
        vis="Coffee mug next to a mechanical keyboard and code on screen, celebratory confetti in brand colors",
        adj="equipo",
    ),
    dict(
        id="sw25", area="software", sector="agroindustria", tipo="interno", pilar="educativo",
        sec="anexado", mod="-",
        det="Se documentó para el equipo comercial la diferencia entre una web informativa, una tienda en línea y un sistema a medida, para orientar a los clientes según su necesidad",
        fuente="Web, tienda o sistema a medida", valor=3,
        razon="Contenido educativo general que orienta a potenciales clientes.",
        li="""¿Web, tienda en línea o sistema a medida? Depende de lo que quieras lograr.

- Web informativa: para que te encuentren y sepan qué haces.
- Tienda en línea: para vender y recibir pedidos.
- Sistema a medida: para ordenar procesos internos que ninguna herramienta estándar resuelve.

Elegir bien evita pagar por algo que no necesitas. ¿No sabes cuál es la tuya? Conversemos.""",
        fb="¿Web, tienda en línea o sistema a medida? Web para que te encuentren, tienda para vender y sistema para ordenar tus procesos. Te ayudamos a elegir.",
        ig="""🤔 ¿Web, tienda o sistema?
Web para que te encuentren, tienda para vender y sistema a medida para ordenar tus procesos.""",
        tt=[("Tres pantallas distintas", "¿Web, tienda en línea o sistema a medida?"),
            ("Web informativa y luego tienda", "Web para que te encuentren; tienda para vender."),
            ("Sistema con procesos internos", "Y sistema a medida para ordenar tus procesos.")],
        tit="¿Web, tienda o sistema?", bul=[("Web informativa", "Para que te encuentren."),
                                            ("Tienda en línea", "Para vender."),
                                            ("Sistema a medida", "Para ordenar procesos.")],
        dato=None, cta="Conversemos",
        tags=["#DesarrolloWeb", "#SoftwareAMedida", "#Pymes", "#TransformaciónDigital"],
        vis="Three device mockups side by side: a website, an online store and a business dashboard",
        comp="lista de 3 beneficios",
    ),
]
