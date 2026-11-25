# Siguientes pasos (guía para el equipo)

Estado al 24 de noviembre de 2026. Sustentación: **8 de diciembre de 2026**.

Este documento dice qué está hecho, cómo arrancar y qué falta, en el orden metodológico del curso:
**problema → dataset → familia → modelo base → estrategia → evaluación → ética**.

## 1. Qué está hecho

| Parte | Estado | Dónde |
|---|---|---|
| Problema de negocio y estudio de marketing | Hecho | `docs/estudio-marketing.md` |
| Plan, arquitectura híbrida y stack | Hecho | `docs/plan.md` |
| Kit de marca como dato | Hecho | `brand/brand.json` |
| Esquema de salida (JSON) | Hecho | `src/marketing_model/schema.py` |
| Validadores (fugas, cifras, exageraciones, hashtags, formato) | Hecho | `src/marketing_model/validators.py` |
| Dataset sintético v0.2: 500 filas limpias, equilibradas por área | Hecho | `data/synthetic/synthetic_v0.2.jsonl`, ficha en `docs/ficha-dataset.md` |
| Generador y banco de tareas | Hecho | `src/marketing_model/generate/` |

Cifras clave del dataset:
- 360 propuestas publicables y 140 descartes.
- 436 filas de entrenamiento y 64 de validación, sin fugas entre splits.
- La tasa de publicación es 0,72 en las cuatro áreas.
- El test no sale del dataset sintético: serán ~21 reportes reales anonimizados (ver 3.3).

## 2. Cómo arrancar

Requisitos: Python 3.11 y git.

