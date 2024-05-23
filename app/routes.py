import re
from flask import redirect, url_for, render_template, session, request
from app.controllers import file_controller, qa_controller

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file_route():
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return render_template('index.html', error='No se ha seleccionado ningún archivo')
        # Llama a la función de controlador para cargar el archivo
        file_controller.upload_file()
        # Después de cargar el archivo, redirige a la página de preguntas
        return redirect(url_for('ask_question_route'))

    @app.route('/ask', methods=['GET', 'POST'])  # Permitir tanto GET como POST en /ask
    def ask_question_route():
        if request.method == 'GET':
            # Si es una solicitud GET, simplemente renderiza la plantilla de preguntas
            return render_template('ask.html')
        elif request.method == 'POST':
            # Verifica si el archivo está cargado en la sesión
            file_path = session.get('file_path')
            if not file_path:
                return "Error: No se ha cargado ningún archivo"
            return qa_controller.ask_question(file_path)