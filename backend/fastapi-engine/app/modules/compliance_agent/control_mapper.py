from typing import List, Dict
from loguru import logger

class ControlMapper:
    """Maps extracted controls to ISO 27001, GDPR, and SOC 2 frameworks."""

    FRAMEWORKS = {
        "ISO 27001": [
            {"id": "A.9.1.1", "text": "Access control policy", "keywords": ["access", "control", "policy"]},
            {"id": "A.9.4.2", "text": "Secure log-on procedures", "keywords": ["log-on", "secure", "password"]},
            {"id": "A.12.3.1", "text": "Information backup", "keywords": ["backup", "data"]},
        ],
        "GDPR": [
            {"id": "Art 32", "text": "Security of processing", "keywords": ["processing", "security", "personal data"]},
            {"id": "Art 25", "text": "Data protection by design", "keywords": ["protection", "design", "privacy"]},
        ],
        "SOC 2": [
            {"id": "CC6.1", "text": "Logical Access Security", "keywords": ["access", "logical", "security"]},
            {"id": "CC7.1", "text": "System Operations Monitoring", "keywords": ["monitoring", "operations", "system"]},
        ]
    }

    def map_to_frameworks(self, extracted_controls: List[Dict]) -> List[Dict]:
        logger.info("Mapping extracted controls to frameworks")
        mapped_results = []
        
        for control in extracted_controls:
            mappings = []
            control_text_lower = control["text"].lower()
            
            for framework, requirements in self.FRAMEWORKS.items():
                for req in requirements:
                    if any(keyword in control_text_lower for keyword in req["keywords"]):
                        mappings.append({
                            "framework": framework,
                            "control_id": req["id"],
                            "requirement_text": req["text"]
                        })
            
            mapped_results.append({
                **control,
                "mappings": mappings
            })
            
        return mapped_results

control_mapper = ControlMapper()
