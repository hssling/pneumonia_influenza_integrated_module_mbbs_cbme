@echo off
echo ================================================
echo PNEUMONIA TREATMENT & IMMUNIZATION CBME MODULE
echo Compilation Script for Distribution Formats
echo Developer: Dr. Siddalingaiah H S
echo ================================================

REM Create export directory
if not exist "export" mkdir export

REM Compile all 15 chapters into single comprehensive document
echo Compiling all chapters into comprehensive book...
pandoc ^
  front_matter.md ^
  drafts/chapter1_introduction_to_pneumonia_epidemiology_and_pathophysiology_cbme.md ^
  drafts/chapter2_pneumonia_classification_community_vs_hospital_acquired_cbme.md ^
  drafts/chapter3_clinical_diagnosis_and_assessment_tools_cbme.md ^
  drafts/chapter4_radiological_diagnosis_and_imaging_cbme.md ^
  drafts/chapter5_microbiological_diagnosis_and_laboratory_tests_cbme.md ^
  drafts/chapter6_antibiotic_treatment_guidelines_and_selection_cbme.md ^
  drafts/chapter7_management_of_severe_and_complicated_pneumonia_cbme.md ^
  drafts/chapter8_non_antibiotic_supportive_care_and_adjunct_therapies_cbme.md ^
  drafts/chapter9_prevention_of_pneumonia_vaccination_strategies_cbme.md ^
  drafts/chapter10_pneumococcal_vaccination_types_and_recommendations_cbme.md ^
  drafts/chapter11_influenza_vaccination_seasonal_and_pandemic_preparedness_cbme.md ^
  drafts/chapter12_immunization_implementation_coverage_cbme.md ^
  drafts/chapter13_coverage_monitoring_and_surveillance_cbme.md ^
  drafts/chapter14_vaccine_safety_adverse_events_and_public_confidence_cbme.md ^
  drafts/chapter15_program_evaluation_and_impact_assessment_cbme.md ^
  back_matter.md ^
  --metadata title="Pneumonia Treatment & Immunization CBME Training Module" ^
  --metadata author="Dr. Siddalingaiah H S, MD, FIAHS" ^
  --metadata date="2025" ^
  --metadata publisher="Community Medicine Department - Medical Education Module" ^
  --metadata description="Comprehensive CBME-aligned training module covering pneumonia diagnosis, treatment, and prevention through immunization for medical students." ^
  --metadata subject="Medical Education, Pneumonia, Immunization, CBME" ^
  --metadata keywords="pneumonia, immunization, vaccination, medical education, CBME, pneumococcal, influenza" ^
  --toc ^
  --toc-depth=2 ^
  --number-sections ^
  --highlight-style=tango ^
  --pdf-engine=pdflatex ^
  -V geometry:margin=1in ^
  -V fontsize=11pt ^
  -V colorlinks=true ^
  -V linkcolor=blue ^
  -V urlcolor=blue ^
  -V citecolor=green ^
  -V geometry:a4paper ^
  -V titlepage=true ^
  -o export\pneumonia-treatment-immunization-cbme.pdf

echo Generating DOCX format...
pandoc ^
  front_matter.md ^
  drafts/chapter1_introduction_to_pneumonia_epidemiology_and_pathophysiology_cbme.md ^
  drafts/chapter2_pneumonia_classification_community_vs_hospital_acquired_cbme.md ^
  drafts/chapter3_clinical_diagnosis_and_assessment_tools_cbme.md ^
  drafts/chapter4_radiological_diagnosis_and_imaging_cbme.md ^
  drafts/chapter5_microbiological_diagnosis_and_laboratory_tests_cbme.md ^
  drafts/chapter6_antibiotic_treatment_guidelines_and_selection_cbme.md ^
  drafts/chapter7_management_of_severe_and_complicated_pneumonia_cbme.md ^
  drafts/chapter8_non_antibiotic_supportive_care_and_adjunct_therapies_cbme.md ^
  drafts/chapter9_prevention_of_pneumonia_vaccination_strategies_cbme.md ^
  drafts/chapter10_pneumococcal_vaccination_types_and_recommendations_cbme.md ^
  drafts/chapter11_influenza_vaccination_seasonal_and_pandemic_preparedness_cbme.md ^
  drafts/chapter12_immunization_implementation_coverage_cbme.md ^
  drafts/chapter13_coverage_monitoring_and_surveillance_cbme.md ^
  drafts/chapter14_vaccine_safety_adverse_events_and_public_confidence_cbme.md ^
  drafts/chapter15_program_evaluation_and_impact_assessment_cbme.md ^
  back_matter.md ^
  --reference-doc=template.docx ^
  --toc ^
  --toc-depth=2 ^
  --number-sections ^
  --highlight-style=tango ^
  -o export\pneumonia-treatment-immunization-cbme.docx

