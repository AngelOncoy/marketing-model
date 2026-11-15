"""Report context for synthetic data. All names are fictitious."""

CLIENTS_BY_SECTOR = {
    "agroindustria": ["Agroexportadora Valle Norte SAC", "Frutos del Chicama SAC", "Cooperativa Agraria Virú",
                      "Fundo Las Palmeras de Chao SAC"],
    "cuero y calzado": ["Calzados Liberteños EIRL", "Curtiembre El Porvenir SAC", "Lanera Andina SAC"],
    "educación": ["Colegio San Martín de Porres", "Instituto Técnico Moche", "Colegio Los Algarrobos"],
    "logística y transporte": ["Transportes Huanchaco SRL", "Logística Pacasmayo SAC",
                               "Distribuidora La Esperanza SRL"],
    "minería": ["Minera Cerro Alto SA", "Minera Andes del Norte SA"],
}
CLIENTS = [c for pool in CLIENTS_BY_SECTOR.values() for c in pool]

# Sector implied by the text of non-publishable tasks that mention a client.
NONPUB_SECTOR = {
    "ns08": "agroindustria", "nh04": "logística y transporte", "nh11": "minería",
    "nh16": "logística y transporte", "nn08": "agroindustria", "ni05": "agroindustria",
    "nn02": "cuero y calzado",
}

PERSONS = [
    "Lucía Paredes", "Jorge Valverde", "Milagros Rojas", "Diego Castañeda", "Rosa Benites",
    "Kevin Alvarado", "Andrea Zavaleta", "Luis Gamboa", "Carla Mendoza", "Renzo Ibáñez",
]

# Main project of the report: internal projects per area, client projects per area and sector.
INTERNAL_PROJECTS = {
    "software": "corall-app, ERP (interno)",
    "hardware": "Laboratorio de hardware (interno)",
    "ia": "Laboratorio de IA (interno)",
    "innovacion": "Programa de innovación (interno)",
}
ERP_ASSISTANT_PROJECT = "Asistente del ERP (interno)"
AREA_LINE = {
    "software": "Software a medida",
    "hardware": "Hardware e IoT",
    "ia": "Soluciones de IA",
    "innovacion": "Innovación y transformación digital",
}


def client_project(area: str, sector: str) -> str:
    return f"{AREA_LINE[area]} para {sector} (cliente)"

PENDIENTES = [
    "Revisar con {persona} los criterios de aceptación del siguiente módulo.",
    "Documentar el procedimiento de despliegue.",
    "Preparar la demo de avance para {cliente}.",
    "Actualizar dependencias del proyecto.",
    "Completar pruebas unitarias del servicio de reportes.",
    "Ordenar el tablero del sprint.",
    "Coordinar visita técnica con {cliente}.",
    "Revisar consumo de la cuenta de nube.",
    "Escribir el manual de usuario del módulo entregado.",
    "Definir la estructura del informe mensual.",
    "Pedir a {persona} las fotos de la última visita.",
    "Afinar los umbrales de alerta del tablero.",
    "Migrar los scripts de prueba al nuevo repositorio.",
    "Agendar capacitación interna sobre buenas prácticas de Git.",
    "Cotizar componentes para el próximo lote de prototipos.",
]

BLOQUEOS = [
    "Seguimos esperando que {cliente} confirme el acceso a su servidor.",
    "La revisión de la app en Meta sigue pendiente; no podemos activar la plantilla de mensajes.",
    "El proveedor de componentes retrasó la entrega dos semanas.",
    "Riesgo: el certificado del dominio vence pronto y nadie tiene el acceso del registrador.",
    "{cliente} cambió los requisitos a mitad del sprint; hay que replanificar.",
    "La cuota del proveedor de IA se agotó a media tarde.",
    "Falta la firma del consentimiento para usar fotos de la visita.",
    "El equipo de pruebas del cliente no responde desde hace tres días.",
]

DISCARD_PHRASES = {
    "seguridad": "el trabajo de seguridad expondría detalles internos",
    "progreso": "hay tareas aún en progreso o en revisión",
    "bug": "las correcciones de errores no aportan al público y revelarían fallas",
    "refactor": "los cambios internos de código no son visibles para el cliente",
    "gestion": "las reuniones y tareas de gestión no son publicables",
    "consentimiento": "el trabajo con el cliente no tiene autorización para difundirse",
    "datos_personales": "la tarea involucra datos personales",
    "infra": "la configuración de infraestructura es información interna",
    "menor": "los ajustes menores no tienen valor suficiente para una publicación",
}

IN_PROGRESS_REASON = (
    "La tarea aún no está terminada; publicarla anticiparía algo que puede cambiar antes de su entrega."
)
