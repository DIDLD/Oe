from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import (
    UsuarioDTOPeticion, UsuarioDTORespuesta,
    GastoDTOPeticion, GastoDTORespuesta,
    CategoriaDTOPeticion, CategoriaDTORespuesta,
    MetodoPagoDTOPeticion, MetodoPagoDTORespuesta,
    FacturaDTOPeticion, FacturaDTORespuesta
)
from app.api.models.modelosApp import Usuario, Gasto, Categoria, MetodoPago, Factura
from app.database.configuration import sessionLocal, engine

# Para que un api funcione debe tener un archivo enrutador
rutas = APIRouter()  # ENDPOINTS

# Crear una función para establecer cuando yo quiera y necesite
# conexion hacia la base de datos
def getDataBase():
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

# SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion: UsuarioDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        usuario = Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=usuario.id,
            nombre=usuario.nombres,  # Asegúrate de usar el campo correcto
            telefono=usuario.telefono,
            ciudad=usuario.ciudad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario {error}")

# SERVICIO PARA OBTENER TODOS LOS USUARIOS
@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db: Session = Depends(getDataBase)):
    try:
        listadoDeUsuarios = db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=usuario.id,
                nombre=usuario.nombres, 
                telefono=usuario.telefono,
                ciudad=usuario.ciudad
            ) for usuario in listadoDeUsuarios
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios {error}")

# NUEVO SERVICIO PARA OBTENER GASTOS DE UN USUARIO
@rutas.get("/usuarios/{usuario_id}/gastos", response_model=List[GastoDTOPeticion])
def obtenerGastosDeUsuario(usuario_id: int, db: Session = Depends(getDataBase)):
    try:
        gastos = db.query(Gasto).filter(Gasto.id_usuario == usuario_id).all()
        return [
            GastoDTOPeticion(
                nombre=gasto.nombre,
                monto=gasto.monto,
                fecha=gasto.fecha,
                descripcion=gasto.descripcion,
                ingresos=gasto.ingresos
            ) for gasto in gastos
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener los gastos {error}")

# SERVICIO PARA REGISTRAR UN GASTO
@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion: GastoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        gasto = Gasto(
            nombre=datosPeticion.nombre,
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            ingresos=datosPeticion.ingresos
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return GastoDTORespuesta(
            id_gasto=gasto.id_gasto,
            nombre=gasto.nombre,
            monto=gasto.monto,
            fecha=gasto.fecha,
            descripcion=gasto.descripcion,
            ingresos=gasto.ingresos
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto {error}")

# SERVICIO PARA OBTENER TODOS LOS GASTOS
@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def obtenerGastos(db: Session = Depends(getDataBase)):
    try:
        gastos = db.query(Gasto).all()
        return [
            GastoDTORespuesta(
                id_gasto=gasto.id_gasto,
                nombre=gasto.nombre,
                monto=gasto.monto,
                fecha=gasto.fecha,
                descripcion=gasto.descripcion,
                ingresos=gasto.ingresos
            ) for gasto in gastos
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener los gastos {error}")

# SERVICIO PARA REGISTRAR UNA CATEGORÍA
@rutas.post("/categorias", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion: CategoriaDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        categoria = Categoria(
            nombre_categoria=datosPeticion.nombre_categoria,
            descripcion_categoria=datosPeticion.descripcion_categoria,
            foto_icono=datosPeticion.foto_icono
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return CategoriaDTORespuesta(
            id_categoria=categoria.id_categoria,
            nombre_categoria=categoria.nombre_categoria,
            descripcion_categoria=categoria.descripcion_categoria,
            foto_icono=categoria.foto_icono
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la categoría {error}")

# SERVICIO PARA OBTENER TODAS LAS CATEGORÍAS
@rutas.get("/categorias", response_model=List[CategoriaDTORespuesta])
def obtenerCategorias(db: Session = Depends(getDataBase)):
    try:
        categorias = db.query(Categoria).all()
        return [
            CategoriaDTORespuesta(
                id_categoria=categoria.id_categoria,
                nombre_categoria=categoria.nombre_categoria,
                descripcion_categoria=categoria.descripcion_categoria,
                foto_icono=categoria.foto_icono
            ) for categoria in categorias
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener las categorías {error}")

# SERVICIO PARA REGISTRAR UN METODO DE PAGO
@rutas.post("/metodos_pago", response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion: MetodoPagoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        metodo_pago = MetodoPago(
            nombre_metodo=datosPeticion.nombre_metodo,
            descripcion_metodo=datosPeticion.descripcion_metodo
        )
        db.add(metodo_pago)
        db.commit()
        db.refresh(metodo_pago)
        return MetodoPagoDTORespuesta(
            id_metodo_pago=metodo_pago.id_metodo_pago,
            nombre_metodo=metodo_pago.nombre_metodo,
            descripcion_metodo=metodo_pago.descripcion_metodo
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el método de pago {error}")

# SERVICIO PARA OBTENER TODOS LOS METODOS DE PAGO
@rutas.get("/metodos_pago", response_model=List[MetodoPagoDTORespuesta])
def obtenerMetodosPago(db: Session = Depends(getDataBase)):
    try:
        metodos_pago = db.query(MetodoPago).all()
        return [
            MetodoPagoDTORespuesta(
                id_metodo_pago=metodo_pago.id_metodo_pago,
                nombre_metodo=metodo_pago.nombre_metodo,
                descripcion_metodo=metodo_pago.descripcion_metodo
            ) for metodo_pago in metodos_pago
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener los métodos de pago {error}")

# SERVICIO PARA REGISTRAR UNA FACTURA
@rutas.post("/facturas", response_model=FacturaDTORespuesta)
def guardarFactura(datosPeticion: FacturaDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        factura = Factura(
            monto_factura=datosPeticion.monto_factura,
            fecha_factura=datosPeticion.fecha_factura,
            descripcion_factura=datosPeticion.descripcion_factura
        )
        db.add(factura)
        db.commit()
        db.refresh(factura)
        return FacturaDTORespuesta(
            id_factura=factura.id_factura,
            monto_factura=factura.monto_factura,
            fecha_factura=factura.fecha_factura,
            descripcion_factura=factura.descripcion_factura
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la factura {error}")

# SERVICIO PARA OBTENER TODAS LAS FACTURAS
@rutas.get("/facturas", response_model=List[FacturaDTORespuesta])
def obtenerFacturas(db: Session = Depends(getDataBase)):
    try:
        facturas = db.query(Factura).all()
        return [
            FacturaDTORespuesta(
                id_factura=factura.id_factura,
                monto_factura=factura.monto_factura,
                fecha_factura=factura.fecha_factura,
                descripcion_factura=factura.descripcion_factura
            ) for factura in facturas
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al obtener las facturas {error}")
