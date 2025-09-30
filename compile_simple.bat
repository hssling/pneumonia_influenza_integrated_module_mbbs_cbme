@echo off
echo ======================================>
echo = SIMPLE COMPILATION SCRIPT =
echo ======================================>

REM Change to textbook directory
cd nutrition-cbme-textbook

REM Create export directories
mkdir "export\compiled" 2>nul
mkdir "export\published" 2>nul

echo Creating complete textbook markdown...

REM Start with front matter
copy "front_matter.md" "export\compiled\complete_nutrition_textbook.md" >nul

REM Add all chapters (simple loop - manually specify each one)
echo. >> "export\compiled\complete_nutrition_textbook.md"
echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
echo # Chapter 1: Introduction to Clinical Nutrition >> "export\compiled\complete_nutrition_textbook.md"
echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
echo. >> "export\compiled\complete_nutrition_textbook.md"
type "drafts\chapter1_introduction_clinical_nutrition_cbme.md" >> "export\compiled\complete_nutrition_textbook.md"

REM Add other chapters 2-42 similarly
for %%i in (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42) do (
    echo. >> "export\compiled\complete_nutrition_textbook.md"
    echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
    echo # Chapter %%i >> "export\compiled\complete_nutrition_textbook.md"
    echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
    echo. >> "export\compiled\complete_nutrition_textbook.md"

    REM Find the chapter file
    for %%f in ("drafts\*chapter%%i_*.md") do (
        if exist "%%f" type "%%f" >> "export\compiled\complete_nutrition_textbook.md"
    )
)

REM Add back matter
echo. >> "export\compiled\complete_nutrition_textbook.md"
type "back_matter.md" >> "export\compiled\complete_nutrition_textbook.md"

echo.
echo = GENERATING PUBLISHED FORMATS =

REM Check if pandoc exists
where pandoc >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Pandoc found! Generating formats...

    echo Creating PDF...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.pdf" --pdf-engine=pdflatex --variable fontsize=12pt --variable geometry:margin=1in 2>nul

    echo Creating DOCX...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.docx" 2>nul

    echo Creating HTML...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.html" --self-contained --css="templates/book_style.css" --toc --toc-depth=3 2>nul

    echo Creating EPUB...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.epub" --toc --toc-depth=3 2>nul

    echo Creating LaTeX...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.tex" 2>nul

    echo.
    echo ✓ FORMAT CONVERSION COMPLETED!
    echo.
    echo FILE OUTPUTS:
    dir "export\published" /b 2>nul
) else (
    echo Pandoc not found. Only Markdown format available.
    echo Install pandoc from: https://pandoc.org/installing.html
)

REM Create metadata
echo Book Title: Comprehensive Clinical Nutrition Textbook (CBME Compliant) > "export\compiled\book_metadata.txt"
echo Author: Dr. Siddalingaiah H S >> "export\compiled\book_metadata.txt"
echo Email: hssling@yahoo.com >> "export\compiled\book_metadata.txt"
echo Phone: +91-8941087719 >> "export\compiled\book_metadata.txt"
echo Total Chapters: 42 >> "export\compiled\book_metadata.txt"
echo Unit Count: 7 >> "export\compiled\book_metadata.txt"
echo Compliance: CBME, NMC India >> "export\compiled\book_metadata.txt"
echo Publication Date: 2025 >> "export\compiled\book_metadata.txt"

echo.
echo ======================================>
echo = COMPILATION FINISHED! =
echo ======================================>
echo.
echo COMPLETE BOOK: export\compiled\complete_nutrition_textbook.md
if exist "export\published\*.pdf" echo PDF VERSION: export\published\nutrition_cbme_complete.pdf
if exist "export\published\*.docx" echo DOCX VERSION: export\published\nutrition_cbme_complete.docx
if exist "export\published\*.html" echo HTML VERSION: export\published\nutrition_cbme_complete.html
if exist "export\published\*.epub" echo EPUB VERSION: export\published\nutrition_cbme_complete.epub
echo METADATA: export\compiled\book_metadata.txt
echo.
cd ..
echo Ready to commit and push to GitHub!
echo ======================================>
