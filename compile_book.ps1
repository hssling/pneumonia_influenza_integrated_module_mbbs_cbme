$processPath = "nutrition-cbme-textbook"

Write-Host "=======================================>" -ForegroundColor Green
Write-Host "= COMPILING CBME NUTRITION TEXTBOOK =" -ForegroundColor Green
Write-Host "=======================================>" -ForegroundColor Green

# Change to textbook directory
Set-Location $processPath

Write-Host "Setting up export directories..." -ForegroundColor Yellow

# Create export directories
$compiledPath = "export\compiled"
$publishedPath = "export\published"
if (!(Test-Path $compiledPath)) { New-Item -ItemType Directory -Path $compiledPath -Force }
if (!(Test-Path $publishedPath)) { New-Item -ItemType Directory -Path $publishedPath -Force }

Write-Host "`n= COMBINING FRONT MATTER + ALL CHAPTERS + BACK MATTER =" -ForegroundColor Cyan

# Start with front matter
Copy-Item "front_matter.md" "export\compiled\complete_nutrition_textbook.md" -Force

# Add all chapters - simplified approach
$chapters = 1..42
foreach ($i in $chapters) {
    $chapterMarker = "`n========================================================`n# Chapter $i`n========================================================`n"
    Add-Content -Path "export\compiled\complete_nutrition_textbook.md" -Value $chapterMarker

    # Find and add the chapter content
    $chapterFiles = Get-ChildItem -Path "drafts" -Filter "*chapter${i}_*.md"
    foreach ($file in $chapterFiles) {
        $content = Get-Content -Path $file.FullName -Raw
        Add-Content -Path "export\compiled\complete_nutrition_textbook.md" -Value $content
    }
}

# Add back matter
$backContent = Get-Content -Path "back_matter.md" -Raw
Add-Content -Path "export\compiled\complete_nutrition_textbook.md" -Value "$backContent"

Write-Host "`n= CHECKING FOR FORMAT CONVERSION =" -ForegroundColor Cyan

# Check for pandoc
$pandocExists = Get-Command pandoc -ErrorAction SilentlyContinue
if ($pandocExists) {
    Write-Host "Pandoc found! Generating formats..." -ForegroundColor Green

    Write-Host "Creating PDF..." -ForegroundColor Yellow
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.pdf" --pdf-engine=pdflatex --variable fontsize=12pt --variable geometry:margin=1in 2>$null

    Write-Host "Creating DOCX..." -ForegroundColor Yellow
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.docx" 2>$null

    Write-Host "Creating HTML..." -ForegroundColor Yellow
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.html" --self-contained --css="templates/book_style.css" --toc --toc-depth=3 2>$null

    Write-Host "Creating EPUB..." -ForegroundColor Yellow
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.epub" --toc --toc-depth=3 2>$null

    Write-Host "Creating LaTeX..." -ForegroundColor Yellow
    pandoc "export\compiled\complete_nutrition_textbook.md" -o "export\published\nutrition_cbme_complete.tex" 2>$null

    Write-Host "`n✓ ALL FORMATS GENERATED SUCCESSFULLY!" -ForegroundColor Green
    Write-Host "=======================================>" -ForegroundColor Green
    Write-Host "= PDF:     nutrition_cbme_complete.pdf" -ForegroundColor White
    Write-Host "= DOCX:    nutrition_cbme_complete.docx" -ForegroundColor White
    Write-Host "= HTML:    nutrition_cbme_complete.html" -ForegroundColor White
    Write-Host "= EPUB:    nutrition_cbme_complete.epub" -ForegroundColor White
    Write-Host "= LaTeX:   nutrition_cbme_complete.tex" -ForegroundColor White
    Write-Host "=======================================>" -ForegroundColor Green
} else {
    Write-Host "Pandoc NOT found. Installing pandoc is recommended for format conversion." -ForegroundColor Red
    Write-Host "Currently available: Markdown format only." -ForegroundColor Yellow
    Write-Host "Please install pandoc from: https://pandoc.org/installing.html" -ForegroundColor Cyan
}

Write-Host "`n= CREATING BOOK METADATA =" -ForegroundColor Cyan

# Create metadata file
$metadata = @"
Book Title: Comprehensive Clinical Nutrition Textbook (CBME Compliant)
Author: Dr. Siddalingaiah H S
Email: hssling@yahoo.com
Phone: +91-8941087719
Affiliation: Indian Medical Council Representative
Edition: 2.0.0
Publication Date: 2025
ISBN: [Assigned upon commercial publication]
Total Chapters: 42
Units: 7
Compliance: CBME, NMC India
Target Audience: MBBS, MD, Nutrition Specialists
"@

$metadata | Out-File -FilePath "export\compiled\book_metadata.txt" -Encoding UTF8

Write-Host "`n=======================================>" -ForegroundColor Green
Write-Host "= COMPILATION COMPLETED SUCCESSFULLY! =" -ForegroundColor Green
Write-Host "=======================================>" -ForegroundColor Green

Write-Host "`n📚 COMPILED BOOK AVAILABLE AT:" -ForegroundColor Cyan
Write-Host "==============================" -ForegroundColor Cyan
Write-Host "Markdown: export\compiled\complete_nutrition_textbook.md" -ForegroundColor White

if (Test-Path "export\published\nutrition_cbme_complete.pdf") {
    Write-Host "PDF:       export\published\nutrition_cbme_complete.pdf" -ForegroundColor White
}
if (Test-Path "export\published\nutrition_cbme_complete.docx") {
    Write-Host "DOCX:      export\published\nutrition_cbme_complete.docx" -ForegroundColor White
}
if (Test-Path "export\published\nutrition_cbme_complete.html") {
    Write-Host "HTML:      export\published\nutrition_cbme_complete.html" -ForegroundColor White
}
if (Test-Path "export\published\nutrition_cbme_complete.epub") {
    Write-Host "EPUB:      export\published\nutrition_cbme_complete.epub" -ForegroundColor White
}
Write-Host "Metadata:  export\compiled\book_metadata.txt" -ForegroundColor White

# Return to parent directory
Set-Location ..

Write-Host "`nNext: Push all compiled files to GitHub!" -ForegroundColor Green
Write-Host "=======================================>" -ForegroundColor Green
