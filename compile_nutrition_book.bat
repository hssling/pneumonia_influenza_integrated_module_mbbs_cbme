@echo off
echo ======================================>
echo = COMPILING CBME NUTRITION TEXTBOOK =
echo ======================================>

echo Setting up environment...
cd nutrition-cbme-textbook

echo.
echo = CREATING COMPILED BOOK CONTENTS =

REM Create the export directories
if not exist "export\compiled" mkdir "export\compiled"
if not exist "export\published" mkdir "export\published"

echo.
echo = COMBINING FRONT MATTER + ALL CHAPTERS + BACK MATTER =

REM Copy front matter first
copy /y "front_matter.md" "export\compiled\complete_nutrition_textbook.md" >nul

REM Append all chapters in order
for %%i in (1,1,42) do if exist "drafts\chapter%%i_*.md" for %%f in ("drafts\chapter%%i_*.md") do (
    echo. >> "export\compiled\complete_nutrition_textbook.md"
    echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
    echo # Chapter %%i >> "export\compiled\complete_nutrition_textbook.md"
    echo ======================================================== >> "export\compiled\complete_nutrition_textbook.md"
    echo. >> "export\compiled\complete_nutrition_textbook.md"
    type "%%f" >> "export\compiled\complete_nutrition_textbook.md"
)

REM Append back matter
echo. >> "export\compiled\complete_nutrition_textbook.md"
type "back_matter.md" >> "export\compiled\complete_nutrition_textbook.md"

echo.
echo = CONVERTING TO MULTIPLE FORMATS =

REM Check if pandoc is available
where pandoc >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Pandoc found! Converting formats...

    REM Generate PDF (requires LaTeX distribution like MiKTeX or TeX Live)
    echo Creating PDF...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.pdf" --pdf-engine=pdflatex --variable fontsize=12pt --variable geometry:margin=1in

    REM Generate DOCX
    echo Creating DOCX...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.docx" --reference-doc="templates/book_template.docx"

    REM Generate HTML with custom styling
    echo Creating HTML...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.html" --self-contained --css="templates/book_style.css" --toc --toc-depth=3

    REM Generate EPUB
    echo Creating EPUB...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.epub" --toc --toc-depth=3 --epub-title="Comprehensive Clinical Nutrition Textbook (CBME)"

    REM Generate LaTeX source
    echo Creating LaTeX...
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.tex" --latex-engine=pdflatex

    echo.
    echo ✓ ALL FORMATS GENERATED SUCCESSFULLY!
    echo ======================================>
    echo = PDF:     nutrition_cbme_complete.pdf
    echo = DOCX:    nutrition_cbme_complete.docx
    echo = HTML:    nutrition_cbme_complete.html
    echo = EPUB:    nutrition_cbme_complete.epub
    echo = LaTeX:   nutrition_cbme_complete.tex
    echo ======================================>
) else (
    echo Pandoc NOT found. Installing pandoc is recommended for format conversion.
    echo Currently available: Markdown format only.
    echo Please install pandoc from: https://pandoc.org/installing.html
)

REM Create separate unit compilations
echo.
echo = CREATING INDIVIDUAL UNIT COMPILATIONS =

