from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from model.note import Note
from fastapi.staticfiles import StaticFiles
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def add_note(
    title: str = Form(...),
    desc: str = Form(...),
    important: bool = Form(False)
):
    # Create note data from form
    note_data = {
        "title": title,
        "desc": desc,
        "important": important
    }
    
    # Insert into MongoDB
    inserted_note = conn.notes.notes.insert_one(note_data)
    
    # Redirect back to home page to show the updated list
    return RedirectResponse(url="/", status_code=303)