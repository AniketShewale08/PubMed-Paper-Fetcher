from typing import Optional
from .paper_fetcher import fetch_papers
from .paper_filter import filter_papers
import pandas as pd
from Bio import Entrez
import typer

# Set your email for Entrez
Entrez.email = 'aniketshewale26@gmail.com'

app = typer.Typer()

@app.command()
def main(
    query: str, 
    debug: bool = typer.Option(False, "--debug", "-d"),
    file: Optional[str] = typer.Option(None, "--file", "-f")
):
    """
    Fetch and filter research papers from PubMed.
    
    Args:
        query: Search query for PubMed
        debug: Enable debug mode
        file: Output CSV file path
    """
    try:
        # Debug logging
        if debug:
            typer.echo(f"Debug mode activated. Query: {query}")
        
        # Fetch papers
        records = fetch_papers(query)
        
        if debug:
            typer.echo(f"Total papers fetched: {len(records)}")
        
        # Filter papers
        filtered_records = filter_papers(records)
        
        if debug:
            typer.echo(f"Papers after filtering: {len(filtered_records)}")
        
        # Create DataFrame
        df = pd.DataFrame(filtered_records)
        
        # Output handling
        if file:
            df.to_csv(file, index=False)
            typer.echo(f"Results saved to {file}")
        else:
            print(df)
    
    except Exception as e:
        typer.echo(f"An error occurred: {e}")
        raise typer.Abort()

if __name__ == "__main__":
    app()