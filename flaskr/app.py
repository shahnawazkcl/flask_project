from flask import Flask
from views import views
import __init__


app = __init__.create_app()
app.register_blueprint(views, url_prefix="/")
if __name__ == '__main__':
    app.run(debug=True, port=8000)

