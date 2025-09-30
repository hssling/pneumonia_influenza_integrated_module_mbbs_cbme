import requests

diagrams = {
    "levels_prevention": """graph TD
A[Primordial Prevention] --> B[Primary Prevention]
B --> C[Secondary Prevention]
C --> D[Tertiary Prevention]""",

    "epidemiological_triangle": """graph TD
A[Agent] --> C[Disease]
B[Host] --> C
D[Environment] --> C""",

    "health_system_india": """graph TD
A[Ministry of Health & Family Welfare] --> B[Central Government]
B --> C[State Governments]
C --> D[District Level]
D --> E[Block Level]
E --> F[Village Level]""",

    "maternal_child_health_cycle": """graph LR
A[Pregnancy] --> B[Antenatal Care]
B --> C[Delivery]
C --> D[Postnatal Care]
D --> E[Child Health]
E --> F[Immunization]
F --> G[Growth Monitoring]""",

    "wash_framework": """graph TD
A[Water] --> D[WASH]
B[Sanitation] --> D
C[Hygiene] --> D
D --> E[Health Outcomes]""",

    "nutrition_indicators": """graph TD
A[Anthropometric] --> F[Nutrition Indicators]
B[Biochemical] --> F
C[Clinical] --> F
D[Dietary] --> F
E[Ecological] --> F""",

    "study_designs_epidemiology": """graph TD
A[Observational] --> B[Descriptive]
A --> C[Analytical]
C --> D[Cohort]
C --> E[Case-Control]
C --> F[Cross-Sectional]
G[Experimental] --> H[Randomized Controlled Trial]
G --> I[Field Trial]""",

    "occupational_hazards": """graph TD
A[Physical Hazards] --> F[Workplace Hazards]
B[Chemical Hazards] --> F
C[Biological Hazards] --> F
D[Ergonomic Hazards] --> F
E[Psychosocial Hazards] --> F""",

    "environmental_health_risks": """graph TD
A[Air Pollution] --> F[Environmental Risks]
B[Water Contamination] --> F
C[Soil Pollution] --> F
D[Noise Pollution] --> F
E[Climate Change] --> F""",

    "research_methodology_steps": """graph LR
A[Identify Problem] --> B[Review Literature]
B --> C[Formulate Hypothesis]
C --> D[Design Study]
D --> E[Collect Data]
E --> F[Analyze Data]
F --> G[Interpret Results]
G --> H[Draw Conclusions]""",

    "health_policy_cycle": """graph LR
A[Problem Identification] --> B[Policy Formulation]
B --> C[Policy Adoption]
C --> D[Policy Implementation]
D --> E[Policy Evaluation]
E --> F[Policy Modification]""",

    "disaster_response_phases": """graph LR
A[Prevention] --> B[Preparedness]
B --> C[Response]
C --> D[Recovery]
D --> E[Mitigation]"""
}

for name, code in diagrams.items():
    response = requests.post("http://127.0.0.1:5008/generate", json={"code": code, "name": name})
    print(f"{name}: {response.json()}")
