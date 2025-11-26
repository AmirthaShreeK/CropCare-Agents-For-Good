# Symptom Agent: takes symptom text input & validates

def describe_symptoms(crop_name, image_path):
    img = Image.open(image_path)
    prompt = f"""
You are an agricultural expert.
Describe the symptoms visible on the {crop_name} leaf.
Return text only.
"""
    model = genai.GenerativeModel(MODEL)
    result = model.generate_content([prompt, img])
    return result.text.strip()