```bash
git clone https://github.com/AngelOncoy/marketing-model.git
cd marketing-model
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

En Linux o macOS se usa `.venv/bin/python` en lugar de `.venv/Scripts/python.exe`.

Regenerar y validar el dataset (debe dar 500 filas limpias y 0 eliminadas):

```bash
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.build_synthetic --n 500 --seed 42
PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.2.raw.jsonl
```

Para cambiar el copy de referencia, edita las tareas en `src/marketing_model/generate/bank/`
(`cards_*.py` son las publicables, `nonpub*.py` los distractores y `wip.py` las versiones sin terminar),
regenera y vuelve a validar. No edites las filas del JSONL a mano.

## 3. Qué falta, en orden

Cada tarea dice qué hay que entregar. Las marcadas con **(terceros)** dependen de alguien fuera del
equipo: conviene pedirlas ya, porque son las que más tardan.

### 3.1 Familia de modelo

- [ ] Escribir `docs/familia-modelo.md` con los 4 criterios del curso:
  - eliminatorios: naturaleza de datos y salida (texto a JSON estructurado) y dataset (500 pares instruction/response);
  - ponderados: requisitos operativos (Colab T4, Cloudflare Workers AI) y ecosistema (Hugging Face, `peft`, `trl`).
- Conclusión esperada: LLM autorregresivo decodificador alineado; la difusión solo genera el visual.

### 3.2 Modelo base (matriz A–E)

- [ ] Escribir `docs/matriz-modelos.md` comparando **Mistral-7B-Instruct-v0.2** y **Gemma-2B-it**.
  - A (licencia, eliminatoria): revisar la licencia de Gemma (términos de uso de Google) y Apache 2.0 de Mistral.
  - B (técnica), C (alineación y desempeño), D (operacional) y E (ética y riesgo): ponderadas.
  - Registrar el repo oficial de Hugging Face y el **commit exacto** de cada modelo.
- [ ] **Prueba rápida en Cloudflare Workers AI**: subir un LoRA mínimo al modelo elegido y comprobar que
  responde. Si falla, cambia la elección. Hacerla antes de entrenar en serio.
- [ ] **(terceros)** Consultar al docente si "LLM principal + difusión complementaria" cumple el requisito
  de modelo alineado.
- [ ] Al decidir, actualizar la sección "Decisiones" de `CLAUDE.md`.

### 3.3 Test real y anonimizador

- [ ] **(terceros)** Pedir a CorAll la **autorización escrita** para usar ~21 reportes reales (Ley 29733).
- [ ] Implementar `src/marketing_model/anonymize.py`: reemplazar clientes y personas por
  `[CLIENTE_n]` y `[PERSONA_n]`. Lo usan el test y la demo.
- [ ] Armar el test en `data/real/` (carpeta privada, no se sube) con su propuesta de referencia por
  reporte. Solo se sube la versión anonimizada, si CorAll lo autoriza.

### 3.4 Línea base y métricas

- [ ] Medir sobre el test, con los validadores como métricas:
  - Propuestas IA actual del ERP;
  - el modelo base sin ajustar.
- Métricas (detalle en `docs/plan.md`, sección 7):
  - JSON válido (%);
  - fugas (objetivo 0);
  - acierto publicar/descartar;
  - validadores de copy;
  - tasa de contenido que necesita corrección.
- [ ] Registrar los comandos exactos de evaluación en `CLAUDE.md`.

### 3.5 Entrenamiento (QLoRA en Colab T4)

- [ ] `notebooks/train_qlora.ipynb` con `transformers`, `peft`, `trl` y `bitsandbytes`.
- [ ] Registrar, para la reproducibilidad:
  - el modelo y su commit;
  - la versión del dataset (v0.2);
  - rank y alpha, learning rate y épocas;
  - la semilla;
  - las versiones en `requirements.txt`.
- [ ] Generar **3 variantes de copy** por propuesta por muestreo en inferencia (el dataset no cambia).
- [ ] Subir el LoRA a Workers AI.

### 3.6 Imagen y compositor

Puede avanzar en paralelo con 3.1–3.5.

- [ ] Cliente de FLUX.1-schnell en Workers AI, en `src/marketing_model/image/`. Usa el
  `prompt_imagen` de la propuesta.
- [ ] Compositor HTML/CSS con Playwright en `src/marketing_model/compose/`:
  - pone el título, los bullets, el dato, el CTA, el eslogan y el logo exactos sobre la imagen;
  - lee colores, fuentes y eslóganes de `brand/brand.json`, nunca escritos a mano;
  - incluye carruseles.
- [ ] Los logos y las fuentes comerciales van en `brand/assets/` (ignorada por git). Pedirlos a
  CorAll y no subirlos.

### 3.7 Evaluación y ética

- [ ] Métricas después del ajuste frente a las líneas base, y análisis de fallos.
- [ ] Sesgo D1 "después": tasa de publicación por área, y además por tipo de proyecto (interno/cliente).
- [ ] `docs/eice.md`: Matriz EICE con ≥ 3 riesgos por dimensión:
  - D1: sesgos, con métrica de equidad;
  - D2: privacidad, Ley 29733;
  - D3: transparencia, con aviso de IA;
  - D4: UNESCO 2021 + IEEE EAD, con el punto de supervisión humana.

### 3.8 Cierre

- [ ] Demo en Gradio (`app/gradio_app.py`) y video de respaldo por si falla en vivo.
- [ ] Informe IEEE (6–10 páginas) y presentación de 15 minutos.
- [ ] README reproducible de punta a punta.
- [ ] Ensayo con todo el equipo.

### Pendientes abiertos del dataset

- [ ] **(terceros)** Que Marketing de CorAll revise una muestra de ~20 propuestas. Si pide cambios
  de tono, se corrigen en el banco y se regenera.
- [ ] Opcional: más variedad visual (155 de 360 propuestas usan "fotografía realista de la escena").

## 4. Reglas de trabajo del equipo

- **Ramas por tarea:** `feat/`, `fix/`, `docs/`… y siempre PR a `main`. Nada directo a `main`.
- **Commits:** solo el título, en español y con Conventional Commits.
  Ejemplo: `feat: agregar anonimizador de reportes`.
- **Datos:** nunca subir reportes reales sin anonimizar, claves de API ni `.env`. En el repo solo hay
  datos sintéticos o anonimizados.
- **Marca:** colores, fuentes y eslóganes salen de `brand/brand.json`. El rojo de branding es `#BF1820`;
  `#A31924` va solo dentro del isotipo.
- **Alcance cerrado:** el caso es CorAll. El prompt libre para microempresas queda fuera.
- **Decisiones:** cada decisión tomada se anota en la sección "Decisiones" de `CLAUDE.md`, y cada
  comando nuevo de tooling también.
