# -*- encoding: utf-8 -*-
from authservice import create_app

app = create_app('config')

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
