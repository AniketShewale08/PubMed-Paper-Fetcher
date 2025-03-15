from typing import List
from Bio import Entrez, Medline

def fetch_papers(query: str) -> List[Medline.Record]:
    """Fetch papers based on the query."""
    try:
        handle = Entrez.esearch(db="pubmed", rettype="medline", retmode="text", term=query)
        record = Entrez.read(handle)
        ids = record.get("IdList", [])
        
        if not ids:
            print("No papers found for the given query.")
            return []
        
        handle = Entrez.efetch(db="pubmed", rettype="medline", retmode="text", id=ids)
        records = Medline.parse(handle)
        return list(records)

    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []
