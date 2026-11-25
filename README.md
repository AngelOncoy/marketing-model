# marketing-model

Proyecto integrador del curso ISIA-119 Modelos Generativos de IA (UPAO, 2026-II), sobre un caso
real de **CorAll** (software y tecnología, Trujillo).

El sistema recibe los reportes diarios de los desarrolladores y decide si hay algo publicable. Si
lo hay, genera una propuesta de marketing para LinkedIn, Facebook, Instagram y TikTok: copy,
hashtags, guion de video y brief de diseño, además de la infografía final. Marketing decide si la
usa (humano en el bucle).

Arquitectura híbrida:
- un LLM ajustado con QLoRA genera la propuesta en JSON;
- un modelo de difusión (FLUX.1-schnell) genera solo el visual;
- un compositor HTML coloca el texto y el logo exactos.

## Estado

- Dataset sintético v0.2 listo: 500 filas limpias y validadas, equilibradas por área.
- Lo que falta y cómo continuar está en **[docs/siguientes-pasos.md](docs/siguientes-pasos.md)**.

## Inicio rápido

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.build_synthetic --n 500 --seed 42
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.2.raw.jsonl
```

## Documentos

| Documento | Contenido |
|---|---|
| [docs/siguientes-pasos.md](docs/siguientes-pasos.md) | Estado, tareas pendientes y reglas del equipo |
| [docs/plan.md](docs/plan.md) | Arquitectura, stack, fases y métricas |
| [docs/estudio-marketing.md](docs/estudio-marketing.md) | Estudio de marketing y línea base (Propuestas IA) |
| [docs/ficha-dataset.md](docs/ficha-dataset.md) | Ficha del dataset: método, distribución, sesgo y limitaciones |
| [CLAUDE.md](CLAUDE.md) | Reglas del curso y decisiones tomadas |

## Estructura

```
brand/brand.json                 kit de marca (colores, tipografías, eslóganes)
data/synthetic/                  dataset sintético y su ficha
src/marketing_model/schema.py    esquema de la propuesta (Pydantic)
src/marketing_model/validators.py validadores usados como filtro y como métricas
src/marketing_model/generate/    generador del dataset y banco de tareas
```

## Equipo (Grupo 6)

Oncoy Patricio, Angel · Alcántara Lopez, Alain · Ulco Lazo, Fabricio · Cisneros Bartra, Adrián
