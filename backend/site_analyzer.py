"""Analyze target sites and produce URLs to scrape."""

import urllib.robotparser
from urllib.parse import urljoin


def analyze_site(base_url: str) -> list[str]:
    """Return a list of allowed URLs based on robots.txt."""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(base_url, "robots.txt"))
    rp.read()

    if not rp.can_fetch("*", base_url):
        raise ValueError("Scraping disallowed by robots.txt")

    return [base_url]
