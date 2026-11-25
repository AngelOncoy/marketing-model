# marketing-model

Proyecto integrador universitario (UPAO, ISIA-119 Modelos Generativos de IA, 2026-II) sobre un
**caso real de una empresa**. Sustentación: **8 de diciembre de 2026**.

> Fase de investigación. El stack aún no está decidido. No asumas tecnologías: si una decisión
> no está en "Decisiones", pregunta o propón opciones con justificación.

## Problema (alcance cerrado)

La empresa es **CorAll** (software y tecnología, Trujillo). Sus desarrolladores generan **reportes
diarios** (redactados con Claude). El sistema recibe esos reportes, decide qué es publicable y
genera **propuestas de marketing** para las redes de CorAll: descripción (copy) + hashtags +
brief de diseño y la **infografía final** (arquitectura híbrida: LLM ajustado + difusión para el
visual + compositor HTML para texto y logo exactos; ver `docs/plan.md`). La empresa decide si las
usa (humano en el bucle).
Plataformas: LinkedIn, Instagram y TikTok (guion de video, sin renderizar); Facebook como variante
de LinkedIn. El renderizado de motion graphics queda fuera de alcance. Estudio completo en
`docs/estudio-marketing.md`.

Ya existe en el ERP de CorAll (corall-app) el módulo "Propuestas IA", basado en prompting con
validadores por código. Es la **línea base** a superar o justificar; ver sección 8.1 del estudio.
Marca oficial: manual de marca 2025 (paleta, tipografías, logo) resumido en la sección 8.2.

Regla crítica: el modelo nunca debe filtrar información interna (rutas, issues, clientes, riesgos,
vulnerabilidades); descartar un reporte es una salida válida.

**Fuera de alcance**: el caso de microempresas con prompt libre. No ampliar el alcance.

## Reglas del curso (docs/Proyecto_Integrador_ISIA119_2026-II_v3.pdf)

Orden metodológico obligatorio: **problema de negocio → dataset → familia de modelo → modelo base
→ estrategia → evaluación → ética**. La tecnología sigue a la necesidad, nunca al revés.

- **Dataset (no negociable)**: >= 500 ejemplos instruction/response, limpio (sin duplicados,
  sin vacíos, codificación consistente). Datos de la empresa solo con autorización y bajo Ley 29733.
- **Familia de modelo**: justificar 4 criterios (naturaleza de datos/salida y dataset son
  eliminatorios; requisitos operativos y ecosistema son ponderados).
- **Modelo base**: alineado (SFT + RLHF/DPO), pesos abiertos, repo oficial en Hugging Face con
  revision/commit exacto, viable en Colab T4 (QLoRA 4-bit). Proponer >= 2 candidatos y compararlos con
  la matriz A-E (A Legal/licencia es eliminatoria; B técnica, C alineación/desempeño,
  D operacional, E ética/riesgo son ponderadas).
- **Estrategia** (declarar una): construcción desde datos, **PEFT (LoRA/QLoRA)** o integración
  (RAG/prompting/tool calling). Debe haber >= 1 métrica cuantitativa en un conjunto de prueba y
  comparación contra una **línea base** (modelo sin especializar o solución no-IA).
- **Ética desde el diseño**, no al final: Matriz EICE con >= 3 riesgos por dimensión
  (D1 sesgos con métrica de equidad, D2 privacidad Ley 29733, D3 transparencia/explicabilidad con aviso
  de IA, D4 UNESCO 2021 + IEEE EAD con punto de supervisión humana).
- **Reproducibilidad**: registrar modelo base + commit, versión del dataset, hiperparámetros
  (rank/alpha, learning rate, épocas), semilla y versiones (`requirements.txt`).
- **Entregables**: demo en vivo (con plan de contingencia), presentación de 15 min, Matriz EICE,
  informe IEEE (6-10 págs) y repo GitHub con README reproducible.

## Decisiones (completar a medida que se tomen)

