@echo off
echo ================================================
echo      ECG Handbook Compiler - Windows Batch
echo ================================================
echo.

echo Starting book compilation process...
python "%~dp0compile_ecg_book.py"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================
    echo           !! SUCCESSFUL COMPILATION !!
    echo ================================================
    echo.
    echo The ECG handbook has been compiled successfully!
    echo.
    echo Next steps:
    echo 1. Check the 'export/book/' directory for the compiled book
    echo 2. The complete handbook file: ecg_handbook_complete.md
    echo 3. Add and commit the compiled book to git
    echo 4. Push to GitHub repository for publication
    echo.
    echo Ready for ECG platform deployment!
    echo.
) else (
    echo.
    echo ================================================
    echo             !! COMPILATION FAILED !!
    echo ================================================
    echo.
    echo Please check the error messages above and fix any issues.
    echo Common issues:
    echo - Python not installed or not in PATH
    echo - Missing chapter files in drafts directory
    echo - Permission issues with file writing
    echo.
)

echo Press any key to continue...
pause >nul
