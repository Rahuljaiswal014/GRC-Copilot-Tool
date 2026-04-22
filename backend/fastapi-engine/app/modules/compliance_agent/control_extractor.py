import re
from typing import List, Dict
from loguru import logger

class ControlExtractor:
    """Extracts security/privacy controls from text using keywords and patterns."""

    KEYWORDS = ["shall", "must", "should", "ensure", "implement", "control", "policy"]

    def extract(self, text: str) -> List[Dict]:
        logger.info("Extracting controls from text")
        sentences = re.split(r'[.!?\n]', text)
        extracted_controls = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            # Basic keyword-based extraction
            if any(keyword in sentence.lower() for keyword in self.KEYWORDS):
                extracted_controls.append({
                    "id": f"CTRL-{len(extracted_controls) + 1}",
                    "text": sentence,
                    "confidence": 0.8 # Mock confidence score
                })
        
        return extracted_controls

control_extractor = ControlExtractor()
