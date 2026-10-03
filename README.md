# 🦔 Sonixly AI Transcriber

Sonixly is a blazing-fast, GPU-accelerated local audio transcriber built with Python, FastAPI, and OpenAI's Whisper model (`large-v3`). It features a custom "Sonic the Hedgehog" inspired Glassmorphism UI, interactive 3D WebGL animations, and seamless Right-to-Left (RTL) support for Moroccan Darija and standard Arabic.

## ✨ Features
* **Hyper-Fast Processing:** Leverages `faster-whisper` and CTranslate2 on NVIDIA GPUs.
* **Darija Optimized:** Custom prompt injection to force accurate Moroccan Darija dialect transcription.
* **Interactive 3D UI:** Custom Perlin-noise breathing blob and floating golden rings built with Vanilla Three.js.
* **Gooey Text Morphing:** Smooth, SVG-filtered text animations.
* **Local Export:** Generate high-quality PDF transcripts entirely client-side using `html2pdf.js`.

## 🚀 Hardware Requirements
* **GPU:** NVIDIA GPU with CUDA support (Optimized for RTX 4060 / 8GB VRAM).
* **OS:** Linux or Windows WSL2.

## 🛠️️ Installation & Setup

1. **Install System Dependencies (Ubuntu/WSL):**
   ```bash
   sudo apt update && sudo apt install -y ffmpeg
   
Set Up the Virtual Environment:

Bash
python3 -m venv whisper-env
source whisper-env/bin/activate
pip install fastapi uvicorn python-multipart faster-whisper
Run the Server:

Bash
uvicorn main:app
Navigate to http://localhost:8000 in your browser.


## 👤 Architect

**El Walid El Alaoui Fels**

*Computer Systems Engineering Student — ISGA Marrakech*

[LinkedIn](https://www.linkedin.com/in/el-walid-el-alaoui-fels/) | [Upwork](https://www.upwork.com/freelancers/~01f4844810b3d78bf7)
