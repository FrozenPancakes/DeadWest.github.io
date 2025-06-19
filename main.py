from js import document, window
from pyodide.ffi import create_proxy

def start_logger():
    console = document.getElementById("console")

    def log_key(event):
        key = event.key
        if key == "Enter":
            console.innerHTML += "🚀 Enter key pressed!\n"
        else:
            console.innerHTML += f"Key pressed: {key}\n"
        console.scrollTop = console.scrollHeight

    proxy = create_proxy(log_key)
    window.addEventListener("keydown", proxy)