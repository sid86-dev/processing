clear
echo "remote: -----> pushing files to remote repo...";
echo -en "\n";
git add .;
read -p "Enter push reason: " reason;
git commit -m "$reason";
git push origin develop;
echo "remote: -----> remote push complete";