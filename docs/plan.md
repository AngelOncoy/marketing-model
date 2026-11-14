# Plan del proyecto: arquitectura, stack y fases

Estado: **aprobado** el enfoque híbrido (14/11/2026). Sustentación: martes 8/12/2026.
Contexto de negocio y marca: `docs/estudio-marketing.md`.

## 1. Justificación de negocio

CorAll ya genera propuestas con prompting a modelos externos ("Propuestas IA" en corall-app). Un
modelo propio especializado aporta:
- **Costo**: sin saldo ni cuotas por minuto de APIs comerciales; el despliegue en Cloudflare
  Workers AI entra en la cuenta que CorAll ya usa (asignación gratuita diaria + pago por uso).
- **Privacidad**: los reportes no se envían a proveedores de LLM de terceros (Ley 29733).
- **Marca integrada**: el modelo aprende el formato, el tono y las reglas de marca sin un prompt enorme,
  y el compositor garantiza logo, colores y tipografías oficiales.

## 2. Arquitectura (híbrida: autorregresiva + difusión)

```
Reporte diario (.md)
  │ 1. Anonimizador (reglas): clientes, personas, rutas, issues/PR, teléfonos, correos
  ▼
LLM ajustado con QLoRA ──► JSON: decisión + ideas evaluadas + copy por red + hashtags + brief
  │ 2. Validadores: esquema, cifras, fugas, exageraciones, hashtags
  ▼
Brief de diseño
  ├─► 3a. Difusión (FLUX.1-schnell): solo el visual, sin texto ni logos
  └─► 3b. Compositor de marca (HTML/CSS → PNG): layout, textos exactos, logo real, fuentes, colores
  ▼
Infografía PNG / carrusel (PNG + PDF) + copy por red ──► revisión humana (aprobar / editar / rechazar)
```

El copy se entrega en 3 variantes (muestreo en inferencia) para que Marketing elija.

Por qué híbrida:
- El manual de marca prohíbe alterar el logo; los modelos de difusión deforman logos y escriben mal en
  español. La difusión genera el visual y el compositor coloca texto y logo exactos.
- Variedad: el LLM elige familia de layout, footer, posición del logo, fondo y composición. Con ~6
  familias y sus variantes hay cientos de combinaciones, no una plantilla fija.
- Dos familias justificadas por requisitos distintos: texto estructurado (autorregresiva) e imagen
  (difusión).

Fuera de alcance: motion graphics y video renderizado (TikTok recibe guion y prompt).
Opcional si sobra tiempo: LoRA de estilo CorAll sobre el modelo de difusión.

**Kit de marca como dato (decidido).** La marca vive en `brand/brand.json` (paleta, fuentes, logos,
eslóganes, tono, temas prohibidos, plataformas). El compositor lo lee mediante variables y cada
ejemplo del dataset incluye una versión corta del kit en la entrada. Para CorAll el resultado es el
mismo; el formato queda listo para otras marcas sin rehacer el dataset. Se entrena una sola variante
(no se comparan dos). Con un único kit, el modelo no aprende a seguir marcas distintas: eso es
trabajo futuro (sección 8).

## 3. Despliegue en Cloudflare (verificado el 14/11/2026, revisar antes de desplegar)

Cloudflare Workers AI permite subir **adaptadores LoRA propios**, pero solo sobre una lista corta de
modelos base, y la función está en **beta abierta** (gratis durante la beta):

| Modelo base con LoRA en Workers AI | Notas |
|---|---|
| `mistral-7b-instruct-v0.2-lora` | Apache 2.0 |
| `gemma-2b-it-lora`, `gemma-7b-it-lora` | Términos de uso de Gemma (revisar en la matriz A) |
| `llama-2-7b-chat-hf-lora` | Licencia Llama 2; modelo antiguo |

Restricciones: base sin cuantizar, rank <= 8 (hasta 32 según el modelo), archivo < 300 MB,
archivos `adapter_config.json` y `adapter_model.safetensors`, `model_type` mistral/gemma/llama.
Subida con `npx wrangler ai finetune create <modelo> <nombre> <carpeta>`; inferencia con el
parámetro `lora`.

Imagen: Workers AI ofrece `flux-1-schnell` (además de SDXL y FLUX.2 klein). Se cobra por tiles de
512x512 y pasos; la cuenta tiene 10 000 neurons gratis al día. Una estimación de terceros da ~170
imágenes de 1024x1024 al día dentro de lo gratuito.

Consecuencias:
- **El modelo base debe estar en esa lista** si queremos desplegar en Cloudflare. Esto entra como
  criterio D (operacional) de la matriz A–E.
- corall-app ya tiene a Cloudflare como proveedor de IA, así que la integración futura es añadir
  el parámetro `lora` a la llamada existente.
- Riesgo: es beta. Plan B: inferencia local con `transformers` (o GGUF con llama.cpp) para la demo.
- Un adaptador entrenado con QLoRA (base en 4 bits) se aplica sobre la base en 16 bits en Cloudflare;
  hay que medir que la calidad no cambie (evaluar con la base sin cuantizar antes de subir).
