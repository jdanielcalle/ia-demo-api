from app.utils import pdf_utils, word_utils, pptx_utils, html_utils

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return pdf_utils.extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return word_utils.extract_text_from_word(file_path)
    elif file_path.endswith('.pptx'):
        return pptx_utils.extract_text_from_pptx(file_path)
    elif file_path.endswith('.html') or file_path.endswith('.htm'):
        return html_utils.extract_text_from_html(file_path)
    else:
        return "Unsupported file format"