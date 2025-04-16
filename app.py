from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
    datos_filtrados = []

    if response.status_code == 200:
        lineas = response.text.strip().split("\n")
        for linea in lineas:
            partes = linea.split("|")
            if len(partes) == 4:
                cedula = partes[0].strip()
                if cedula.startswith(('3', '4', '5', '7')):
                    datos_filtrados.append({
                        "cedula": partes[0].strip(),
                        "nombre": partes[1].strip(),
                        "apellido": partes[2].strip(),
                        "email": partes[3].strip()
                    })

    html = """
    <!doctype html>
    <html>
    <head><title>Personas filtradas</title></head>
    <body>
        <h2>Personas con cédulas que inician en 3, 4, 5 o 7</h2>
        <table border="1" cellpadding="5">
            <tr>
                <th>Cédula</th><th>Nombre</th><th>Apellido</th><th>Email</th>
            </tr>
            {% for persona in personas %}
            <tr>
                <td>{{ persona.cedula }}</td>
                <td>{{ persona.nombre }}</td>
                <td>{{ persona.apellido }}</td>
                <td>{{ persona.email }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, personas=datos_filtrados)

if __name__ == "__main__":
    app.run(debug=True)
