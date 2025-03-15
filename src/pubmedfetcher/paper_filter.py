from typing import List
from Bio import Medline

COMPANY_KEYWORDS = ["pharma", "biotech", "inc.", "ltd.", "corporation", "gmbh", "s.a.", "co.", "technologies"]

def is_company(affiliation: str) -> bool:
    """Determine if an affiliation belongs to a non-academic company."""
    affiliation_lower = affiliation.lower()
    return any(keyword in affiliation_lower for keyword in COMPANY_KEYWORDS)

def filter_papers(records: List[Medline.Record]) -> List[dict]:
    """Filter papers to include only those with non-academic authors."""
    filtered_records = []
    
    for record in records:
        authors = record.get("AU", [])
        affiliations = record.get("AD", [])
        non_academic_authors = []
        company_affiliations = []
        corresponding_author_email = None

        for i, author in enumerate(authors):
            if i < len(affiliations):
                affiliation = affiliations[i]
                if is_company(affiliation):
                    non_academic_authors.append(author)
                    company_affiliations.append(affiliation)
        
        # Try extracting email (if available in AD field)
        email = None
        for aff in affiliations:
            if "@" in aff:
                email = aff.split()[-1]  # Extract last word (email)
                break

        if non_academic_authors:
            filtered_records.append({
                "PubmedID": record.get("PMID", ""),
                "Title": record.get("TI", ""),
                "Publication Date": record.get("DP", ""),
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": email or "",
            })

    return filtered_records
