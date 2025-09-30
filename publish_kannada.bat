@echo off
setlocal ENABLEDELAYEDEXPANSION
cd /d "d:\AI Book and Content Writer\book_automation_mcp"

set SRC=export\book\community_medicine_kannada.md
set OUTDIR=export\book
set DOCX=%OUTDIR%\community_medicine_kannada.docx
set HTML=%OUTDIR%\community_medicine_kannada.html
set CSS=%OUTDIR%\kannada.css
set PDF=%OUTDIR%\community_medicine_kannada.pdf

REM Prefer bundled Pandoc; fallback to PATH
set PANDOC_EXE=pandoc\pandoc-3.1.9\pandoc.exe
if not exist "%PANDOC_EXE%" set PANDOC_EXE=pandoc

echo Using Pandoc: %PANDOC_EXE%
if not exist "%SRC%" (
  echo Source not found: %SRC%
  exit /b 1
)

echo [1/4] Building DOCX...
"%PANDOC_EXE%" "%SRC%" -s -o "%DOCX%" --toc --toc-depth=2 --metadata lang=kn-IN --metadata title="Community Medicine (Kannada)"
if errorlevel 1 ( echo DOCX build failed. ) else ( echo DOCX written to %DOCX% )

echo [2/4] Building HTML...
if exist "%CSS%" (
  echo Using CSS: %CSS%
  "%PANDOC_EXE%" "%SRC%" -s -o "%HTML%" --toc --toc-depth=2 --metadata lang=kn-IN --metadata title="Community Medicine (Kannada)" --css="%CSS%"
) else (
  "%PANDOC_EXE%" "%SRC%" -s -o "%HTML%" --toc --toc-depth=2 --metadata lang=kn-IN --metadata title="Community Medicine (Kannada)"
)
if errorlevel 1 ( echo HTML build failed. ) else ( echo HTML written to %HTML% )

echo [3/4] Trying XeLaTeX via Pandoc...
where xelatex >nul 2>&1
if %errorlevel%==0 (
  "%PANDOC_EXE%" "%SRC%" -s -o "%PDF%" --toc --toc-depth=2 --pdf-engine=xelatex -V mainfont="Nirmala UI" -V geometry:margin=1in 1>nul 2>"%OUTDIR%\xelatex_errors.log"
)
if exist "%PDF%" goto done_pdf

echo [4/4] HTML-to-PDF fallbacks...
where wkhtmltopdf >nul 2>&1
if %errorlevel%==0 (
  wkhtmltopdf -q "%HTML%" "%PDF%"
)
if exist "%PDF%" goto done_pdf

for %%I in ("%HTML%") do set HTML_ABS=%%~fI
for %%J in ("%PDF%") do set PDF_ABS=%%~fJ
where msedge >nul 2>&1
if %errorlevel%==0 (
  echo Using Microsoft Edge headless to print PDF...
  msedge --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
)
if exist "%PDF%" goto done_pdf

where chrome >nul 2>&1
if %errorlevel%==0 (
  echo Using Google Chrome headless to print PDF...
  chrome --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
)
if exist "%PDF%" goto done_pdf

REM Try default install paths for Edge/Chrome
if not exist "%PDF%" (
  if exist "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" (
    echo Using Edge default path to print PDF...
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
  )
)
if not exist "%PDF%" (
  if exist "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" (
    echo Using Edge x86 path to print PDF...
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
  )
)
if exist "%PDF%" goto done_pdf

if not exist "%PDF%" (
  if exist "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" (
    echo Using Chrome default path to print PDF...
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
  )
)
if not exist "%PDF%" (
  if exist "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" (
    echo Using Chrome x86 path to print PDF...
    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --headless=new --disable-gpu --print-to-pdf="%PDF_ABS%" "%HTML_ABS%"
  )
)
if exist "%PDF%" goto done_pdf

echo PDF build failed. See %OUTDIR%\xelatex_errors.log (if any). You can also print the HTML to PDF in a browser.
goto end

:done_pdf
echo PDF written to %PDF%

:end
echo Done.
endlocal
