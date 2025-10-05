@echo off
echo =====================================>
echo = COPYING MALNUTRITION CONTENT TO CLEAN REPO =
echo =====================================>

cd ../malnutrition-module-repo

echo Removing old malnutrition content...
rd /s /q malnutrition-cbme-training

echo Copying complete malnutrition module...
xcopy /e /i /y "..\book_automation_mcp\malnutrition-cbme-training" "malnutrition-cbme-training" >nul

echo Verifying copy...
dir malnutrition-cbme-training\drafts /b

echo =====================================>
echo = COPY COMPLETE - READY FOR PUSH =
echo =====================================>
