@echo off
REM CBME Human Anatomy Textbook Compilation Script
echo ========================================
echo   CBME HUMAN ANATOMY TEXTBOOK COMPILER
echo ========================================
echo.

REM Change to scripts directory and run Python script
pushd "%~dp0"

REM Run the Python compilation script
python compile_book.py

REM Pop back to original directory
popd

echo.
echo Compilation process complete!

REM Pause to see results
pause
