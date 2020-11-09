import typer
import requests
import pprint

URL = "https://en.wikipedia.org/w/api.php"

"""def search(search_input: str):
	params = {
		"action": "query",
		"format": "json",
		"srsearch": search_input,
	}
	r = requests.get(URL, params = params)
	typer.echo(r.json())"""

def main(search_input: str = typer.Argument()):
	params = {
	    "action": "query",
	    "format": "json",
	    "titles": search_input.title(),
	    "explaintext": True,
	    "prop": "extracts",
	    "formatversion": 2,
	}
	r = requests.get(URL, params=params)
	typer.echo(r.json())

if __name__ == "__main__":
    typer.run(main)
