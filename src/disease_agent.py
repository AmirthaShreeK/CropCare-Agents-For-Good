# Disease Agent: decides final disease prediction using combined features

def diagnose_disease(crop_name, symptoms):
    classes_list = "\n".join(PLANTVILLAGE_CLASSES)
    prompt = f"""
You are an agricultural disease expert.
Crop: {crop_name}
Symptoms: {symptoms}
Diagnose ONLY from this PlantVillage list:
{classes_list}
Return JSON:
{{"disease_name":"...", "reasoning":"...", "confidence":"..." }}
"""
    model = genai.GenerativeModel(MODEL)
    result = model.generate_content([prompt])
    return safe_json_parse(result.text)
