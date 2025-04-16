from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    
    
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
   

    personas = []

    for linea in response.splitlines():
        partes = linea.split("|")
        if len(partes) == 4:
            cedula = partes[0].strip()
            if cedula.startswith(('3', '4', '5', '7')):
                personas.append(partes)

    if not personas:
        return "<p>No se encontraron personas con cédulas que comiencen en 3, 4, 5 o 7.</p>"

    html = """
    <h2>Personas filtradas</h2>
    <table border="1" cellpadding="5">
        <tr><th>Cédula</th><th>Nombre</th><th>Apellido</th><th>Email</th></tr>
    """

    for p in personas:
        html += f"<tr><td>{p[0].strip()}</td><td>{p[1].strip()}</td><td>{p[2].strip()}</td><td>{p[3].strip()}</td></tr>"

    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
