# PacketVSocket Assignments

This repository contains the assignments and activities based on the PacketVSocket Summer-Mentorship Program conducted by **Cipher IET NITK - 2025**. 
The repository will be regularly updated every week, therefore, follow the commands below to keep your local repositories updated. 

---

To begin with finding your assignments in a local-git-repository, you're welcome to follow the below commands. And if you'd like to NOT take this route, you're welcome to find the folder here in this GitHub repository at regular intervals and download the necessary files and start hands-on :)

## Setup Commands:
To set up the git-repositories with the assignment folders for the first time, follow the commands:
1. Setup the repository by cloning it:
    ```bash
    git clone https://github.com/cs131-231nitk/IET25SMP-PacketVSocket-Assgn.git
    ```
2. Navigate into the repository:
    ```bash
    cd IET25SMP-PacketVSocket-Assgn
    ```

You can now view the assignments in their Week's folder and find the fun-activies :)

## Updating the Local-Repo:
Now that you notice new changes in the repository, you don't have to clone it again, which you can, but a little creative way is the following:
1. Pull down the changes made in the original-repo (Fetching):
    ```bash
    git fetch origin main
    # OR simply
    git fetch --all
    ```
    Now, all the new updates are in the branch `origin/main` instead of `main`. 
2. Get the changes pulled into your `main` branch:
    ```bash
    git checkout main
    git rebase origin/main

    # OR in simple-terms
    git switch main
    git merge origin/main
    ```
You now have all the changes made in the **remote-repository** to your **local-repository**.

## Interested submitting your solutions?
If you're interested in submitting your solutions, you can manually contact your subject-mentors and submit it to them, or follow the Official PacketVSocket WhatsApp group to know more about the submission protocol. 

The best solution amongst all will be uploaded in the `solutions` branch and will be tagged by the solution-ideator's GitHub handle! :) 
