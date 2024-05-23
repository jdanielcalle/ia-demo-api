from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'pptx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No se adjuntó ningún archivo.')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No se ha seleccionado ningún archivo.')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            flash('Archivo cargado con éxito.')
            
            # Guardar la ruta completa del archivo en la sesión
            session['file_path'] = file_path
            
            return redirect(url_for('ask_question_route'))
        else:
            flash('Extensión de archivo no permitida.')
            return redirect(request.url)
    return render_template('upload.html')