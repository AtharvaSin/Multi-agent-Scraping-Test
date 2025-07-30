"""Scraper agent for fetching and parsing pages."""

import requests
from bs4 import BeautifulSoup


def scrape_pages(urls: list[str], task: dict) -> list[dict]:
    items: list[dict] = []
    for url in urls:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        item = {field: extract_field(soup, field) for field in task.get("fields", [])}
        items.append(item)
    return items


def extract_field(soup: BeautifulSoup, field: str):
    if field == "title":
        return soup.title.string.strip() if soup.title else None
    # Add more field handlers here
    return None
