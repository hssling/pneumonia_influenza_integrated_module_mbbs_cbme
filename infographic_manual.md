# Infographic Manual on Community Medicine

**Author: AI Content Creator Matrix**  
**Framework: Competency-Based Medical Education (CBME)**  
**Generated: 2025**

This manual provides visual infographics summarizing key concepts in community medicine, aligned with the CBME competencies. Each infographic is presented as a Mermaid diagram code, which can be rendered into SVG images using Mermaid CLI or online tools.

## 1. Levels of Prevention

The levels of prevention in public health illustrate the hierarchy from primordial to tertiary prevention.

![Levels of Prevention](diagrams/levels_prevention.svg)

```mermaid
graph TD
A[Primordial Prevention] --> B[Primary Prevention]
B --> C[Secondary Prevention]
C --> D[Tertiary Prevention]
```

## 2. Epidemiological Triangle

The epidemiological triangle shows the interaction between agent, host, and environment in disease causation.

![Epidemiological Triangle](diagrams/epidemiological_triangle.svg)

```mermaid
graph TD
A[Agent] --> C[Disease]
B[Host] --> C
D[Environment] --> C
```

## 3. Health System Organization in India

The structure of the health system in India from central to village level.

![Health System Organization in India](diagrams/health_system_india.svg)

```mermaid
graph TD
A[Ministry of Health & Family Welfare] --> B[Central Government]
B --> C[State Governments]
C --> D[District Level]
D --> E[Block Level]
E --> F[Village Level]
```

## 4. Maternal and Child Health Cycle

The continuum of care in maternal and child health.

![Maternal and Child Health Cycle](diagrams/maternal_child_health_cycle.svg)

```mermaid
graph LR
A[Pregnancy] --> B[Antenatal Care]
B --> C[Delivery]
C --> D[Postnatal Care]
D --> E[Child Health]
E --> F[Immunization]
F --> G[Growth Monitoring]
```

## 5. WASH Framework

Water, Sanitation, and Hygiene (WASH) components and their impact on health.

![WASH Framework](diagrams/wash_framework.svg)

```mermaid
graph TD
A[Water] --> D[WASH]
B[Sanitation] --> D
C[Hygiene] --> D
D --> E[Health Outcomes]
```

## 6. Nutrition Surveillance Indicators

Types of indicators used in nutrition surveillance.

![Nutrition Surveillance Indicators](diagrams/nutrition_indicators.svg)

```mermaid
graph TD
A[Anthropometric] --> F[Nutrition Indicators]
B[Biochemical] --> F
C[Clinical] --> F
D[Dietary] --> F
E[Ecological] --> F
```

## 7. Study Designs in Epidemiology

Classification of epidemiological study designs.

![Study Designs in Epidemiology](diagrams/study_designs_epidemiology.svg)

```mermaid
graph TD
A[Observational] --> B[Descriptive]
A --> C[Analytical]
C --> D[Cohort]
C --> E[Case-Control]
C --> F[Cross-Sectional]
G[Experimental] --> H[Randomized Controlled Trial]
G --> I[Field Trial]
```

## 8. Occupational Hazards

Types of hazards in occupational health.

![Occupational Hazards](diagrams/occupational_hazards.svg)

```mermaid
graph TD
A[Physical Hazards] --> F[Workplace Hazards]
B[Chemical Hazards] --> F
C[Biological Hazards] --> F
D[Ergonomic Hazards] --> F
E[Psychosocial Hazards] --> F
```

## 9. Environmental Health Risks

Major environmental health risks.

![Environmental Health Risks](diagrams/environmental_health_risks.svg)

```mermaid
graph TD
A[Air Pollution] --> F[Environmental Risks]
B[Water Contamination] --> F
C[Soil Pollution] --> F
D[Noise Pollution] --> F
E[Climate Change] --> F
```

## 10. Research Methodology Steps

Steps in conducting community-based research.

![Research Methodology Steps](diagrams/research_methodology_steps.svg)

```mermaid
graph LR
A[Identify Problem] --> B[Review Literature]
B --> C[Formulate Hypothesis]
C --> D[Design Study]
D --> E[Collect Data]
E --> F[Analyze Data]
F --> G[Interpret Results]
G --> H[Draw Conclusions]
```

## 11. Health Policy Cycle

The process of health policy development and implementation.

![Health Policy Cycle](diagrams/health_policy_cycle.svg)

```mermaid
graph LR
A[Problem Identification] --> B[Policy Formulation]
B --> C[Policy Adoption]
C --> D[Policy Implementation]
D --> E[Policy Evaluation]
E --> F[Policy Modification]
```

## 12. Disaster Response Phases

Phases of disaster management.

![Disaster Response Phases](diagrams/disaster_response_phases.svg)

```mermaid
graph LR
A[Prevention] --> B[Preparedness]
B --> C[Response]
C --> D[Recovery]
D --> E[Mitigation]
```

## How to Generate SVGs

To render these diagrams into SVG images:

1. Install Mermaid CLI: `npm install -g @mermaid-js/mermaid-cli`
2. Run: `mmdc -i diagram.mmd -o diagram.svg`

Or use online tools like https://mermaid.live/

## Conclusion

These infographics provide a quick visual reference for key concepts in community medicine. They are designed to aid in teaching and learning within the CBME framework.
