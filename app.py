from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from process_string import ProcessText

app = FastAPI()
process_obj = ProcessText()


@app.get("/")
async def read_root():
    """
    Return the homepage HTML file.
    """
    return FileResponse(r".\templates\homepage.html")


@app.get("/process_text/")
async def process_text(
    input_text: str = Query(title="Input Text", description="Text to process"),
    autocorrector: bool = Query(
        False, title="Autocorrector", description="Enable autocorrection"
    ),
):
    """
    Process and clean uncleaned text data.

    Args:
        input_text (str): The uncleaned text data.
        autocorrector (bool): Whether to apply spelling correction or not.

    Returns:
        JSONResponse: The cleaned text data in JSON format.
    """
    response = await process_obj.clean_text(
        uncleaned_text=input_text, auto_corrector=autocorrector
    )
    data = {"cleaned_text": response}
    return JSONResponse(content=data, status_code=200)