echo Generating HTML format...
pandoc ^
  front_matter.md ^
  drafts/chapter1_introduction_to_pneumonia_epidemiology_and_pathophysiology_cbme.md ^
  drafts/chapter2_pneumonia_classification_community_vs_hospital_acquired_cbme.md ^
  drafts/chapter3_clinical_diagnosis_and_assessment_tools_cbme.md ^
  drafts/chapter4_radiological_diagnosis_and_imaging_cbme.md ^
  drafts/chapter5_microbiological_diagnosis_and_laboratory_tests_cbme.md ^
  drafts/chapter6_antibiotic_treatment_guidelines_and_selection_cbme.md ^
  drafts/chapter7_management_of_severe_and_complicated_pneumonia_cbme.md ^
  drafts/chapter8_non_antibiotic_supportive_care_and_adjunct_therapies_cbme.md ^
  drafts/chapter9_prevention_of_pneumonia_vaccination_strategies_cbme.md ^
  drafts/chapter10_pneumococcal_vaccination_types_and_recommendations_cbme.md ^
  drafts/chapter11_influenza_vaccination_seasonal_and_pandemic_preparedness_cbme.md ^
  drafts/chapter12_immunization_implementation_coverage_cbme.md ^
  drafts/chapter13_coverage_monitoring_and_surveillance_cbme.md ^
  drafts/chapter14_vaccine_safety_adverse_events_and_public_confidence_cbme.md ^
  drafts/chapter15_program_evaluation_and_impact_assessment_cbme.md ^
  back_matter.md ^
  --toc ^
  --toc-depth=2 ^
  --number-sections ^
  --self-contained ^
  --highlight-style=tango ^
  -c custom.css ^
  -o export\pneumonia-treatment-immunization-cbme.html

echo Generating EPUB format...
pandoc ^
  front_matter.md ^
  drafts/chapter1_introduction_to_pneumonia_epidemiology_and_pathophysiology_cbme.md ^
  drafts/chapter2_pneumonia_classification_community_vs_hospital_acquired_cbme.md ^
  drafts/chapter3_clinical_diagnosis_and_assessment_tools_cbme.md ^
  drafts/chapter4_radiological_diagnosis_and_imaging_cbme.md ^
  drafts/chapter5_microbiological_diagnosis_and_laboratory_tests_cbme.md ^
  drafts/chapter6_antibiotic_treatment_guidelines_and_selection_cbme.md ^
  drafts/chapter7_management_of_severe_and_complicated_pneumonia_cbme.md ^
  drafts/chapter8_non_antibiotic_supportive_care_and_adjunct_therapies_cbme.md ^
  drafts/chapter9_prevention_of_pneumonia_vaccination_strategies_cbme.md ^
  drafts/chapter10_pneumococcal_vaccination_types_and_recommendations_cbme.md ^
  drafts/chapter11_influenza_vaccination_seasonal_and_pandemic_preparedness_cbme.md ^
  drafts/chapter12_immunization_implementation_coverage_cbme.md ^
  drafts/chapter13_coverage_monitoring_and_surveillance_cbme.md ^
  drafts/chapter14_vaccine_safety_adverse_events_and_public_confidence_cbme.md ^
  drafts/chapter15_program_evaluation_and_impact_assessment_cbme.md ^
  back_matter.md ^
  --epub-cover-image=cover.jpg ^
  --toc ^
  --toc-depth=2 ^
  --number-sections ^
  --highlight-style=tango ^
  -o export\pneumonia-treatment-immunization-cbme.epub

echo Generating assessment supplements...
pandoc mcq_bank/pneumonia_immunization_cbme_mcq_bank.md ^
  --metadata title="Pneumonia CBME Module MCQ Bank" ^
  --metadata author="Dr. Siddalingaiah H S" ^
  -o export\pneumonia_cbme_mcq_bank.pdf

pandoc assessments/osce_stations_pneumonia_cbme.md ^
  --metadata title="Pneumonia CBME Module OSCE Stations" ^
  --metadata author="Dr. Siddalingaiah H S" ^
  -o export\pneumonia_cbme_osce_stations.pdf

pandoc case_studies/pneumonia_vaccination_integrative_case_study_cbme.md ^
  --metadata title="Pneumonia CBME Module Case Studies" ^
  --metadata author="Dr. Siddalingaiah H S" ^
  -o export\pneumonia_cbme_case_studies.pdf

pandoc student_handouts/pneumonia_cbme_key_concepts_summary.md ^
  --metadata title="Pneumonia CBME Module Student Handouts" ^
  --metadata author="Dr. Siddalingaiah H S" ^
  -o export\pneumonia_cbme_student_handouts.pdf

pandoc DEPLOYMENT_GUIDE.md ^
  --metadata title="Pneumonia CBME Module Deployment Guide" ^
  --metadata author="Dr. Siddalingaiah H S" ^
  -o export\pneumonia_cbme_deployment_guide.pdf

echo Creating ZIP Archive...
powershell Compress-Archive -Path export\* -DestinationPath export\pneumonia-treatment-immunization-cbme-complete-package.zip -Force

echo ================================================
echo COMPILATION COMPLETE!
echo ================================================
echo Generated Files in export/ directory:
echo ================================================
echo pneumonia-treatment-immunization-cbme.pdf (Main textbook - PDF)
echo pneumonia-treatment-immunization-cbme.docx (Word document)
echo pneumonia-treatment-immunization-cbme.html (Web version)
echo pneumonia-treatment-immunization-cbme.epub (E-book format)
echo
echo Supplementary Materials:
echo pneumonia_cbme_mcq_bank.pdf
echo pneumonia_cbme_osce_stations.pdf
echo pneumonia_cbme_case_studies.pdf
echo pneumonia_cbme_student_handouts.pdf
echo pneumonia_cbme_deployment_guide.pdf
echo
echo Complete Package ZIP:
echo pneumonia-treatment-immunization-cbme-complete-package.zip
echo ================================================
echo Developer: Dr. Siddalingaiah H S, FIAHS
echo Version: 2025.1.0
echo Generated: %date% %time%
echo ================================================

pause
