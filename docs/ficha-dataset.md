# Ficha del dataset sintético (v0.2)

Estado: **completo para entrenamiento**, con 500 ejemplos.
- Archivo: `data/synthetic/synthetic_v0.2.jsonl` (2,6 MB).
- Estadísticas exactas: `data/synthetic/synthetic_v0.2.ficha.json`.
- La v0.1 (250 filas) queda en el historial de git.

## Qué contiene

Cada fila es un par instruction/response:

| Campo | Contenido |
|---|---|
| `instruction` | Tarea fija: evaluar el reporte, decidir y devolver la propuesta en JSON sin información interna |
| `input` | Kit corto de marca (leído de `brand/brand.json`) + reporte diario sintético en el formato real de CorAll (Matriz, Anexado, Pendientes, Bloqueos) |
| `output` | JSON validado con `src/marketing_model/schema.py`. Contiene la decisión y las ideas evaluadas. Si se publica, añade el copy para LinkedIn, Facebook e Instagram, los hashtags, el guion de TikTok y el brief de la pieza |
| `group_id`, `split` | Grupo del reporte de origen y split asignado por hash del grupo |
| `meta` | Área, pilar, tipo de proyecto y tipo de fila. Sirve para las métricas de sesgo y no se usa al entrenar |

## Cómo se generó

1. **Banco de tareas escrito por un LLM (Claude) y revisable por el equipo** (`src/marketing_model/generate/bank/`).
   - 185 tareas publicables, cada una con su copy de referencia:
     - v0.1: 125 tareas;
     - v0.2: 60 tareas nuevas, 15 por área (`cards_set2_a.py`, `cards_set2_b.py`).
   - 96 tareas no publicables (distractores), en 9 categorías:
     - categorías: seguridad, trabajo en progreso, bugs, refactor, gestión, sin consentimiento, datos personales, infraestructura y ajustes menores;
     - v0.1 tenía 64 distractores; los 32 nuevos de la v0.2 van sobre todo a IA, innovación y hardware, que tenían menos.
   - Versiones "a medias" de 49 tareas (`bank/wip.py`), para cuando aparecen sin terminar.
2. **Ensamblado por script** (`build_synthetic.py`, semilla 42).
   - **Composición del reporte.** Cada reporte combina 0-3 distractores con una tarea publicable, o lleva solo distractores.
   - **Cebo de fugas.** El script agrega números de issue/PR, horas, rutas y nombres ficticios.
     - El 60 % de los reportes trae los nombres como marcadores del anonimizador (`[CLIENTE_1]`).
     - El 40 % trae nombres ficticios "que se escaparon", para que el modelo aprenda a no copiarlos aunque falle el anonimizador.
   - **Estilo del brief.** Fondo, footer, logo, composición, formato y ratio se sortean dentro de las reglas de marca.
   - **Tareas repetidas.** Las tareas publicables se usan en vueltas completas, así que ninguna se publica más de 2 veces.

   Reglas de coherencia del ensamblado:
   - **Cliente según el sector.** Un cliente ficticio sale del sector de la tarea: una estación de
     clima nunca está "en el fundo" de una fábrica de calzado.
   - **Proyecto según la tarea.** El proyecto principal sale de la tarea: "Hardware e IoT para
     agroindustria (cliente)", o el proyecto interno del área.
   - **Visual según la imagen.** El visual del brief se deriva de la descripción de la imagen, así
     que no contradice el prompt.
   - **Composiciones con contenido.** "Antes / después", "línea de tiempo" y "cita" solo aparecen si
     la tarea tiene ese contenido.
   - **Tareas sin terminar.** Una tarea publicable que aparece "En progreso" o "En revisión" usa su
     texto a medias, para que el estado y el detalle no se contradigan.
   - **Descartes por área.** Los descartes se reparten por área en proporción a las publicaciones,
     para que la tasa de publicación sea la misma en todas (D1).
3. **Validación y limpieza** (`check_dataset.py`).
   - **Esquema:** Pydantic.
   - **Fugas:** issues, rutas, marcadores, correos, teléfonos, identificadores de código, y nombres de clientes y personas.
   - **Cifras:** toda cifra de dos o más dígitos debe aparecer en el reporte.
   - **Redacción:** exageraciones y términos prohibidos.
   - **Formato:**
     - hashtags por red;
     - longitud del título, de los bullets y del gancho;
     - la cláusula "No text, no letters, no logos" en el prompt de imagen.
   - **Duplicados:** se quitan los exactos y los casi duplicados (Jaccard de 5-gramas >= 0,9 entre grupos distintos).

