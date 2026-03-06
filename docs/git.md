# Tracking Code In Git/github

[]("figures/git/sph_cida_wm_blk.png")

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

[]("figures/git/figure0A.png")

Once you have logged into GitKraken with you GitHub account, you will need to 
connect it to GitHub. The default GitKraken screen has a panel called 
"Integrations": click on GitHub. From here, there are two possibilities: if you 
click on "Connect to GitHub" it may take you to the SSO again and you can log in
that way (slightly repetitive). Or, if prompted to use the OAuth or Personal 
Access token, you can do the following: go to your "Settings" tab on GitHub, 
click on "Developer Settings", and then click on "Personal access tokens" to 
generate a token for 90 days, making sure to select "repo" (along with other 
scopes as needed).

[]("figures/git/figure1A.png")

Ideally, you should be able to automatically connect to GitHub without 
generating a personal access token, but GitKraken is moderately cursed.

Once you have successfully connected to GitHub, you will then need to generate 
an SSH key and add to GitHub. To do this, simply click the "Generate SSH key 
and add to GitHub" button (optionally adding a title to the SSH key if you 
wish). If this step is successful, you will receive a notification within 
GitKraken on the lower left, and your screen will now display the SSH key 
within GitKraken and under the Settings -> SSH and GPG keys tab on your GitHub:

[]("figures/git/figure3A.png")

Congratulations, you should be successfully linked to the CIDA GitHub! 

From here, you can open, clone, and initiate repositories from the CIDA Github 
using the, you guessed it, Open a repo, Clone a repo, and Start a local repo 
options on the home screen:

[]("figures/git/figure4A.png")

If you are going to clone a repo, just make sure you are on the GitHub.com 
section, and that you select the CIDA repository to clone, as well as where you 
would like to clone it to (H: or P: drives, or elsewhere). 

[]("figures/git/figure4B.png")

First, however, you will need to generate another SSH key on GitKraken to add 
to your GitHub (at least this is the only way that I can figure). Go to 
Preferences -> SSH and then generate a new Private/Public Key, or copy the SSH 
Public Key if you already have one:

[]("figures/git/figure4C.png")

Then return to your GitHub account, and click on SSH and GPG keys under the 
settings, click Add new key, and then copy the SSH key into the Key box. You 
will then need to Authorize it with the SSO. After that, you should be able to 
clone, open, and initialize your repos!

[]("figures/git/figure4D.png")

Once you have cloned a repo, you can open it to push/pull any changes. This is 
done pretty simply via the push or pull commands on the top after opening the 
repo. 

[]("figures/git/figure5A.png")

For more details on how to manage pull, push, branching, and other features, 
visit https://help.gitkraken.com/gitkraken-client/github-gitkraken-client/

---

[]("figures/git/sph_cida_wm_blk.png")
