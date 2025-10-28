from flask import Flask, request, send_file, render_template, flash, redirect
import pdfplumber
import subprocess
import os
import uuid
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change for production
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        if 'pdf' not in request.files:
            flash('No file uploaded')
            return redirect('/')
        
        pdf_file = request.files['pdf']
        voice = request.form.get('voice', 'default')
        
        if pdf_file.filename == '':
            flash('No file selected')
            return redirect('/')
        
        # Save PDF
        pdf_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + '.pdf')
        pdf_file.save(pdf_path)
        
        # Extract text
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        
        if not text.strip():
            flash('No text found in PDF')
            os.remove(pdf_path)
            return redirect('/')
        
        # Generate TTS audio via subprocess
        audio_path = os.path.join(AUDIO_FOLDER, str(uuid.uuid4()) + '.mp3')
        subprocess.run(['python', 'tts_script.py', text, audio_path, voice], check=True)
        
        # Check if audio file was created
        if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
            flash('Audio generation failed')
            os.remove(pdf_path)
            return redirect('/')
        
        # Clean up PDF
        os.remove(pdf_path)
        
        return send_file(audio_path, as_attachment=True, download_name='audiobook.mp3')
    
    except Exception as e:
        logging.error(f"Error during conversion: {str(e)}")
        flash(f'An error occurred: {str(e)}')
        return redirect('/')

if __name__ == '__main__':
    app.run()  # No debug=True to avoid threading issues