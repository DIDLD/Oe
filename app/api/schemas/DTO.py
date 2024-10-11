from pydantic import BaseModel
from datetime import date

# DTO para Usuario
class UsuarioDTOPeticion(BaseModel):
    nombre: str
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro: date
    ciudad: str 

    class Config:
        orm_mode = True

class UsuarioDTORespuesta(BaseModel):
    id: int
    nombre: str
    telefono: str
    ciudad: str

    class Config:
        orm_mode = True

# DTO para Gasto
class GastoDTOPeticion(BaseModel):
    nombre: str
    monto: float
    fecha: date
    descripcion: str
    ingresos: float

    class Config:
        orm_mode = True

class GastoDTORespuesta(BaseModel):
    id_gasto: int
    nombre: str
    monto: float
    fecha: date
    descripcion: str
    ingresos: float

    class Config:
        orm_mode = True

# DTO para Categoria
class CategoriaDTOPeticion(BaseModel):
    nombre_categoria: str
    descripcion_categoria: str
    foto_icono: str

    class Config:
        orm_mode = True

class CategoriaDTORespuesta(BaseModel):
    id_categoria: int
    nombre_categoria: str
    descripcion_categoria: str
    foto_icono: str

    class Config:
        orm_mode = True

# DTO para MetodoPago
class MetodoPagoDTOPeticion(BaseModel):
    nombre_metodo: str
    descripcion_metodo: str

    class Config:
        orm_mode = True

class MetodoPagoDTORespuesta(BaseModel):
    id_metodo_pago: int
    nombre_metodo: str
    descripcion_metodo: str

    class Config:
        orm_mode = True

# DTO para Factura
class FacturaDTOPeticion(BaseModel):
    monto_factura: float
    fecha_factura: date
    descripcion_factura: str

    class Config:
        orm_mode = True

class FacturaDTORespuesta(BaseModel):
    id_factura: int
    monto_factura: float
    fecha_factura: date
    descripcion_factura: str

    class Config:
        orm_mode = True
