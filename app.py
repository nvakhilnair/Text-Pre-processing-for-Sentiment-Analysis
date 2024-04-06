from fastapi import FastAPI, Query

from process_string import ProcessText

from fastapi.responses import JSONResponse

from fastapi.responses import FileResponse


app = FastAPI()
process_obj = ProcessText()


@app.get("/")
async def read_root():
    return FileResponse(r".\templates\homepage.html")



@app.get("/process_text/")
async def process_text(input_text: str = Query(title="Input Text", description="Text to process"),
                       autocorrector: bool = Query(False, title="Autocorrector", description="Enable autocorrection")):
    response = await process_obj.clean_text(uncleaned_text=input_text, auto_corrector=autocorrector)
    data = {"cleaned_text": response}
    return JSONResponse(content=data, status_code=200)