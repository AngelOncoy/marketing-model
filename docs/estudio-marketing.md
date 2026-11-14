# Estudio de marketing para CorAll

Base de diseño del proyecto: qué se publica, cómo se escribe y cómo se diseña. Las decisiones
técnicas (modelo, dataset, evaluación) deben trazarse a este documento.

> Fuentes: análisis de 8 piezas reales/generadas de CorAll aportadas por el equipo, más guías de
> terceros sobre formatos (no oficiales; verificar con la ayuda de cada plataforma antes de fijar
> reglas). Colores y tipografías oficiales: ver sección 8.2 (manual de marca).

## 1. Cómo se trabaja hoy

Flujo actual: reporte diario (redactado con Claude a partir del trabajo del día) → módulo
"Propuestas IA" del ERP (corall-app, ver sección 8.1) → texto para las redes + "Imagen sugerida"
(un prompt) → ChatGPT o Gemini con los logos adjuntos → imagen.

Conclusión clave: **la infografía final la produce un modelo de imagen externo a partir de un prompt**.
Lo que nuestro modelo debe generar es el contenido de texto: copy, hashtags y un *brief de diseño*
(incluido el prompt). Actualización 14/11: la infografía final sí entra en el alcance, con una arquitectura híbrida
(ver `docs/plan.md`); la variedad viene del brief, no de una plantilla fija.

Problemas del flujo actual:

| Problema | Evidencia | Consecuencia para el modelo |
|---|---|---|
| Fuga de información técnica | El copy de seguridad nombra una ruta interna de la API y sugiere que hubo una falla | Filtro de confidencialidad obligatorio (sección 3) |
| Afirmaciones no verificables | "Tus datos, siempre seguros" | Solo claims respaldados por el reporte |
| Look "hecho por IA" y repetitivo | Mismo footer rojo, mismo esquema en las pruebas | Variación controlada de estilo (sección 5) |
| Se queda corto frente a las piezas reales | Piezas de la empresa usan fotos, formas y layouts variados | Brief más rico y variado |

## 2. Piezas reales de CorAll: pilares de contenido

| Pilar | Ejemplo | Rasgos visuales |
|---|---|---|
| Producto | Sensor de Pulpa de Fruta | Fondo claro, título negro + palabra en rojo, render/foto realista, 3 íconos al pie, footer oscuro "Desarrollado por CorAll" |
| Catálogo / portafolio | Telemetría IoT | Lista de 3 beneficios con íconos rosa, grilla de productos, franja de sectores, CTA rojo, footer negro con 3 íconos, ola roja |
| Evento | Taller de Difusión ERP | Fondo blanco, formas geométricas rojo/negro, retrato en círculo con borde rojo, fecha/hora/lugar con íconos, botón de registro, logos de cofinanciadores al pie |
| Fecha especial / cultura | Día del Ingeniero | Foto del equipo con overlay rojo, tipografía script + negrita, caja blanca con borde, footer blanco con logo |
| Servicio en territorio | Diagnóstico Madurez Digital | Carrusel de fotos reales, etiqueta roja superior, logo del cliente, footer rojo con logo |
| Educativo / buenas prácticas | Seguridad de datos | Gris claro, ola roja, 3 beneficios, ilustración 3D, botón CTA, banda roja inferior |

Constantes de marca observadas: logo CorAll con isotipo de coral (versiones negra, blanca e
isotipo solo), rojo burdeos/carmesí + negro + blanco + gris claro, tipografía sans geométrica en
negrita para títulos (parece Poppins; confirmar) y serif solo en el logo, iconos de línea en
círculo rosa suave. Eslóganes en uso: "Innovación que transforma", "Innovación que genera valor",
"Soluciones tecnológicas a medida", "Tecnología aplicada a la agroindustria".

Variación observada (lo que el modelo debe reproducir): footer rojo / negro / blanco / mixto,
fondo gris claro / blanco / foto con overlay, logo arriba-izquierda / centrado abajo / junto al
título, visual 3D / foto real / formas geométricas / mockup de interfaz.

## 3. Qué reportes y qué ideas son publicables

El modelo primero **decide**; descartar es un resultado válido.

Candidatos a publicar:
- Funcionalidad o mejora **terminada y desplegada** y visible para el cliente final.
- Resultado medible respaldado por el reporte (pruebas, tiempos, cantidades reales).
- Hitos de proyecto, eventos, servicios en territorio, fechas relevantes.
- Lecciones técnicas generales, redactadas como buena práctica y sin referirse a un incidente propio.

