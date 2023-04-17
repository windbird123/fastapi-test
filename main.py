import uvicorn

from api.api import create_app


def main():
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
    print("Hello World")


if __name__ == "__main__":
    main()
