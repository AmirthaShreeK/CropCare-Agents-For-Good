# CropCare-Agents-For-Good
Sequential multi-agent LLM system that analyzes PlantVillage leaf images to identify the crop, detect symptoms, classify plant diseases, and recommend treatments. Uses Gemini Flash multimodal reasoning with sequential orchestration, handling color, grayscale, and segmented images.
This is the official submission for the **Google AI Agents for Good Hackathon**.

---

## 🚀 Features

| Agent | Role |
|------|------|
| Vision Agent | Analyzes leaf images and predicts symptoms |
| Symptom Agent | Extracts key symptoms from farmer’s input text |
| Disease Agent | Determines the most probable crop disease |
| Treatment Agent | Suggests actionable treatment and prevention steps |
| Orchestrator | Coordinates all agents into one unified pipeline |

---

## 🧠 Architecture
Detailed diagrams are available in:  
📄 `docs/architecture.md`

---

## 📂 Repository Structure

```

cropcare-agents/
│
├── notebooks/
│   └── CropCare_Agents_For_Good.ipynb    <-- MAIN NOTEBOOK 
│
├── images/
│   └── sample_inputs/                    <-- few sample PlantVillage images
│
├── src/
│   ├── orchestrator.py                   <-- Full pipeline orchestrator
│   ├── vision_agent.py                   <-- Vision Agent code
│   ├── symptom_agent.py                  <-- Symptom Agent code
│   ├── disease_agent.py                  <-- Disease Agent code
│   ├── treatment_agent.py                <-- Treatment Agent code
│   └── utils.py                          <-- JSON cleaning, logging, helpers
│
├── docs/
│   ├── architecture.md                   <-- Agent architecture diagrams + explanation
│   
│
├── .gitignore                            <-- Prevents unwanted files in repo
├── LICENSE                               <-- MIT license or Apache 2.0
├── README.md                             <-- How to run + project description
└── requirements.txt                      <-- Dependencies for local execution

````

---

## 🛠 Setup Instructions (Local)

### 1️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Notebook

Open:

```
notebooks/CropCare_Agents_For_Good.ipynb
```

➡️ Upload a plant leaf image from `images/sample_inputs/`
➡️ Run all cells

---

## 📝 Input Format

| Input         | Type                        |
| ------------- | --------------------------- |
| Crop image    | JPG/PNG (Leaf)              |


---

## 🎯 Output Includes

✔ Extracted symptoms (from image + text)
✔ Top probable crop diseases
✔ Possible symptoms
✔ Validated treatment recommendations


---

## 📌 Tech Stack

* Python
* OpenAI Agents / LLM-powered services
* PlantVillage dataset (for testing)

---



---

## 📜 License

MIT License – Free for research and educational use.

---

🌾 *Empowering farmers with accessible AI crop healthcare.*

```

