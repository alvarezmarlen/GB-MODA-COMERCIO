from app.app import create_app

# Llamamos a la función constructora que tiene toda la configuración del equipo
app = create_app()

if __name__ == "__main__":
    # Arrancamos el servidor
    app.run(host="0.0.0.0", port=5000, debug=True)
