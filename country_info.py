import requests

def get_country_info(name):
    try:
        url = f"https://restcountries.com/v3.1/name/{name}"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()[0]

        return {
            "name": data.get("name", {}).get("common", name),
            "official_name": data.get("name", {}).get("official", "N/A"),
            "capital": data.get("capital", ["N/A"])[0],
            "population": data.get("population", "N/A"),
            "currency": list(data.get("currencies", {}).keys())[0],
            "language": ', '.join(data.get("languages", {}).values()),
            "region": data.get("region", "N/A")
        }

    except Exception as e:
        return {"error": f"Unable to fetch info for '{name}': {e}"}
