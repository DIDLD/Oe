from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(150))
    edad=Column(Integer)
    telefono=Column(String(120))
    correo=Column(String(200))
    contraseña=Column(String(100))
    fechaRegistro=Column(Date)
    ciudad=Column(String(150))




class Gasto(Base):
    __tablename__ = 'gastos'

    id_gasto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))
    monto = Column(Float)
    fecha = Column(Date)
    descripcion = Column(String(100))
    ingresos = Column(Float)



class Categoria(Base):
    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre_categoria = Column(String(150))
    descripcion_categoria = Column(String(100))
    foto_icono = Column(String(150))


class MetodoPago(Base):
    __tablename__ = 'metodos_pago'
    id_metodo_pago = Column(Integer, primary_key=True, autoincrement=True)
    nombre_metodo = Column(String(150))
    descripcion_metodo = Column(String(150))


class Factura(Base):
    __tablename__ = 'facturas'

    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    monto_factura = Column(Float)
    fecha_factura = Column(Date)
    descripcion_factura = Column(String(100))


