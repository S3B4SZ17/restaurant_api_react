import psycopg2, logging
from psycopg2.extensions import connection
from api.models.app_config import get_app_config
from sqlmodel import create_engine

logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s- %(message)s', level=logging.INFO)


cubox_be_config = get_app_config()
logging.info("Attempting connection to %s", cubox_be_config["postgres"]["database"])
try:
    host: str = cubox_be_config["postgres"]["hostname"]
    port: str = cubox_be_config["postgres"]["port"]
    user: str = cubox_be_config["postgres"]["user"]
    password: str = cubox_be_config["postgres"]["password"]
    database: str = cubox_be_config["postgres"]["database"]
    conn_string = 'postgresql://{user}:{password}@{host}:{port}/{database}'
    conn_string = conn_string.format(user=user, password=password, host=host, port=port, database=database)
    engine = create_engine(conn_string)

    logging.info("Successful connection!")
except Exception as exc:
    logging.error(f"Exception occured while connecting to the db %s", exc)