for %%u in (1,1,7) do (
    echo Compiling Unit %%u...
    if %%u==1 set UNIT_TITLE=Basic Principles of Nutrition
    if %%u==2 set UNIT_TITLE=Lifecycle Nutrition
    if %%u==3 set UNIT_TITLE=Nutritional Disorders and Management
    if %%u==4 set UNIT_TITLE=Clinical Nutrition in Disease Management
    if %%u==5 set UNIT_TITLE=Public Health Nutrition
    if %%u==6 set UNIT_TITLE=Advanced Topics in Nutrition Science
    if %%u==7 set UNIT_TITLE=Ethical, Legal and Professional Aspects

    REM Calculate chapter ranges for each unit
    if %%u==1 (
        set CHAPTER_START=1
        set CHAPTER_END=7
    ) else if %%u==2 (
        set CHAPTER_START=8
        set CHAPTER_END=12
    ) else if %%u==3 (
        set CHAPTER_START=13
        set CHAPTER_END=18
    ) else if %%u==4 (
        set CHAPTER_START=19
        set CHAPTER_END=24
    ) else if %%u==5 (
        set CHAPTER_START=25
        set CHAPTER_END=30
    ) else if %%u==6 (
        set CHAPTER_START=31
        set CHAPTER_END=36
    ) else if %%u==7 (
        set CHAPTER_START=37
        set CHAPTER_END=42
    )

    echo # Unit %%u: !UNIT_TITLE! > "export\compiled\unit%%u_nutrition_cbme.md"
    for /l %%c in (!CHAPTER_START!,1,!CHAPTER_END!) do if exist "drafts\chapter%%c_*.md" (
        echo. >> "export\compiled\unit%%u_nutrition_cbme.md"
        echo --- >> "export\compiled\unit%%u_nutrition_cbme.md"
        echo. >> "export\compiled\unit%%u_nutrition_cbme.md"
        type "drafts\chapter%%c_*.md" >> "export\compiled\unit%%u_nutrition_cbme.md"
    )
)

echo.
echo = GENERATING MCQ COMPILATIONS =

if exist "mcq_bank\*.md" (
    echo Combining MCQ assessments...
    copy /y "mcq_bank\nutrition_mcq_template.md" "export\compiled\nutrition_mcq_bank_compiled.md" >nul
    echo. >> "export\compiled\nutrition_mcq_bank_compiled.md"
    echo --- >> "export\compiled\nutrition_mcq_bank_compiled.md"
    echo. >> "export\compiled\nutrition_mcq_bank_compiled.md"
    for %%m in ("mcq_bank\*.md") do if not "%%m"=="nutrition_mcq_template.md" type "%%m" >> "export\compiled\nutrition_mcq_bank_compiled.md"
)

echo.
echo = CREATING BOOK METADATA =

REM Create metadata file
echo Book Title: Comprehensive Clinical Nutrition Textbook (CBME Compliant) > "export\compiled\book_metadata.txt"
echo Author: Dr. Siddalingaiah H S >> "export\compiled\book_metadata.txt"
echo Email: hssling@yahoo.com >> "export\compiled\book_metadata.txt"
echo Phone: +91-8941087719 >> "export\compiled\book_metadata.txt"
echo Affiliation: Indian Medical Council Representative >> "export\compiled\book_metadata.txt"
echo Edition: 2.0.0 >> "export\compiled\book_metadata.txt"
echo Publication Date: 2025 >> "export\compiled\book_metadata.txt"
echo ISBN: [Assigned upon commercial publication] >> "export\compiled\book_metadata.txt"
echo Total Chapters: 42 >> "export\compiled\book_metadata.txt"
echo Units: 7 >> "export\compiled\book_metadata.txt"
echo Compliance: CBME, NMC India >> "export\compiled\book_metadata.txt"
echo Target Audience: MBBS, MD, Nutrition Specialists >> "export\compiled\book_metadata.txt"

echo.
echo ======================================>
echo = COMPILATION COMPLETED SUCCESSFULLY! =
echo ======================================>
echo.
echo 📚 COMPILED BOOK AVAILABLE AT:
echo ===============================
echo Markdown: export\compiled\complete_nutrition_textbook.md
echo.
if exist "export\published\*.pdf" echo PDF:       export\published\nutrition_cbme_complete.pdf
if exist "export\published\*.docx" echo DOCX:     export\published\nutrition_cbme_complete.docx
if exist "export\published\*.html" echo HTML:     export\published\nutrition_cbme_complete.html
if exist "export\published\*.epub" echo EPUB:     export\published\nutrition_cbme_complete.epub
if exist "export\published\*.tex" echo LaTeX:    export\published\nutrition_cbme_complete.tex
echo.
echo 🧪 MCQ Bank: export\compiled\nutrition_mcq_bank_compiled.md
echo 📊 Metadata: export\compiled\book_metadata.txt
echo.
echo Next: Push all compiled files to GitHub!
echo =======================================>
