# gitlab
0. Git global setup
```bash
git config --global user.name "tzhouyi_108087"
git config --global user.email "tzhouyi@todaychina.com"
git config --global --list
```

1. Git local setup
* please check .git/config file
```bash
git config user.name "Your Name"
git config user.email "Your Email"
```

2. Create a new repository
```bash
git clone https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
cd liops-jobs
git switch -c master
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```
3. Push an existing folder
```bash
cd existing_folder
git init --initial-branch=master
git remote add origin https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
git add .
git commit -m "Initial commit"
git push -u origin master
```
4. Push an existing Git repository
```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.chehejia.com/tzhouyi_108087/liops-jobs.git
git push -u origin --all
git push -u origin --tags
```

5. git规范
    * feat: A new feature
    * fix: A bug fix
    * docs: Documentation only changes
    * style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    * refactor: A code change that neither fixes a bug nor adds a feature
    * perf: A code change that improves performance
    * test: Adding missing or correcting existing tests
    * chore: Changes to the build process or auxiliary tools and libraries such as documentation generation