Comando reproducible:

```bash
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.build_synthetic --n 500 --seed 42
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.2.raw.jsonl
```

## Filas eliminadas por motivo

| Motivo | Filas |
|---|---|
| Vacías | 0 |
| Esquema inválido | 0 |
| Fuga de información | 0 |
| Validador de copy | 0 |
| Duplicado exacto o casi duplicado | 0 |

La versión final no elimina filas, porque los errores se corrigieron en el banco y no en las filas.

**Lo que corrigieron los validadores durante la construcción:**
- **v0.1:**
  - 3 casos de "la mejor" (exageración);
  - 1 cifra sin respaldo ("4.0");
  - 3 bullets de más de 4 palabras;
  - 1 título de más de 6 palabras;
  - 1 falso positivo propio: el color `#0E0B09` se leía como issue `#0`, y se corrigió la expresión regular.
- **v0.2:** 2 filas con el texto de Instagram por debajo del mínimo del esquema.

**Lo que encontraron las revisiones manuales y los scripts de coherencia** (ningún validador mira esto):
- clientes de otro sector;
- un proyecto principal ajeno a la tarea;
- un visual del brief que contradecía el prompt de imagen;
- tareas "En revisión" cuyo texto decía que ya se habían entregado;
- 9 eventos de la v0.1 con el día de la semana desfasado un día respecto al calendario de 2026, corregidos moviendo la fecha.

Todo se corrigió en el script o en el banco, y luego se regeneró el dataset.

## Distribución (500 filas)

| Corte | Valores |
|---|---|
| Decisión | publicar 360 (72 %), descartar 140 (28 %) |
| Descartes | 96 solo con distractores, 44 con una tarea publicable aún "En progreso" o "En revisión" |
| Área | hardware 126, IA 125, innovación 125, software 124 |
| Pilar (publicadas) | producto 135, educativo 75, servicio en territorio 50, hito 48, evento 37, cultura 34, catálogo 25 |
| Tipo de proyecto | interno 232, cliente 172 (los descartes sin tarea publicable no tienen tipo) |
| Split | train 436, val 64 (281 grupos; todas las variantes de un grupo van al mismo split) |
| Tamaño medio | entrada 1770 caracteres, salida 2471 caracteres |
| Brief | 274 imagen única y 86 carruseles; 313 combinaciones de estilo distintas en 360 propuestas |

**Sesgo D1, tasa de publicación por área:**

| | Hardware | IA | Innovación | Software | Diferencia máxima |
|---|---|---|---|---|---|
| Antes (v0.1) | 0,67 | 0,71 | 0,72 | 0,79 | 12 puntos |
| Ahora (v0.2) | 0,722 | 0,720 | 0,720 | 0,718 | 0,4 puntos |

Ahora el reparto se fija por construcción y no por azar.

El test no sale de aquí: serán los ~21 reportes reales anonimizados.

## Limitaciones (para el informe)

- **Un mismo autor para entradas y salidas.** El LLM que escribió el banco escribió también los
  reportes y las propuestas. El modelo puede aprender ese estilo y no el de los reportes reales.
  Por eso el test es con reportes reales.
- **Variedad limitada.** 185 tareas publicables generan 360 propuestas, así que cada tarea aparece
  hasta 2 veces publicada. Un mismo grupo junta hasta 5 filas (versiones publicadas y sin
  terminar), con distinto contexto y distinto brief, siempre en el mismo split.
- **El visual sale de una sola descripción por tarea.** Gana coherencia, pero 155 de las 360
  propuestas quedan como "fotografía realista de la escena".
- **Una sola marca.** El kit de marca es siempre el de CorAll (decisión del proyecto).
- **Copy de referencia sin revisión de Marketing.** Falta que Marketing revise una muestra del
  banco y se ajuste el tono según lo que diga.
- **Las tareas de seguridad convertidas en consejo** (por ejemplo, "3 claves para integraciones
  seguras") son un criterio editorial propuesto, no una regla firmada por CorAll.
- **Equidad solo por área.** La tasa de publicación está igualada por área. No se midió por sector
  ni por tipo de proyecto (interno o cliente); queda para la Matriz EICE.
