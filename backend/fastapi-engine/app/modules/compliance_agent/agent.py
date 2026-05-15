from .policy_parser import policy_parser
from .control_extractor import control_extractor
from .control_mapper import control_mapper
from .gap_analysis import gap_analysis
from .risk_engine import risk_engine
from .recommendation_engine import recommendation_engine
from loguru import logger
from datetime import datetime

class ComplianceMappingAgent:
    """The main agent that orchestrates the entire compliance mapping process."""

    async def run_assessment(self, file_content: bytes, filename: str):
        logger.info(f"Compliance Mapping Agent started for {filename}")
        
        # 1. Parse policy text
        policy_text = policy_parser.parse(file_content, filename)
        
        # 2. Extract controls
        extracted_controls = control_extractor.extract(policy_text)
        
        # 3. Map controls to frameworks
        mapped_controls = control_mapper.map_to_frameworks(extracted_controls)
        
        # 4. Perform gap analysis
        gaps = gap_analysis.perform_gap_analysis(mapped_controls)
        
        # 5. Identify risks
        risks = risk_engine.identify_risks(gaps)
        
        # 6. Generate recommendations
        recommendations = recommendation_engine.generate_recommendations(gaps)
        
        # Calculate some stats
        total_controls = len(extracted_controls)
        mapped_count = sum(1 for c in mapped_controls if c.get("mappings"))
        
        return {
            "metadata": {
                "filename": filename,
                "timestamp": datetime.utcnow().isoformat(),
                "total_controls_found": total_controls,
                "mapped_controls_count": mapped_count,
                "unmapped_controls_count": total_controls - mapped_count,
                "total_gaps": len(gaps),
                "total_risks": len(risks)
            },
            "controls_found": extracted_controls,
            "mapped_controls": mapped_controls,
            "gaps": gaps,
            "risks": risks,
            "recommendations": recommendations,
            "status": "complete"
        }

agent = ComplianceMappingAgent()
