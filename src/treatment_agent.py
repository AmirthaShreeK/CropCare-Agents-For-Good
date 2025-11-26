# Treatment Agent: recommends cure/prevention steps
def give_treatment(crop_name, disease_name):
    prompt = f"""
You are an agricultural expert.
Provide treatment for {crop_name} affected by {disease_name}.
Return JSON: {{"treatment_steps": ["..."], "safety_precautions": ["..."]}}
"""
    model = genai.GenerativeModel(MODEL)
    result = model.generate_content([prompt])
    return safe_json_parse(result.text)
