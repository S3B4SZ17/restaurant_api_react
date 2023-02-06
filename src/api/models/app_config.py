import yaml, logging, os

logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s- %(message)s', level=logging.INFO)

def env_constructor(loader, node):
    return os.environ[node.value[0:]]

def get_app_config() -> dict:
    '''
    Gets the cubox-be app config from yaml
    '''
    app_config: dict = {}
    with open('app_config.yaml', 'r', encoding='utf8') as file:
        try:
            yaml.add_constructor("!env", env_constructor, Loader=yaml.SafeLoader)
            app_config: dict = yaml.safe_load(file)
        except Exception as exc:
            logging.error(exc)
    return app_config