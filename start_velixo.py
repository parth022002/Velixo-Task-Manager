import os
import sys
import subprocess
import time
import webbrowser

def main():
    print("=" * 60)
    print("[START] VELIXO: AI Work Operating System (AI Chief of Staff)")
    print("=" * 60)
    print("Tagline: Your AI Chief of Staff for Work and Life.")
    print("Mode:    Zero-Cost Multi-Provider AI Engine (Groq / Gemini / OpenRouter)")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(base_dir, "backend")
    client_dir = os.path.join(base_dir, "client")

    print("\n[1/2] Starting FastAPI Velixo AI Engine Backend on http://localhost:8000...")
    backend_cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    backend_proc = subprocess.Popen(backend_cmd, cwd=backend_dir)

    print("\n[2/2] Starting Velixo React Dashboard on http://localhost:5173...")
    client_cmd = "npx vite"
    client_proc = subprocess.Popen(client_cmd, cwd=client_dir, shell=True)

    time.sleep(3)
    print("\n" + "=" * 60)
    print("[SUCCESS] Velixo is live!")
    print("   -> Dashboard: http://localhost:5173")
    print("   -> API Docs:  http://localhost:8000/docs")
    print("=" * 60 + "\n")

    try:
        webbrowser.open("http://localhost:5173")
        backend_proc.wait()
        client_proc.wait()
    except KeyboardInterrupt:
        print("\nShutting down Velixo services...")
        backend_proc.terminate()
        client_proc.terminate()

if __name__ == "__main__":
    main()
