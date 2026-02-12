import time
import pyperclip
import uuid
from core import add_clip

def main():
    print("📋 Semantic Clipboard Listener started...")
    last_clip = ""

    try:
        while True:
            # Get current clipboard content
            current_clip = pyperclip.paste().strip()

            # If it's new and not empty, save it
            if current_clip and current_clip != last_clip:
                clip_id = str(uuid.uuid4())
                add_clip(current_clip, clip_id)
                print(f"✅ Saved new clip: {current_clip[:50]}...")
                last_clip = current_clip
            
            # Check every 2 seconds to save CPU
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()