- El compositor HTML → PNG: en la demo corre en Python con Playwright; en producción puede ir en el
  navegador de la intranet o en Cloudflare Browser Rendering (costo no verificado).
- Cloudflare no entrena: el entrenamiento se hace en Colab T4.

## 4. Stack

| Parte | Herramientas |
|---|---|
| Lenguaje | Python 3.11 |
| LLM candidatos | Mistral-7B-Instruct-v0.2 y Gemma-2B-it (desplegables en Cloudflare); Qwen3-4B como referencia de calidad no desplegable |
| Ajuste fino | `transformers`, `peft` (QLoRA, rank <= 8 o 32), `trl` (SFT), `bitsandbytes`; Colab T4 |
| Difusión | FLUX.1-schnell (Apache 2.0) vía Workers AI; local con `diffusers` como respaldo |
| Compositor | Plantillas HTML/CSS + Playwright → PNG / PDF |
| Esquema y validación | Pydantic; validadores del ERP portados a Python |
| Demo | Gradio; video de respaldo |
| Reproducibilidad | `requirements.txt`, semillas, revisión exacta de cada modelo; MLflow o W&B opcional |

## 5. Estructura del repositorio

```
marketing-model/
  CLAUDE.md  README.md  requirements.txt  .env.example
  docs/        estudio-marketing.md, plan.md, matriz-modelos.md, eice.md, informe/
  brand/       logos y fuentes (ver nota de licencias)
  data/
    real/      reportes reales anonimizados (test)     [privado hasta anonimizar]
    synthetic/ reports/*.md, targets.jsonl
    dataset/   train.jsonl, val.jsonl, test.jsonl
    manifest.csv
  src/marketing_model/
    schema.py  anonymize.py  validators.py
    generate/  (herramientas del dataset)
    compose/   templates/ (familias de layout), render.py
    image/     (cliente FLUX en Workers AI y local)
    inference/ (local y Workers AI con LoRA)
  notebooks/   train_qlora.ipynb, eval.ipynb
  app/         gradio_app.py
  tests/
```

Nota de licencias: la fuente Artegra Soft Condensed y Zapf Calligraphic son comerciales y los logos
son de CorAll. Si el repositorio es público, no subirlos: documentar cómo obtenerlos y cargarlos
desde una carpeta ignorada por git. Pedir autorización a CorAll para publicar el logo en ejemplos.

## 6. Fases

Las fases se gestionan por orden y entregable, sin fechas por fase.

| Fase | Entregable |
|---|---|
| 0. Bases | Repo con estructura, `requirements.txt`, esquema JSON, taxonomía (área × pilar × tipo de proyecto), matriz A–E (LLM y difusión) |
| 1. Dataset | ~21 reportes reales anonimizados con propuestas de referencia (test); 500 sintéticos por lotes de ~25, validados, sin duplicados, balanceados por área; splits sin fugas (variantes de un reporte en el mismo split); ficha del dataset con filas eliminadas por motivo; métrica de sesgo "antes" |
| 2. Compositor e imagen | 6 familias de layout, integración FLUX, carruseles |
| 3. Entrenamiento | QLoRA en Colab; evaluación de líneas base (modelo sin ajustar y Propuestas IA actual) |
| 4. Evaluación, ética y despliegue | Métricas, sesgo "después", Matriz EICE, análisis de fallos, LoRA subido a Workers AI |
| 5. Cierre | Demo Gradio, informe IEEE, diapositivas, video de contingencia, ensayo con el equipo |

Las fases 1 y 2 pueden avanzar en paralelo si otro integrante toma el compositor.

## 7. Métricas

- Validez del JSON y campos completos (%).
- Fuga confidencial sobre el test (objetivo 0).
- Exactitud de la decisión publicar / descartar.
- Validadores: cifras verificadas, exageraciones, hashtags por red.
- Calidad del copy: rúbrica 1-5 con evaluación humana ciega frente a las líneas base.
- Tasa de contenido que necesita corrección: % de propuestas que la revisión humana edita o rechaza.
- Diversidad de diseño: variedad de combinaciones de layout entre propuestas.
- Sesgo (D1): paridad de selección entre áreas (software, hardware, IA, innovación) y entre proyectos
  internos y de clientes, antes y después de balancear.
- Latencia y costo por propuesta (local y Workers AI).

## 8. Trabajo futuro

- **Multiempresa**: entrenar con varios kits de marca para que el modelo siga el kit que recibe;
  onboarding para subir logos, fuentes y paleta (con chequeo de contraste); extracción automática del
  kit desde el manual de marca y ejemplos de estilo desde posts anteriores (few-shot / RAG); LoRA por
  cliente como opción para empresas con mucho historial.
- Entradas genéricas además de reportes: PDF, Markdown y prompt libre.
- LoRA de estilo visual por marca sobre el modelo de difusión.
- Motion graphics y video renderizado.