Nunca publicar (dataset debe incluir estos casos como negativos):
- Vulnerabilidades sin desplegar o parchadas recientemente, rutas, endpoints, nombres de tablas,
  números de issue/PR, variables, credenciales, claves.
- Bloqueos o conflictos con terceros (p. ej. Meta, cliente), riesgos, deuda técnica, horas.
- Trabajo en estado "En progreso" o "En revisión".
- Nombres de clientes, personas o logos sin autorización registrada (p. ej. caso con consentimiento
  pendiente), teléfonos, correos, datos personales.
- Promesas absolutas ("100% seguro", "garantizamos") que el reporte no sostiene.

Cuando un tema sensible tiene valor educativo (seguridad), se transforma en consejo general
("3 claves para que cada cliente solo vea sus pedidos") sin contar qué falló ni cómo se llama la ruta.

## 4. Cómo escribir la descripción (copy)

Estructura recomendada:
1. **Gancho** en la primera línea: LinkedIn muestra solo la primera línea o dos antes de "ver más"
   (Instagram, unos ~125 caracteres). Debe aportar valor por sí sola: pregunta del cliente, dato
   concreto o promesa específica.
2. **Problema o contexto** del cliente en una frase.
3. **Qué hicimos**, traducido de lenguaje técnico a beneficio.
4. **Prueba**: un dato verificable del reporte (sin inventar cifras).
5. **CTA suave** ("Conoce más", "Cuéntanos tu caso"). Un CTA duro es agresivo en un primer contacto.
6. **Hashtags**: marca (#CorAll), sector y tema. No hay fuente fiable sobre cantidad; fijar como
   convención 3-5 en LinkedIn y 5-8 en Instagram y medirlo.

Marcos por pilar: PAS (problema-agitación-solución) para educativo y seguridad; AIDA para
producto y evento; antes-después-puente para servicios y casos; historia-lección para cultura y equipo.

Traducción técnico → beneficio (ejemplos para el dataset):

| Reporte dice | Copy dice |
|---|---|
| Validación de propietario del pedido en el servidor | Cada cliente solo ve sus propios pedidos |
| Pedido en 4 pasos sin pago en línea | Comprar es más simple: eliges, personalizas y cierras por WhatsApp |
| Migración con TRIM en ubicaciones | (No publicable: detalle interno) |
| Plan por hitos y épicas | (No publicable salvo como lección de gestión) |

Reglas de estilo: español peruano profesional y cercano; una idea por publicación; verbos en
primera persona plural ("desarrollamos", "implementamos"); sin jerga interna; sin emojis en exceso
(un emoji de apertura como en las piezas reales es aceptable).

## 5. Diseño de la pieza: el brief

El modelo emite un brief de diseño estructurado. Los campos varían entre propuestas para evitar el
look repetitivo; las constantes de marca no varían.

Constantes: paleta rojo/negro/blanco/gris, logo CorAll (negro, blanco o isotipo según fondo),
eslogan de la lista, iconos de línea, ningún otro logo (salvo cofinanciadores o clientes con
autorización), nunca generar rostros de personas reales.

Ejes de variación: formato, ratio, fondo (gris con ola / blanco con formas / foto con overlay /
negro), footer (rojo / negro / blanco / mixto / con íconos), posición del logo, tipo de visual
(render 3D, foto real aportada, formas geométricas, mockup de interfaz, ilustración de iconos),
composición (lista de 3 beneficios, grilla, dato destacado, línea de tiempo, antes/después, cita),
tipo de CTA.

Texto dentro de la imagen: los modelos de imagen fallan con textos largos. Título <= 6 palabras,
bullets <= 4 palabras, cadenas exactas entre comillas en el prompt (como en los prompts actuales).

Formatos (guías de terceros; verificar):

| Uso | Medida |
|---|---|
| LinkedIn imagen única horizontal | 1.91:1, 1200 x 627 |
| LinkedIn / Instagram vertical (más espacio en el feed) | 4:5, 1080 x 1350 |
| Cuadrado | 1:1, 1080 x 1080 |
| Carrusel | Todas las diapositivas con la misma proporción, 4:5 o 1:1; en LinkedIn se sube como PDF |
| Historias | 9:16, 1080 x 1920 |

Carrusel: 6-10 diapositivas (las guías discrepan; validar con pruebas A/B). Diapositiva 1 = gancho,
una idea por diapositiva, penúltima = prueba, última = CTA suave. El motion graphics queda **fuera
de alcance**; el campo de formato puede reservarse pero el modelo no lo genera.

## 6. Esquema de salida propuesto

```json
{
  "decision": "publicar | descartar",
  "motivo_descarte": null,
  "ideas_evaluadas": [{"fuente": "tarea del reporte", "pilar": "producto", "valor": 1, "riesgo": 1, "razon": "..."}],
  "propuesta": {
    "plataforma": "linkedin | facebook | instagram",
    "pilar": "...",
    "copy": "...",
    "hashtags": ["#CorAll"],
    "pieza": {
      "formato": "imagen_unica | carrusel",
      "ratio": "4:5", "resolucion": "1080x1350",
      "estilo": {"fondo": "", "footer": "", "logo": "", "visual": "", "composicion": "", "cta": ""},
      "diapositivas": [{"titulo": "", "texto": "", "visual": ""}],
      "prompt_imagen": "..."
    }
  }
}
```

## 7. Cómo medir (insumo para la métrica del curso)

- **Fuga confidencial**: 0 casos sobre el test (rutas, issues, clientes, riesgos).
- **Decisión correcta**: exactitud en publicar/descartar sobre casos positivos y negativos.
- **Calidad del copy**: rúbrica 1-5 (gancho, claridad, claim verificable, tono, CTA) con evaluación humana ciega.
- **Validez del brief**: % de JSON válido y de campos completos.
- **Diversidad de diseño**: variedad de combinaciones de estilo entre propuestas (que no sean todas iguales).
- **Líneas base**: (1) el modelo base sin ajustar; (2) el agente actual con DeepSeek, que es la solución existente de la empresa.

## 8. Hallazgos de la segunda revisión (reportes, manual de marca y sitio web)

### 8.1 El sistema actual ya existe: "Propuestas IA" (corall-app)

Según los reportes del 27/10 al 12/11:
- Un procedimiento almacenado lista las entradas de los reportes del equipo (hasta 31 días) **sin
  datos de la persona ni referencias de GitHub**, porque ese texto se envía a un proveedor de IA externo.
- Un servicio pide propuestas en JSON a 4 proveedores configurables: Claude, Groq (gpt-oss-120b),
  DeepSeek y uno simulado.
- Enfoque "inspirado, no anuncio": la IA deduce si el proyecto es interno o de cliente; marca la
  propuesta "lista para aprobar" y reserva "en reserva" lo que identifica al cliente o es sensible.
- Tipos de pieza: campo (foto real con plantilla de marca), infografía, carrusel (un prompt por
  lámina), video (guion de tomas, canal TikTok) e imagen simple. Proporción según la red (4:5,
  1.91:1, 1:1), textos exactos entre comillas y lista de archivos de marca a adjuntar.
- Validaciones por código: cada cifra debe estar en la entrada que cita, números sin declarar, frases
  de anuncio o exageración, hashtags según la red, cláusula "no text, no logos" en el prompt de imagen.
- Bandeja de revisión: Borrador / Aprobada / Rechazada (con motivo obligatorio), edición en línea y
  paso a la Parrilla de contenido. Estado a 12/11: en revisión; Marketing aún debe elegir generador y
  aprobar ejemplos.

Implicaciones para el proyecto:
1. **Línea base natural**: este sistema (prompting de un modelo grande) y el modelo base sin ajustar.
2. **Los validadores son métricas listas** y filtros de calidad para el dataset sintético.
3. **La bandeja aún no sirve como dataset**: casi todas las propuestas guardadas son pruebas
   (confirmado por el equipo). Se descarta como fuente de entrenamiento por ahora; a futuro, las
   aprobaciones, rechazos con motivo y ediciones reales serían datos etiquetados valiosos.
4. **Hay que justificar el valor de un modelo propio frente a uno de 120B con prompt**. Un modelo
   pequeño ajustado en Colab T4 probablemente no gane en calidad bruta. Las tesis defendibles son:
   privacidad (los reportes no salen a un proveedor externo; Ley 29733), costo y límites de cuota
   (Groq limita tokens por minuto; DeepSeek depende de saldo), formato y marca consistentes sin un
   prompt enorme. Decidir cuál es la tesis antes de elegir la estrategia.

### 8.2 Marca oficial (Manual de Marca 2025)

- Paleta: rojo `#BF1820`, marrón oscuro `#534437` (Judge Gray), negro `#0E0B09`, blanco `#FFFFFF`.
  **Decisión**: `#BF1820` es el rojo de branding para todas las piezas. `#A31924` se usa
  **solo** en el isotipo y nunca como color de fondo, texto o elementos.
- Tipografías: Artegra Soft Condensed (marca), Zapf Calligraphic 801 (acento humano/creativo) y
  Poppins (textos). Las piezas observadas usan sans geométrica en negrita, coherente con Poppins.
- Patrón: circuito continuo / eslabón de cadena.
- Logo: versiones horizontal, vertical, monocromo y escala de grises; zona de protección igual a la
  altura de la "C"; prohibido cambiar color, tipografía o forma, inclinarlo o ponerle bordes; sobre
  fondo sólido o foto que garantice legibilidad; reglas de co-branding con partners.
- Archivos de marca: isotipo, logo negro `#0E0B09`, logo blanco y logo Judge Gray.
- El marrón `#534437` casi no aparece en las piezas observadas: opcional como acento cálido.

### 8.3 Sitio web (coralldar.com)

CorAll D&R (Trujillo) diseña, fabrica e integra el sistema completo: dispositivo que captura el
dato, modelo que lo interpreta y plataforma donde se decide. Cuatro áreas: Innovación, Software,
Inteligencia artificial y Hardware. Sectores: logística y transporte, educación, agroindustria,
minería, cuero y calzado. Casos publicados: monitoreo de flotas, telemetría para vehículos pesados,
Industria 4.0 en una línea de procesamiento de lana. Tono: directo, técnico, orientado a resultados,
con "tú" en los llamados a la acción y énfasis en el piloto en campo antes de escalar.

Notas: la web no menciona un ERP ni marketing automatizado, pero las piezas reales sí hablan del ERP.
El manual de marca habla de mypes como público, mientras la web muestra clientes corporativos:
definir el público objetivo de cada pieza.

### 8.4 Plataformas objetivo

| Plataforma | Rol | Pieza y copy |
|---|---|---|
| LinkedIn | Principal (B2B) | 1.91:1 o 4:5; carrusel en PDF; gancho en la primera línea; tono profesional con "tú" |
| Instagram | Principal (visual) | 4:5 o carrusel; caption corto; más hashtags |
| TikTok | Principal (video) | 9:16; guion por tomas con gancho en los primeros segundos. El modelo entrega guion y prompt, no renderiza video |
| Facebook | Derivada | Variante de la propuesta de LinkedIn con copy más corto y CTA directo; no genera pieza propia |

Recomendación propia: LinkedIn y Facebook comparten público y piezas en la práctica, así que se
genera una propuesta base y una variante de copy, no dos propuestas. Validar con Marketing.
Las medidas de TikTok y la duración ideal del video no están verificadas.

### 8.5 Imagen adjunta opcional

El brief incluye `imagen_adjunta`: ninguna / hardware / campo / equipo.
- Con imagen: el prompt la referencia como archivo adjunto y dice cuál es su rol.
- Sin imagen: el prompt describe entre paréntesis qué foto conseguir (como ya hace el sistema actual).
- Hardware real: preferir la foto del producto. Si se genera una ilustración, marcarla como
  "ilustrativa" y no afirmar especificaciones.
- Personas: nunca generar rostros reconocibles; las fotos de campo se usan solo con consentimiento.

### 8.6 Los reportes disponibles

Más de 20 reportes (12/10 al 12/11). Proyectos: corall-app (ERP interno: RR. HH., CRM, Propuestas IA),
una tienda en línea (cliente), una landing para un exportador (cliente) y una integración de
mensajería para un gremio empresarial (cliente). Estructura constante: Matriz (código) con Módulo/Repo, Issue, PR, Estado, Horas y
Detalle; Anexado (gestión, soporte, reuniones, campo); Pendientes; Bloqueos/Riesgos. El Markdown y
el PDF tienen el mismo contenido, así que se usa Markdown.

Datos que hay que anonimizar antes de usar un reporte: nombres de clientes y de personas
(incluido el autor), teléfonos, correos, credenciales mencionadas y cualquier ruta o número de issue/PR.

## 9. Pendientes

- Fijar la justificación de negocio del modelo propio frente al sistema actual (propuesta:
  privacidad + costo; ver CLAUDE.md).
- Confirmar con Marketing el tratamiento de Facebook y las especificaciones de TikTok.
- Reglas de confidencialidad firmadas por la empresa (qué nunca se publica).

## Fuentes (terceros, no oficiales)

- https://contentin.io/blog/linkedin-post-specs/
- https://www.krumzi.com/blog/linkedin-carousel-size
- https://www.oktopost.com/blog/linkedin-carousel-pdf-best-practices/
- https://www.linearity.io/blog/instagram-size-guide/
- https://alphavant.com/blog/linkedin-carousel-lead-generation
