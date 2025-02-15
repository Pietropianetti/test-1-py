





import keyboard

keyboard.hook_key("d",lambda e: MOVE.baixo() if e.event_type == "down" else None)