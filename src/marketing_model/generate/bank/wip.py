"""Unfinished versions of publishable tasks, used when a report shows them "En progreso" or "En revisión".

The text must describe work that is not done yet, so the state and the detail agree. Only the cards
listed here can appear as unfinished; the rest always appear finished.
"""

WIP_DET = {
    "hw01": "Calibración del sensor de pulpa para la línea de mango de {cliente}: ya reconoce 2 de los 3 rangos de madurez; falta ajustar el tercero y hacer la prueba en planta contra el laboratorio.",
    "hw02": "Tablero de telemetría para la flota de {cliente}: 9 unidades ya reportan posición; faltan la temperatura del motor y las alertas de velocidad.",
    "hw04": "Contador de pares para la línea de aparado de {cliente}: lector óptico montado en la faja; falta la pantalla del supervisor y el turno de prueba.",
    "hw06": "Estación de clima para el fundo de {cliente}: armada y probada en el laboratorio; falta instalarla en campo y medir el alcance LoRa hasta el gateway.",
    "hw09": "Red LoRa del fundo de {cliente}: 1 de 3 gateways instalado; falta cubrir el resto de sectores y conectar los sensores de suelo.",
    "hw13": "Detector portátil de gases para {cliente}: primer lote armado; faltan las pruebas de umbral con gas patrón antes de entregar.",
    "hw16": "Balanza conectada para centros de acopio: el pesaje y el envío por wifi funcionan; falta asociar cada pesada al productor con el QR.",
    "hw21": "Botón de pánico para cabina: el envío de ubicación funciona con datos móviles; falta el respaldo por SMS y las pruebas de activación.",
    "hw23": "Sensores ultrasónicos de nivel para los tanques de {cliente}: 2 de 6 instalados; falta configurar el aviso de nivel bajo.",
    "sw01": "Flujo de pedido para la tienda de {cliente}: listos los pasos de elegir y personalizar; faltan la revisión del pedido y el envío por WhatsApp.",
    "sw02": "Módulo de solicitudes de vacaciones del ERP: la solicitud desde el celular ya funciona; falta la aprobación del jefe y el cálculo automático del saldo.",
    "sw04": "Tablero de tickets de soporte: estados por color listos; falta medir el tiempo de primera respuesta y el filtro por cliente.",
    "sw08": "Seguimiento de pedidos en el portal de {cliente}: se muestran las etapas de corte y aparado; faltan armado y despacho.",
    "sw10": "Reportes descargables para el portal de {cliente}: el PDF de ventas por día ya sale; faltan Excel y los reportes por producto y vendedor.",
    "sw15": "App de despachos para {cliente}: registro con foto listo; faltan la firma y el modo sin conexión.",
    "sw21": "App de registro de cosecha para {cliente}: el registro de jabas por lote funciona en pruebas; falta el tablero del ingeniero y probarla con las cuadrillas.",
    "ia01": "Modelo de conteo de fruta por cámara para la línea de {cliente}: entrenado con el primer lote; falta validar con más lotes y medir el error.",
    "ia02": "Asistente de búsqueda en el ERP: entiende preguntas sobre tickets; falta conectar pedidos y propuestas y armar las consultas de prueba.",
    "ia03": "Inspección visual de costuras en la línea de {cliente}: el modelo marca algunas costuras irregulares; falta compararlo con el supervisor en una muestra grande.",
    "ia04": "Lector de guías de remisión para {cliente}: ya extrae la fecha; falta extraer RUC y productos y probar con guías reales.",
    "ia06": "Modelo de recomendación de riego para {cliente}: combina la humedad de suelo; falta integrar el pronóstico de clima y arrancar el piloto.",
    "ia10": "Clasificador automático de tickets en el ERP: sugiere categoría; falta la prioridad y la prueba con los tickets históricos.",
    "ia13": "Predicción de demanda semanal para el almacén de {cliente}: datos de ventas limpios; falta entrenar y validar con el último trimestre.",
    "ia16": "Clasificador de calibre de mango por imagen: separa los calibres extremos; falta distinguir los intermedios y comparar con la balanza.",
    "ia19": "Optimizador de rutas de reparto para {cliente}: ordena paradas sin ventanas de horario; falta agregarlas y probar en reparto real.",
    "ia24": "Detector de casco y chaleco para el ingreso a planta de {cliente}: detecta el casco; falta el chaleco y la alerta al supervisor.",
    "in02": "Proyecto Industria 4.0 en la línea de lana de {cliente}: 2 de 4 puntos de medición instalados; falta el tablero de producción por turno.",
    "in14": "Prototipo de trazabilidad por lote con QR: el productor ya registra la cosecha; falta la vista del comprador al escanear el QR.",
    "mx24": "Tablero del productor: muestra los kilos entregados; faltan la calidad por lote y los pagos pendientes.",
    "mx25": "Asistente de estado de pedidos por WhatsApp para {cliente}: responde con el estado; falta la hora estimada de llegada y la derivación a una persona.",
}
