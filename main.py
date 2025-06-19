from js import document, window
from pyodide.ffi import create_proxy

console = document.getElementById("console")

def log_key(event):
    key = event.key
    if key == "Enter":
        console.innerHTML += "🚀 Enter key pressed! Launching...\n"
    else:
        console.innerHTML += f"Key pressed: {key}\n"
    console.scrollTop = console.scrollHeight

# Create a persistent proxy for the JS event listener
log_key_proxy = create_proxy(log_key)

# Attach the Python function as a JS event listener
window.addEventListener("keydown", log_key_proxy)