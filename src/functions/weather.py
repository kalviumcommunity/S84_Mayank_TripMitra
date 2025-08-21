def get_weather(destination: str, month: str) -> str:
    seasonal = {
        "bali": {"best":"Apr–Oct", "note":"Dry season; warm & sunny."},
        "jaipur": {"best":"Oct–Mar", "note":"Pleasant winters; hot summers."},
        "paris": {"best":"Apr–Jun & Sep–Nov", "note":"Mild; occasional rain."}
    }
    info = seasonal.get(destination.lower(), {"best":"Varies", "note":"Check local forecast closer to travel dates."})
    return f"Best time: {info['best']}. {info['note']}"