- Dataset: sintético (banco de tareas escrito por LLM + ensamblado por script) para train/val;
  test con ~21 reportes reales anonimizados. JSONL instruction/input/output. v0.2 = 500 filas
  (`data/synthetic/`, ficha en `docs/ficha-dataset.md`), con descartes repartidos por área para
  igualar la tasa de publicación (D1).
- Arquitectura: **híbrida aprobada** (LLM autorregresivo + difusión + compositor HTML). Ver `docs/plan.md`.
- Despliegue: Cloudflare Workers AI (CorAll no tiene GPU). Solo admite LoRA sobre Mistral-7B-Instruct-v0.2,
  Gemma 2B/7B-it y Llama-2-7B-chat (beta); imagen con FLUX.1-schnell.
- Modelo base: _pendiente_ matriz A–E; candidatos Mistral-7B-Instruct-v0.2 y Gemma-2B-it.
- Estrategia: PEFT (QLoRA) en Colab T4 para el LLM; difusión sin ajuste fino (LoRA de estilo opcional).
- Python 3.11; stack completo en `docs/plan.md`.
- Marca como dato: `brand/brand.json` leído por el compositor; cada ejemplo del dataset lleva un kit
  corto de marca en la entrada. Nunca escribir colores, fuentes o eslóganes a mano en plantillas o código.
  Una sola variante de entrenamiento; multiempresa es trabajo futuro.
- Métricas y línea base: _pendiente_ (línea base: Propuestas IA actual y el modelo base sin ajustar;
  los validadores por código del ERP sirven como métricas)
- Justificación de negocio del modelo propio: _propuesta_ privacidad (los reportes no salen a un
  proveedor externo; Ley 29733) + costo (sin cuotas ni saldo de APIs). Confirmar con el equipo.
- Colores: `#BF1820` rojo de branding; `#A31924` solo dentro del isotipo.
- Bandeja de Propuestas IA: no se usa como dataset (casi todo son pruebas).
- Aportes de la propuesta MarketingGen Studio (compañero), adoptados sobre el caso CorAll:
  - **3 variantes de copy** por propuesta para que Marketing elija; se generan por muestreo en
    inferencia, el formato del dataset no cambia.
  - **Ficha del dataset** con conteo de filas eliminadas por motivo (vacías, duplicadas, sensibles).
  - **Splits sin fugas**: todas las variantes de un mismo reporte van al mismo split (train/val/test).
  - **Métrica "tasa de contenido que necesita corrección"**: % de propuestas que la revisión humana
    edita o rechaza.
  - **Consultar al docente** si "LLM principal + difusión complementaria" cumple el requisito de
    modelo alineado. _pendiente_
  - No se adopta: caso ficticio con prompt libre, dataset genérico en inglés, Qwen3/Gemma 3 (no
    desplegables con LoRA en Cloudflare), React + FastAPI.
- Entorno: `python -m venv .venv` y `.venv/Scripts/python.exe -m pip install -r requirements.txt`.
- Dataset: `PYTHONPATH=src .venv/Scripts/python.exe -m marketing_model.generate.build_synthetic --n 500 --seed 42`
  y luego `... -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.2.raw.jsonl`.
- Comandos de test / lint: _pendiente_

## Reglas de trabajo

- Idioma: conversación, docs y copy generado en español; código e identificadores en inglés.
- Antes de implementar algo no trivial: investigar y proponer un plan; no escribir código sin acuerdo.
- Los reportes son datos de negocio sensibles: nunca commitearlos ni enviarlos a servicios externos
  sin confirmar. En el repo solo datos anonimizados o sintéticos.
- Nunca commitear claves de API ni `.env`.
- Commits pequeños y atómicos, en ramas por tarea (`feat/`, `fix/`, `docs/`...).
- Reglas locales de commits y autoría (prevalecen): @AGENTS.local.md
- Registrar aquí el comando exacto cuando se añada tooling.
- Si el agente se equivoca repetidamente en algo, añadir la corrección a este archivo.
