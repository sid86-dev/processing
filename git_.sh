git add .;
read -p "Enter push reason: " reason;
git commit -m "$reason";
git push origin develop;