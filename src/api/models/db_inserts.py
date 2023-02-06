from api.models.restaurant import Restaurant, Restaurant_type
from api.models.postgresql import engine
from sqlmodel import Session, SQLModel

def insert_test_data():

    # 2 - generate database schema
    SQLModel.metadata.create_all(engine)

    # 4 - create Users
    tipo_rest = Restaurant_type("Bar Rest", "Restaurante con bebidas alcoholicas")
    tipo_rest2 = Restaurant_type("Italiano", "Restaurante especializado en comida Italiana")
    tipo_rest3 = Restaurant_type("Japones", "Restaurante especializado en comida Japonesa")
    
    # 3 - create a new session
    with Session(engine) as session:
        # 5 - persists data
        session.add(tipo_rest)
        session.add(tipo_rest2)
        session.add(tipo_rest3)

        # 6 - commit and close session
        session.commit()
        restaurante = Restaurant("Santo Pecado", "Plaza Real Alajuela", tipo_rest.id)
        session.add(restaurante)
        session.commit()
        session.close()
