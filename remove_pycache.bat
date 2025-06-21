@echo off  
  
echo Removing __pycache__ directories from git history...  
git rm -r --cached */__pycache__/  
git commit -m "Remove __pycache__ directories from git history"  
  
echo Done!  
echo.  
echo Next steps:  
echo 1. Push changes to GitHub with: git push origin main  
echo 2. Your .gitignore file will prevent future __pycache__ files from being committed  
 
