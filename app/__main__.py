import uvicorn


uvicorn.run(
    "main:app",
    reload=True,
    port=7500,
)
