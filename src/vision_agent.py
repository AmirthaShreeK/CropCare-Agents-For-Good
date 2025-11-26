# Vision Agent: loads model & predicts disease
def detect_crop_with_llm(image_path):
    img = Image.open(image_path)
    prompt = """
You are an agriculture expert.
Identify the crop shown in the image.
Return ONLY JSON like:
{
  "crop": "name of the crop",
  "confidence": "high / medium / low",
  "alternatives": ["possible option1", "option2"]
}
"""
    model = genai.GenerativeModel(MODEL)
    result = model.generate_content([prompt, img])
    return safe_json_parse(result.text)
