# How to Transfer Coursework Files to Your Personal GitHub Repository (Windows CMD)

```cmd
REM 1. Move to your Documents folder (or wherever you want to work)
cd %USERPROFILE%\Documents

REM 2. Clone your personal repository from GitHub
git clone https://github.com/Farhazprojects/university-projects-portfolio.git

REM 3. Clone your coursework repository (if you haven’t already)
git clone https://github.com/Farhazprojects/coit20246y25t1-journal-Farhazkhondoker.git

REM 4. Create the "Networking and Security" directory inside your portfolio repo
mkdir "university-projects-portfolio\Networking and Security"

REM 5. Copy your weekly journal markdown files to your portfolio repo
copy coit20246y25t1-journal-Farhazkhondoker\week*.md "university-projects-portfolio\Networking and Security\"

REM 6. (Optional) Copy images folder if you have images
xcopy /E /I coit20246y25t1-journal-Farhazkhondoker\images "university-projects-portfolio\Networking and Security\images"

REM 7. Change into your personal repository directory
cd university-projects-portfolio

REM 8. Set your Git username and email (only needs to be done once per computer)
git config --global user.name "Farhaz Khondoker"
git config --global user.email "farhazkhondoker0@gmail.com"

REM 9. Add the new files to Git staging
git add "Networking and Security"

REM 10. Commit the changes
git commit -m "Add weekly journal files to Networking and Security"

REM 11. Push your changes to GitHub
git push

REM 12. Visit your repository online to check your files
REM https://github.com/Farhazprojects/university-projects-portfolio
```
