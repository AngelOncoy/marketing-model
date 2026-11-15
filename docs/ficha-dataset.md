# Ficha del dataset sintético (v0.1)

Estado: **primera mitad** (250 de los 500 ejemplos planeados). Archivo: `data/synthetic/synthetic_v0.1.jsonl`
(1,3 MB). Estadísticas exactas: `data/synthetic/synthetic_v0.1.ficha.json`.

## Qué contiene

Cada fila es un par instruction/response:

| Campo | Contenido |
|---|---|
| `instruction` | Tarea fija: evaluar el reporte, decidir y devolver la propuesta en JSON sin información interna |
| `input` | Kit corto de marca (leído de `brand/brand.json`) + reporte diario sintético en el formato real de CorAll (Matriz, Anexado, Pendientes, Bloqueos) |
| `output` | JSON validado con `src/marketing_model/schema.py`: decisión, ideas evaluadas y, si se publica, copy para LinkedIn, Facebook e Instagram, hashtags, guion de TikTok y brief de la pieza |
| `group_id`, `split` | Grupo del reporte de origen y split asignado por hash del grupo |
| `meta` | Área, pilar, tipo de proyecto y tipo de fila (para métricas de sesgo; no se usa al entrenar) |

## Cómo se generó

1. **Banco escrito a mano por un LLM (Claude) y revisable por el equipo** (`src/marketing_model/generate/bank/`):
   125 tareas publicables con su copy de referencia y 64 tareas no publicables (distractores) en 9
   categorías: seguridad, trabajo en progreso, bugs, refactor, gestión, sin consentimiento, datos
   personales, infraestructura y ajustes menores.
2. **Ensamblado por script** (`build_synthetic.py`, semilla 42): cada reporte combina 0-3
   distractores con una tarea publicable, o solo distractores. Agrega números de issue/PR, horas,
   rutas y nombres ficticios como cebo de fugas. Los nombres aparecen como marcadores del
   anonimizador (`[CLIENTE_1]`) en el 60 % de los reportes y como nombres ficticios "que se
   escaparon" en el 40 % restante, para que el modelo aprenda a no copiarlos aunque falle el
   anonimizador. El estilo del brief (fondo, footer, logo, composición, formato, ratio) se sortea
   dentro de las reglas de marca.

   Reglas de coherencia del ensamblado:
   - **Cliente según el sector.** Un cliente ficticio sale del sector de la tarea: una estación de
     clima nunca está "en el fundo" de una fábrica de calzado.
   - **Proyecto según la tarea.** El proyecto principal sale de la tarea: "Hardware e IoT para
     agroindustria (cliente)", o el proyecto interno del área.
   - **Visual según la imagen.** El visual del brief se deriva de la descripción de la imagen, así
     que no contradice el prompt.
   - **Composiciones con contenido.** "Antes / después", "línea de tiempo" y "cita" solo aparecen si
     la tarea tiene ese contenido.
   - **Tareas sin terminar.** Una tarea publicable que aparece "En progreso" o "En revisión" usa un
     texto a medias (`bank/wip.py`, 30 tareas), para que el estado y el detalle no se contradigan.
3. **Validación y limpieza** (`check_dataset.py`): esquema Pydantic, fugas (issues, rutas,
   marcadores, correos, teléfonos, identificadores de código, nombres de clientes y personas),
   cifras de dos o más dígitos que no estén en el reporte, exageraciones, términos prohibidos,
   hashtags por red, longitud del título y los bullets en la imagen, longitud del gancho y la
   cláusula "No text, no letters, no logos" en el prompt de imagen. Luego quita duplicados exactos
   y casi duplicados (Jaccard de 5-gramas >= 0,9 entre grupos distintos).

Comando reproducible:

```bash
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.build_synthetic --n 250 --seed 42
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.1.raw.jsonl
```

## Filas eliminadas por motivo

| Motivo | Filas |
|---|---|
| Vacías | 0 |
| Esquema inválido | 0 |
| Fuga de información | 0 |
| Validador de copy | 0 |
| Duplicado exacto o casi duplicado | 0 |

La versión final no elimina filas porque los errores se corrigieron en el banco, no en las filas.
Durante la construcción, los validadores detectaron y obligaron a corregir: 3 casos de "la mejor"
(exageración), 1 cifra sin respaldo ("4.0"), 3 bullets de más de 4 palabras y 1 título de más de 6
palabras. También detectaron un falso positivo propio (el color `#0E0B09` se leía como issue `#0`),
que se corrigió en la expresión regular.

Una revisión manual de una muestra encontró 4 incoherencias que los validadores no miran:
- cliente de otro sector;
- proyecto principal ajeno a la tarea;
- un visual del brief que contradecía el prompt de imagen;
- tareas "En revisión" cuyo texto decía que ya se habían entregado.

Se corrigieron en el script y se regeneró la versión.

## Distribución (250 filas)

| Corte | Valores |
|---|---|
| Decisión | publicar 180 (72 %), descartar 70 (28 %) |
| Descartes | 47 solo con distractores, 23 con una tarea publicable aún "En progreso" o "En revisión" |
| Área | innovación 67, IA 66, hardware 60, software 57 |
| Pilar (publicadas) | producto 66, educativo 42, servicio en territorio 24, cultura 22, hito 19, evento 17, catálogo 13 |
| Tipo de proyecto | interno 124, cliente 79 (los descartes sin tarea publicable no tienen tipo) |
| Split | train 214, val 36 (172 grupos; todas las variantes de un grupo van al mismo split) |
| Tamaño medio | entrada 1771 caracteres, salida 2509 caracteres |
| Brief | 132 imagen única y 48 carruseles; 167 combinaciones de estilo distintas en 180 propuestas |

**Sesgo "antes" (D1)**, tasa de publicación por área: hardware 0,67, IA 0,71, innovación 0,72,
software 0,79. La diferencia máxima es de 12 puntos. Sale de cuántos distractores tocan a cada
área, no de una regla de decisión. Se corregirá al generar la segunda mitad y se medirá otra vez.

El test no sale de aquí: serán los ~21 reportes reales anonimizados.

## Limitaciones (para el informe)

- **Un mismo autor para entradas y salidas.** El LLM que escribió el banco escribió también los
  reportes y las propuestas. El modelo puede aprender ese estilo y no el de los reportes reales.
  Por eso el test es con reportes reales.
- **Variedad limitada.** 125 tareas publicables generan 180 propuestas. Un mismo grupo junta hasta
  6 filas (versiones publicadas y sin terminar), con distinto contexto y distinto brief, siempre en
  el mismo split.
- **El visual sale de una sola descripción por tarea.** Gana coherencia, pero 64 de las 180
  propuestas quedan como "fotografía realista de la escena".
- **Una sola marca.** El kit de marca es siempre el de CorAll (decisión del proyecto).
- **Copy de referencia sin revisión de Marketing.** Falta que Marketing revise una muestra del
  banco y se ajuste el tono según lo que diga.
- **Las tareas de seguridad convertidas en consejo** (por ejemplo, "3 claves para integraciones
  seguras") son un criterio editorial propuesto, no una regla firmada por CorAll.
