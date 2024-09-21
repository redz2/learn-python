# gitlab
0. Git global setup
```
git config --global user.name "tzhouyi_108087"
git config --global user.email "tzhouyi@todaychina.com"
git config --global --list
```

1. Git local setup
* please check .git/config file
```
git config user.name "Your Name"
git config user.email "Your Email"
```

2. Create a new repository
```
git clone https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
cd liops-jobs
git switch -c master
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```
3. Push an existing folder
```
cd existing_folder
git init --initial-branch=master
git remote add origin https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
git add .
git commit -m "Initial commit"
git push -u origin master
```
4. Push an existing Git repository
```
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
git push -u origin --all
git push -u origin --tags
```