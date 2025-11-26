# Orchestrator Agent
# This file manages workflow across all agents


def orchestrate_pipeline(image_path):
    # Step 1: Detect crop
    crop_info = detect_crop_with_llm(image_path)
    if crop_info is None:
        return {"error": "Failed to detect crop"}

    crop_name = crop_info["crop"]

    # Step 2: Describe symptoms
    symptoms = describe_symptoms(crop_name, image_path)

    # Step 3: Diagnose disease
    disease_info = diagnose_disease(crop_name, symptoms)
    if disease_info is None:
        disease_info = {"disease_name": "Unknown", "reasoning": "Failed LLM diagnosis", "confidence": "low"}

    # Step 4: Provide treatment
    disease_name = disease_info.get("disease_name", "Unknown")
    treatment_info = give_treatment(crop_name, disease_name)
    if treatment_info is None:
        treatment_info = {"treatment_steps": [], "safety_precautions": []}

    # Merge final result
    return {
        "crop_info": crop_info,
        "symptoms": symptoms,
        "disease_info": disease_info,
        "treatment_info": treatment_info
    }
