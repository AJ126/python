
from PyPDF2 import PdfReader
import pyttsx3

def pdf_to_audio(pdf_path, audio_path):
    reader = PdfReader(pdf_path)
    speaker = pyttsx3.init()

    # Extract text from all PDF pages
    text = "\n".join(
        page.extract_text() or ""
        for page in reader.pages
    )

    if not text.strip():
        print("No extractable text found in the PDF.")
        return

    # Save all text as an audio file
    speaker.save_to_file(text, audio_path)
    speaker.runAndWait()
    speaker.stop()

    print(f"Audio saved successfully: {audio_path}")


pdf_to_audio("Notes/Python_DS.pdf", "audio.mp3")
