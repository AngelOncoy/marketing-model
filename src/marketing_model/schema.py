"""Output schema of the model: decision + evaluated ideas + proposal (docs/estudio-marketing.md, s. 6)."""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

Pilar = Literal["producto", "catalogo", "evento", "cultura", "servicio_territorio", "educativo", "hito"]
Area = Literal["software", "hardware", "ia", "innovacion"]


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Idea(Strict):
    fuente: str = Field(min_length=3)
    pilar: Pilar
    valor: int = Field(ge=1, le=5)
    riesgo: int = Field(ge=1, le=5)
    publicable: bool
    razon: str = Field(min_length=10)


class Copys(Strict):
    linkedin: str = Field(min_length=200)
    facebook: str = Field(min_length=80)
    instagram: str = Field(min_length=80)


class Hashtags(Strict):
    linkedin: list[str] = Field(min_length=3, max_length=5)
    instagram: list[str] = Field(min_length=5, max_length=8)
    tiktok: list[str] = Field(min_length=3, max_length=5)


class Toma(Strict):
    segundos: str
    toma: str
    voz: str


class Estilo(Strict):
    fondo: str
    footer: str
    logo: str
    visual: str
    composicion: str
    cta: str


class Textos(Strict):
    titulo: str
    bullets: list[str] = Field(max_length=4)
    dato: Optional[str] = None
    cta: str
    eslogan: str


class Diapositiva(Strict):
    titulo: str
    texto: str
    visual: str


class Pieza(Strict):
    formato: Literal["imagen_unica", "carrusel"]
    ratio: Literal["4:5", "1:1", "1.91:1"]
    resolucion: str
    estilo: Estilo
    textos: Textos
    diapositivas: list[Diapositiva]
    imagen_adjunta: Literal["ninguna", "hardware", "campo", "equipo"]
    prompt_imagen: str

    @model_validator(mode="after")
    def check_slides(self) -> "Pieza":
        if self.formato == "carrusel" and not 6 <= len(self.diapositivas) <= 10:
            raise ValueError("a carousel needs 6-10 slides")
        if self.formato == "imagen_unica" and self.diapositivas:
            raise ValueError("a single image has no slides")
        return self


class Propuesta(Strict):
    pilar: Pilar
    area: Area
    tipo_proyecto: Literal["interno", "cliente"]
    copys: Copys
    hashtags: Hashtags
    guion_tiktok: list[Toma] = Field(min_length=3, max_length=5)
    pieza: Pieza


class Output(Strict):
    decision: Literal["publicar", "descartar"]
    motivo_descarte: Optional[str]
    ideas_evaluadas: list[Idea] = Field(min_length=1)
    propuesta: Optional[Propuesta]

    @model_validator(mode="after")
    def check_decision(self) -> "Output":
        if self.decision == "publicar" and (self.propuesta is None or self.motivo_descarte):
            raise ValueError("publish requires a proposal and no discard reason")
        if self.decision == "descartar" and (self.propuesta is not None or not self.motivo_descarte):
            raise ValueError("discard requires a reason and no proposal")
        if self.decision == "publicar" and not any(i.publicable for i in self.ideas_evaluadas):
            raise ValueError("publish requires at least one publishable idea")
        if self.decision == "descartar" and any(i.publicable for i in self.ideas_evaluadas):
            raise ValueError("discard cannot contain publishable ideas")
        return self
