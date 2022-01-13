from app import app
from config import config

def page_error(error):
    return '<h1>La pagina no existe</h1>'

# Server run

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,page_error)
    app.run()