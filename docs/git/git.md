#Tracking Code In Git/github

![](figures/git/sph_cida_wm_blk.png)

---



# Introduction

## What is Git?

According to Git's website, "Git is a free and open source distributed version 
control system." So what does that mean? Let's break it down. First, Similarly to R, 
Git is available to anyone with a computer and access to the internet free of 
charge. Anyone can install and use it, and anyone can contribute to the project
(if they have the technical know-how). 

As for the second half, a version control system (VCS) is a tool that enables
teams as small as a single person or as large as a multinational corporation to
track changes in code over time and to integrate changes made by a 
decentralized team of developers.

For our purposes, Git enables us to create reproducible analysis code bases,
where the full history of the analysis is available to ourselves and those which
we choose to share it with.

## What is GitHub?

## Command Line Basics

In order to use Git from the command line (Terminal or Git Bash), a certain
level of basic commands will be needed to navigate the files on your computer. 
Below is a list of commands that will help you navigate your directories and
accomplish basic tasks using the command line.

- `ls` - List subdirectories and files in current directory
- `pwd` - Print working directory
- `cd` - Change directory (i.e., navigate to a different folder)
  - `cd MyFolder` - Move to the folder `MyFolder` located in current working
  directory
  - `cd Path/To/MyFolder` - Move to the folder `MyFolder` located at 
  `Path/To/` inside the current working directory
  - `cd ..` - Move to parent directory (i.e. one folder back)
  - `cd /` - Move to root directory
  - `cd ~` - Move to home directory
- `mkdir` - Make directory
- `rm <filename>` - Remove file

## Notes

### Terminal / Git Bash

The instructions which follow attempt to be applicable to both MacOS and Windows
platforms. However, some key differences do exist between the two
operating systems. In most of these situations we have created separate 
instructions for Windows and MacOS. However, for sections where MacOS and
Windows are functionally the same, only a single section is provided. In these
sections, some language used may reference Terminal, and in those cases you
should substitute Git Bash if you are using Windows operating system.

### Main vs Master

Historically, the default branch in a new Git repository was named `master`. 
However, in 2020 a push to remove unnecessary references to slavery led 
GitHub and other companies to change the default branch name to `main`. The
instructions which follow will assume the default branch name is `main` and
will show you how to setup your local Git configuration to default to `main`.

However, due to the relative recency of this change, you may encounter 
repositories that have `master` as the primary branch. In such situations, all
the instructions which follow will still be applicable, but you will need to
substitute `main` for `master`.

# Getting Started

## Installing Git

### MacOS

Open Terminal and run the command `git --version`. If you don't have Git
installed already, you will be prompted to install. Follow the 
instructions provided in the Terminal or pop-up window to install Git.

### Windows

