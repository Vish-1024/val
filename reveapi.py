import requests
import base64
import os
import time
import sys


# ────────────────────────────────────────────────
#          CHANGE THESE PATHS AS NEEDED
# ────────────────────────────────────────────────
IMAGE_1_PATH = r"C:\Users\raisu\Downloads\Telegram Desktop\photo_2026-02-14_16-51-46.jpg"
IMAGE_2_PATH = r"C:\Users\raisu\Pictures\Screenshots\Screenshot 2026-02-14 165304.png"

OUTPUT_FILENAME = "output.jpg"
# ────────────────────────────────────────────────

ENDPOINT = "https://api.reve.com/v1/image/remix"

REVE_API_KEY = "papi.8ae7bb40-057e-4e39-836d-847bac6803d0.beZQv3CB3RLaOyYnvkT_OcOjOtcHh36i"


def file_to_base64(filepath: str) -> str:
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Image not found: {filepath}")
    
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main():
    print("Starting outfit remix script...\n")
    print(f"Image 1 (base person) : {IMAGE_1_PATH}")
    print(f"Image 2 (dress source) : {IMAGE_2_PATH}")
    print("-" * 60)

    try:
        # Convert images to base64
        print("Reading and encoding images...")
        base64_img1 = file_to_base64(IMAGE_1_PATH)
        base64_img2 = file_to_base64(IMAGE_2_PATH)
        print("Images encoded successfully.")

        reference_images = [base64_img1, base64_img2]

        headers = {
            "Authorization": f"Bearer {REVE_API_KEY}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        prompt = """Create a realistic full-body portrait by combining two reference images.
Instructions:

* Use Image 1 as the base model (face, body proportions, hairstyle, identity).

* Replace her outfit with the dress from Image 2, ensuring accurate fabric texture, fit, color, and structural details.

* Generate a full-body portrait, centered and fully visible from head to toe.

* Pose: standing upright, arms gently held together above the abdomen (hands softly clasped or overlapping), relaxed shoulders, natural posture.

* Background: elegant grey curtains covering the backdrop.

* Floor: natural wooden flooring with realistic texture and perspective.

* Lighting: soft, studio-style lighting with subtle shadows, evenly illuminating the subject.

* Style: photorealistic, high detail, sharp focus, natural skin tones.

* Composition: vertical portrait orientation, balanced framing, professional fashion photography look."""

        payload = {
            "prompt": prompt,
            "reference_images": reference_images,
            "version": "latest-fast"
            # Optional: "aspect_ratio": "2:3" or "9:16" for taller portrait
        }

        print("\nSending request to Reve API...")
        start_time = time.time()

        response = requests.post(ENDPOINT, headers=headers, json=payload, timeout=90)
        response.raise_for_status()

        end_time = time.time()
        duration = end_time - start_time

        result = response.json()

        image_b64 = result.get("image")
        credits_used = result.get("credits_used")
        credits_remaining = result.get("credits_remaining")

        if not image_b64:
            raise ValueError("No image data returned from API")

        # Save the image
        img_bytes = base64.b64decode(image_b64)
        with open(OUTPUT_FILENAME, "wb") as f:
            f.write(img_bytes)

        print("\n" + "="*70)
        print("SUCCESS!")
        print(f"Image saved as: {os.path.abspath(OUTPUT_FILENAME)}")
        print(f"Time taken: {duration:.2f} seconds")
        print(f"Credits used: {credits_used}")
        print(f"Credits remaining: {credits_remaining}")
        print("="*70)

    except FileNotFoundError as e:
        print("\nERROR: File not found")
        print(e)
        sys.exit(1)
    except requests.RequestException as e:
        print("\nERROR: Failed to contact Reve API")
        print(e)
        if hasattr(e.response, 'text'):
            print("Response content:", e.response.text)
        sys.exit(1)
    except Exception as e:
        print("\nUNEXPECTED ERROR:")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()