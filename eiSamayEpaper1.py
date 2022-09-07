from pathlib import Path
import requests
filename = Path('metadata.pdf')
url = 'https://www.epaper.eisamay.com/epaperimages/07092022/07092022-md-em-1.pdf'
response = requests.get(url)
filename.write_bytes(response.content)