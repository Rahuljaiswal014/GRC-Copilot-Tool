import io
from docx import Document
from loguru import logger

class PolicyParser:
    """Extracts text from various document formats (PDF, DOCX, TXT)."""

    def parse(self, file_content: bytes, filename: str) -> str:
        logger.info(f"Parsing file: {filename}")
        if filename.endswith(".txt"):
            return file_content.decode("utf-8")
        elif filename.endswith(".docx"):
            return self._parse_docx(file_content)
        elif filename.endswith(".pdf"):
            # Placeholder for PDF parsing
            logger.warning("PDF parsing is not yet fully implemented. Using mock extraction.")
            return "This is a mock text extracted from PDF. [CONTROL-1]: Ensure all passwords are encrypted."
        else:
            raise ValueError(f"Unsupported file format: {filename}")

    def _parse_docx(self, file_content: bytes) -> str:
        doc = Document(io.BytesIO(file_content))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)

policy_parser = PolicyParser()
