from js import document, window

console = document.getElementById("console")

def log_key(event):
    key = event.key
    console.innerHTML += f"Key pressed: {key}\n"
    console.scrollTop = console.scrollHeight

# Attach the listener
window.addEventListener("keydown", log_key)