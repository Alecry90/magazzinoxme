PERCORSO = "data/products.csv"
# imposto il percorso da seguire 

def leggi_prodotti():
    prodotti =[]

    try:
        with open(PERCORSO, "r", encoding="utf-8") as f:
            righe = f.readlines()

        for riga in righe[1:]:
            riga = riga.strip()

            if not riga:
                continue

            parti = riga.split(",")

            prodotti.append({
                "id": int(parti[0]),
                "nome":  
            })