Git and Git Bash come included as part of the 
[Git For Windows](https://gitforwindows.org/) package. 
Download and install Git For Windows like other Windows applications. Once 
downloaded find the included `.exe` file and open to execute Git Bash.

## Creating GitHub Account

Go to <https://github.com/> and click `Sign Up` in the upper right hand corner.
Follow the instructions to create an account, choosing an account name that is
easily identifiable as belonging to you (i.e. "firstname-lastname" or something
similar).

__NOTE:__ If you already have a personal GitHub account, you may continue to use
it for your work at CIDA __if__ your account name is easily identifiable as 
belonging to you (i.e. if you have an account name like "firstname-lastname" or 
something similar).

## Configure Git

To associate your local Git configuration with your name and Email, run the 
commands below in Terminal or Git Bash. Here, `your_email@cuanschutz.edu` should
be substituted with
the email associated with your GitHub account. If you are using a preexisting
personal GitHub account, this may or may not end with `cuanschutz.edu`. 

```bash
git config --global user.name "Firstname Lastname"
git config --global user.email "your_email@cuanschutz.edu"
```

Additionally, your local Git should be configured to make `main` the default
branch name. To do so, run the following command in Terminal/GitBash:

```bash
git config --global -add init.defaultBranch main
```

## Requesting CIDA GitHub Access

Following account creation, send an email containing your GitHub username to 
`ryan <dot> peterson <at> cuanschutz <dot> edu` and 
`max <dot> mcgrath <at> cuanschutz <dot> edu` to request access to CIDA's GitHub
organization (please send email from your cuanschutz.edu email address).

## Setting Up SSH

The below instructions are up-to-date as of 10/05/22. Newer instructions along 
with additional troubleshooting may
be available from [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### MacOS

1. Check for Existing SSH Keys
    a. Open Terminal
    b. Enter `ls -al ~/.ssh` to see if existing SSH keys are present by looking
    for the following filenames:
        - id_rsa.pub
        - id_ecdsa.pub
        - id_ed25519
    c. If you see any of these files present, proceed to Step 3. Otherwise
    continue with Step 2.
2. Generate a new SSH key
   a. Open Terminal
   b. Enter `ssh-keygen -t ed25519 -C "your_email@example.com"` substituting in
   the email address associated with your GitHub account
   c. When you're prompted to "Enter a file in which to save the key," press 
   Enter. This accepts the default file location.
   d. At the prompt, type a secure passphrase
   e. Start the ssh-agent in the background by running `eval "$(ssh-agent -s)"`
   f. Open the configuration file with `open ~/.ssh/config`
      - If the file doesn't exist create it with `touch ~/.ssh/config` then use
      the above command to open it
   g. Edit `~/.ssh/config` to contain the following lines:
   
```bash
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
   h. Add your SSH private key to the ssh-agent and store your password in the 
   keychain by running `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`
3. Add SSH key to GitHub account
    a. Copy the SSH public key to your clipboard with 
    `pbcopy < ~/.ssh/id_ed25519.pub`
    b. Open GitHub in a web browser, log in
    c. Go the the upper right hand corner, click your profile photo, and
    select __Settings__
    d. Select __SSH and GPG keys__ in the menu on the left
    e. Click green __New SSH key__ button
    f. Enter a title for the SSH key in the __Title__ field (use descriptive 
    title like "CIDA MacBook Pro")
    g. Select __Key type__ as "Authentication Key"
    h. Paste your key into the __Key__ field
    i. Click __Add SSH key__
4. Verify connection
    a. Test access to GitHub SSH with `ssh -T git@github.com`
    b. If you see the following message, verify that the fingerprint you see
    matches GitHub's public key fingerprint
    ([link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)). 
    If it does, type `Yes`
```bash
> The authenticity of host 'github.com (IP ADDRESS)' cant be established.
> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
> Are you sure you want to continue connecting (yes/no)?
```
    c. Verify that the resulting message contains your username. If you receive 
    a "permission denied" message, see [Error: Permission denied (publickey)](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey)


### Windows

1. In Git Bash, type `ssh-keygen`
2. Press enter to save the SSH key to the default location
3. Enter a password to password protect your SSH key or leave blank and hit 
`Enter` to proceed without a password
4. You will recieve a message saying your public key has been saved in 
`c/Users/username/.ssh/id_rsa.pub`, type `cat c/Users/username/.ssh/id_rsa.pub`
to output the key
5. Copy and paste the key
6. Add SSH key to GitHub account
    a. Open GitHub in a web browser, log in
    b. Go the the upper right hand corner, click your profile photo, and
    select __Settings__
    c. Select __SSH and GPG keys__ in the menu on the left
    d. Click green __New SSH key__ button
    e. Enter a title for the SSH key in the __Title__ field (use descriptive 
    title like "CIDA MacBook Pro")
    f. Select __Key type__ as "Authentication Key"
    g. Paste your key into the __Key__ field
    h. Click __Add SSH key__


## Setting up SSO

Copy/distill instructions here: 
<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/about-authentication-with-saml-single-sign-on>

1. After being granted access to the CIDA-CSPH GitHub organization and setting 
up SSH, go to <https://github.com>, log in
2. In the upper-right corner of any page, click your profile photo, then click
__Settings__
3. Select __SSH and GPG keys__ in the menu on the left
4. To the right of the SSH key you'd like to authorize, click __Configure SSO__.
If you don't see __Configure SSO__, ensure that you have authenticated at least
once with the CIDA-CSPH organization by visiting 
<https://github.com/orgs/CIDA-CSPH/>, accessing a non-public repository, and
signing in with your CU login
5. You will see __CIDA-CSPH__ listed. Click __Authorize__ to the right.

## Creating New Project

1. Create project folder on your local computer by calling 
`CIDAtools::create_project()` in `R`
2. Initialize git repository by navigating to folder (`cd Path/To/Folder`) then
using the command `git init`
3. Stage file changes `git add . `
4. Create initial commit with `git commit -m "Initial commit"`
5. Create empty repository in CIDA-CSPH GitHub organization
    a. In a web browser, navigate to <https://github.com/orgs/CIDA-CSPH/repositories>
    b. Sign in using your CU login
    c. Click the green `New repository` button
    d. Enter the name of your repository
    e. Do __not__ add a template, README, .gitignore, or license file
    f. Click `Create repository`
6. Add remote to local repository with 
`git remote add origin git@github.com:CIDA-CSPH/<your-repository>.git` (this SSH link
can be copied from the empty GitHub remote repository you've just created).
7. Push work to GitHub with `git push origin main`

## Cloning Existing Project

1. Navigate to GitHub remote repository
2. Click green "Code &or;" button
3. Click "SSH" then copy link
4. Clone repository with `git clone git@github.com:CIDA-CSPH/<your-repository>.git`

# Regular Workflow

1. Add and commit changes
```bash
cd Path/To/Directory
git add .
git commit -m "My commit message"
```
2. Fetch and merge any changes (see Handling Merge Conflicts below)
```bash
git fetch origin main
git merge origin/main
## Fix any merge conflicts
git commit -m "Brief description of changes (<=50 characters)"
```
3. Push all new commits
```bash
git push origin main
```

## Handling Merge conflicts

In the case that another user has modified and committed changes to a file that
you have modified in one of your recent commits, when you run `git pull` you 
may be notified that you have a merge conflict and need to resolve those
conflicts before you can push your changes to GitHub. To do so:

1. After running `git merge origin/main` and being notified that you have
merge conflicts, run `git status` to see which files have conflicts (they
will be listed with `both modified: ` in front of them)
    a. Note: On newer version of Git you may receive an error saying "You have
    divergent branches and need to specify how to reconcile them"
    b. In this case, you can add an indicator to pull without rebasing with
    `git merge --no-rebase origin/main`
2. Open those files in a text editor (RStudio, Vim, textEdit, Notepad++, etc.)
3. Here, you will see some sections of code with:

![](figures/git/figure0A.png)

Once you have logged into GitKraken with you GitHub account, you will need to 
connect it to GitHub. The default GitKraken screen has a panel called 
"Integrations": click on GitHub. From here, there are two possibilities: if you 
click on "Connect to GitHub" it may take you to the SSO again and you can log in
that way (slightly repetitive). Or, if prompted to use the OAuth or Personal 
Access token, you can do the following: go to your "Settings" tab on GitHub, 
click on "Developer Settings", and then click on "Personal access tokens" to 
generate a token for 90 days, making sure to select "repo" (along with other 
scopes as needed).

![](figures/git/figure1A.png)

![](figures/git/figure1B.png)

![](figures/git/figure1C.png)

![](figures/git/figure2A.png)

![](figures/git/figure2B.png)

![](figures/git/figure2C.png)


Ideally, you should be able to automatically connect to GitHub without 
generating a personal access token, but GitKraken is moderately cursed.

Once you have successfully connected to GitHub, you will then need to generate 
an SSH key and add to GitHub. To do this, simply click the "Generate SSH key 
and add to GitHub" button (optionally adding a title to the SSH key if you 
wish). If this step is successful, you will receive a notification within 
GitKraken on the lower left, and your screen will now display the SSH key 
within GitKraken and under the Settings -> SSH and GPG keys tab on your GitHub:

![](figures/git/figure3A.png)
![](figures/git/figure3B.png)
![](figures/git/figure3C.png)

Congratulations, you should be successfully linked to the CIDA GitHub! 

From here, you can open, clone, and initiate repositories from the CIDA Github 
using the, you guessed it, Open a repo, Clone a repo, and Start a local repo 
options on the home screen:

![](figures/git/figure4A.png)

If you are going to clone a repo, just make sure you are on the GitHub.com 
section, and that you select the CIDA repository to clone, as well as where you 
would like to clone it to (H: or P: drives, or elsewhere). 

![](figures/git/figure4B.png)

First, however, you will need to generate another SSH key on GitKraken to add 
to your GitHub (at least this is the only way that I can figure). Go to 
Preferences -> SSH and then generate a new Private/Public Key, or copy the SSH 
Public Key if you already have one:

![](figures/git/figure4C.png)

Then return to your GitHub account, and click on SSH and GPG keys under the 
settings, click Add new key, and then copy the SSH key into the Key box. You 
will then need to Authorize it with the SSO. After that, you should be able to 
clone, open, and initialize your repos!

![](figures/git/figure4D.png)

Once you have cloned a repo, you can open it to push/pull any changes. This is 
done pretty simply via the push or pull commands on the top after opening the 
repo. 

![](figures/git/figure5A.png)

For more details on how to manage pull, push, branching, and other features, 
visit https://help.gitkraken.com/gitkraken-client/github-gitkraken-client/

---

![](figures/git/sph_cida_wm_blk.png)
