from app import create_app

def _main():
    app = create_app()
    app.config["DEBUG"] = True
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    _main()