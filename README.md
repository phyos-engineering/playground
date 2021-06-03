# Playground

Use this repoistory to practice pull requests, branching, fetching updates from target branch and etc.

## Pull Requests:

**1. Create your own branch:**
```
git checkout -b [name_of_your_new_branch]
```
**2. Push your branch to the respository:**
```
git push origin [name_of_your_new_branch]
```
**3. Switch to your branch:**
```
git checkout [name_of_your_new_branch]
```
**4. Commit and push code to your branch:**
```
git add foo.py
git commit -m "adding method A"
git push
```
**5. Open pull request comparing [name_of_your_branch] with the DEVELOPMENT BRANCH and assign PHYOS-ENGINEERING as reviewer of pull request.**

### Best Practices:

1. Avoid opening pull requests highlighting massive changes (lots of code added/deleted).

## Fetching Updates From A Branch

**1. Switch to your branch:**
```
git checkout [name_of_your_new_branch]
```
**2. Fetch data from [name_of_branch]:**
```
git fetch [name_of_branch]
```
**3. Merge data from [name_of_branch] with your branch:**
```
git merge [name_of_branch]
```
**4. Update your remote branch with merges:**
```
git push
```

**Guides:** https://guides.github.com/

**Hello World For Github:** https://guides.github.com/activities/hello-world/
