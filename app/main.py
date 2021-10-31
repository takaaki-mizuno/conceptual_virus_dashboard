from bootstrap.create_app import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app',
                host="127.0.0.1",
                port=8010,
                reload=True,
                debug=True)
