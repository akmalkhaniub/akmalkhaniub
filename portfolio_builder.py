"""
Developer Portfolio Showcase Aggregator & JSON-LD Schema Generator for akmalkhaniub
Builds structured Schema.org metadata for portfolio SEO optimization.
"""
import json
from typing import Dict, Any, List

class PortfolioBuilderEngine:
    """Generates structured SEO Schema.org Person & CreativeWork metadata."""

    @staticmethod
    def generate_person_schema(
        name: str,
        role: str,
        github_url: str,
        skills: List[str]
    ) -> Dict[str, Any]:
        """Build Schema.org Person JSON-LD object."""
        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": name,
            "jobTitle": role,
            "sameAs": [github_url],
            "knowsAbout": skills
        }

    @staticmethod
    def generate_project_schema(
        title: str,
        description: str,
        tech_stack: List[str],
        repo_url: str
    ) -> Dict[str, Any]:
        """Build Schema.org SoftwareSourceCode JSON-LD object."""
        return {
            "@context": "https://schema.org",
            "@type": "SoftwareSourceCode",
            "name": title,
            "description": description,
            "programmingLanguage": tech_stack,
            "codeRepository": repo_url
        }

    @staticmethod
    def export_schema_html_script(schema_obj: Dict[str, Any]) -> str:
        """Embed schema JSON-LD inside HTML script tag."""
        return f'<script type="application/ld+json">\n{json.dumps(schema_obj, indent=2)}\n</script>'
