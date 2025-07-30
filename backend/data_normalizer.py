"""Utility functions to clean and normalize scraped data."""


def normalize_data(item: dict) -> dict:
    cleaned = {}
    for key, value in item.items():
        if key == "price" and value:
            cleaned[key] = float(str(value).replace("$", "").replace(",", ""))
        elif isinstance(value, str):
            cleaned[key] = value.strip()
        else:
            cleaned[key] = value
    return cleaned
