from pypdf import PdfReader
import io

def read_pdf(file_path_or_buffer):
    """
    Reads text from a PDF file path or a file-like object.
    """
    try:
        reader = PdfReader(file_path_or_buffer)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

if __name__ == "__main__":
    # Test with a dummy file if it existed
    pass
