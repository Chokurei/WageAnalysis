# WageAnalysis

## Summary

* Create hourly wage from the text.

## Rule

* For first commit, ` git clone ` from [` develop `](https://gitlab.com/RM-Trust-Tech/WageAnalysis/tree/develop) branch and create your own branch.
* After second commits, ` git pull ` from [` develop `](https://gitlab.com/RM-Trust-Tech/WageAnalysis/tree/develop) branch when another guys have updated the latest code.
* When you finish your work, pls git push your codes.
* Wheh you finish your task, pls report to me. Then I'll merge the develop branch with your branch.

### Git global setup

```
git config --global user.name "your name"
git config --global user.email "your mail address"
```

### Create a new repository

```
git clone git@gitlab.com:RM-Trust-Tech/WageAnalysis.git
cd WageAnalysis
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

### Existing folder

```
cd existing_folder
git init
git remote add origin git@gitlab.com:RM-Trust-Tech/WageAnalysis.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

### Existing Git repository

```
cd existing_repo
git remote add origin git@gitlab.com:RM-Trust-Tech/WageAnalysis.git
git push -u origin --all
git push -u origin --tags
```