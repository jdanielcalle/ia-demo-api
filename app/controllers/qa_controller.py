from flask import request, render_template
import torch
from transformers import pipeline
from app.services import file_service

# Descargar y cargar el modelo de pregunta-respuesta
question_answerer = pipeline("question-answering")

def ask_question(file_path):

    question = request.form['question']

    context = file_service.extract_text(file_path)
    
    answer = question_answerer(question=question, context=context)

    return render_template('index.html', question=question, answer=answer['answer'])