from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse, FileResponse
import shutil
import os
from faster_whisper import WhisperModel

app = FastAPI()

print("Loading Whisper model onto the RTX 4060...")
model = WhisperModel("large-v3", device="cuda", compute_type="float16")
print("Engine ready.")

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# NEW: Route to serve your local Sonic music file
@app.get("/Sonic5.mp3")
async def serve_audio():
    if os.path.exists("Sonic5.mp3"):
        return FileResponse("Sonic5.mp3", media_type="audio/mpeg")
    return HTMLResponse(status_code=404, content="Music file not found")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...), language: str = Form(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    lang_code = "ar" if language == "darija" else (None if language == "auto" else language)
    prompt = "هذا تسجيل بالدارجة المغربية. بغيت نكتب هاد الشي اللي كيتقال." if language == "darija" else None
    
    segments, _ = model.transcribe(
        temp_path,
        beam_size=5,
        language=lang_code,
        initial_prompt=prompt,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500, speech_pad_ms=400)
    )
    
    full_text = " ".join([segment.text.strip() for segment in segments])
    os.remove(temp_path)
    return {"text": full_text}