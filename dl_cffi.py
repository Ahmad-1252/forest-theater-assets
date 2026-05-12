from curl_cffi import requests

urls = [
    ("https://images.unsplash.com/photo-1518834107812-67b0b7c58434?q=80&w=600&auto=format&fit=crop", "chicago.png"),
    ("https://images.unsplash.com/photo-1470229722913-7c090be5c520?q=80&w=600&auto=format&fit=crop", "outsiders.png"),
    ("https://images.unsplash.com/photo-1503095396549-807759245b35?q=80&w=600&auto=format&fit=crop", "notebook.png"),
    ("https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=600&auto=format&fit=crop", "mamma_mia.png"),
    ("https://images.unsplash.com/photo-1465847899084-d164df4dedc6?q=80&w=600&auto=format&fit=crop", "mincemeat.png"),
    ("https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=600&auto=format&fit=crop", "mormon.png")
]

for url, filename in urls:
    response = requests.get(url, impersonate="chrome110")
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed {filename} with status {response.status_code}")
