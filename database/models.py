from .db import db


class Client(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    preexistence = db.ListField(db.StringField(), required=True)

class CrearServicio(db.Document):
    id_servicio = db.StringField(required=True, unique=True)
    nombre_servicio = db.StringField(required=True)
    cod_servicio = db.StringField(required=True, unique=True)
    estado_servicio = db.StringField(required=True)
    
 class ConsultarServicio(db.Document):
    id_servicio = db.StringField(required=True, unique=True)
    nombre_servicio = db.StringField(required=True)
    cod_servicio = db.StringField(required=True, unique=True)
    estado_servicio = db.StringField(required=True)      
    
  class ActualizarServicio(db.Document):
    id_servicio = db.StringField(required=True, unique=True)
    nombre_servicio = db.StringField(required=True)
    cod_servicio = db.StringField(required=True, unique=True)
    estado_servicio = db.StringField(required=True)
    
 class InactivarServicio(db.Document):
    id_servicio = db.StringField(required=True, unique=True)
    nombre_servicio = db.StringField(required=True)
    cod_servicio = db.StringField(required=True, unique=True)
    estado_servicio = db.StringField(required=True)
      
