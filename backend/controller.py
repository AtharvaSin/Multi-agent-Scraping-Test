"""Main controller that orchestrates the scraping workflow."""

from .nlp_agent import parse_instruction
from .site_analyzer import analyze_site
from .scraper import scrape_pages
from .data_normalizer import normalize_data
from .storage_manager import store_items


def run_job(prompt: str) -> tuple[int, list[dict]]:
    task = parse_instruction(prompt)
    urls = analyze_site(task["target"])
    raw_items = scrape_pages(urls, task)
    cleaned_items = [normalize_data(item) for item in raw_items]
    store_items(cleaned_items)
    return len(cleaned_items), cleaned_items
