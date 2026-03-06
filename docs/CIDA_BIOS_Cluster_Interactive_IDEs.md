# Rstudio/JupyterLab On The CSPH Biostats Cluster

## Introduction

### L3 Heading

#### L4 Heading

This document will guide you through running interactive RStudio (and/or JupyterLab) sessions on the Biostats cluster.

Once configured, you'll be able to easily submit RStudio/JupyterLab SLURM jobs, and access them through your browser. 

We'll cover:

1. [First-time Setup](#first-time-setup) - Some one-time, prerequisite configuration steps on your local computer to enable connections to RStudio and JupyterLab.
2. [Launching RStudio Sessions](#launching-an-rstudio-session) - How to launch an RStudio session on the cluster and connect from your browser.
3. [Launching JupyterLab Sessions](#launching-a-jupyterlab-session) - How to launch a JupyterLab session on the cluster and connect from your browser.
4. [Quitting RStudio/JupyterLab Sessions](#quit-the-rstudiojupyterlab-session) - How to quit an RStudio/JupterLab session.
6. [(Optional) Additional Options](#optional-additional-options-and-job-customization) - Some additional options and information which may be useful.

If you've never used the `csphbiostats` cluster before, you'll need to request an account. Information on how to access the cluster is available in the [Accessing the CSPH Biostats Cluster](https://cida-csph.github.io/CIDAtools/articles/CIDA_BIOS_Cluster.html#accessing-the-csph-biostats-cluster) section of the main Biostats HPC article.

If you previously followed this guide to set up RStudio/JupyterLab and just need a refresher on how to launch an RStudio/JupyterLab job, check out the [Quickstart](#quickstart-for-returning-users) section.

### Motivation
Using RStudio/JupyterLab on the `csphbiostats` cluster allows you to:

- Use the cluster's significant [computational resources](https://cida-csph.github.io/CIDAtools/articles/CIDA_BIOS_Cluster.html#csph-biostats-hpc-cluster) to work with larger datasets than would be possible on a local machine, while coding interactively in a familiar environment.
- Offload time consuming analysis tasks from your local computer to the cluster (your RStudio/JupyterLab job will keep running on the cluster, even if you log out!)
- Running RMarkdown/Quarto/Jupyter Notebooks and generating reports directly from the cluster.
- Generate and view visualizations in real-time.

### A2. Capabilities

The RStudio container runs R 4.5.0, and supports the usual RStudio functions including RMarkdown/Quartio notebooks, interactive plotting, etc. For convenience, the RStudio container has a variety of commonly used packages pre-installed, including the `tidyverse` family, and also packages many system libraries needed for compiling R packages from source.

The JupyterLab container supports running Jupyter Notebooks (`.ipynb`), and supports all JupyterLab functions. By default, the JupyterLab container has the following kernels installed:

- Python 3.13
- R 4.5.0
- Julia 1.11.5


## B. Questions, Comments, Issues

This project is [hosted on GitHub here](https://github.com/CIDA-CSPH/Biostats-Cluster-Tools). 

If you have questions, encounter difficulties, or have suggestions for improvements, feel free to either [open an issue on GitHub](https://github.com/CIDA-CSPH/Biostats-Cluster-Tools/issues) or <a href="mailto:andrew.2.hill@cuanschutz.edu">email me directly</a>.

## 1. First-time Setup

Although the RStudio/JupyterLab instance will run on an HPC compute node, you'll log in to the cluster normally (via SSH), and access then RStudio/JupyterLab interface through your local browser.

In order for this to work correctly, we need to configure a few SSH options when logging in to the cluster. These SSH options should only need to be configured once.

### 1A. Locate SSH Config File

The simplest way to configure SSH connections is to use the SSH `config` file, which allows us to define persistent options that will be used each time we log in to the cluster (rather than having to remember which parameters to pass on the command line each time).

On Mac/Unix-like systems, this file is located at `~/.ssh/config`, and on Windows it is located at `C:/Users/<username>/.ssh/config`.

If you don't see a file named `config` in that location that's OK, just create it with your text editor of choice.

**Note:** Some GUI clients (like PuTTY on Windows) do not support port forwarding to Unix sockets (requried functionality to use RStudio/JupyterLab on the cluster). However, modern command-line versions of SSH on Mac and Windows do support this.

### 1B. Add SSH Configuration options

Open up the `config` file in your text editor of choice. If you had a pre-existing `config` file, check if you have an entry with `Host csphbiostats.ucdenver.pvt` or `HostName csphbiostats.ucdenver.pvt`. If you already have an entry you can modify it instead of creating a new entry. 

**IMPORTANT:** If you have an existing `config`, and there is an entry that begins with `Host *`, you should add the new configuration we make **above** the existing `Host *` section to ensure that our new configuration will take precedence.

#### 1B.1 SSH Config Template

Configure your entry to look something like the below entry template, replacing the three highlighted `your_username` placeholders with the username you use to log into the cluster with SSH:

<div class="sourceCode">
<pre><code>Host biostats
    HostName csphbiostats.ucdenver.pvt
    User <mark>your_username</mark>
    Port 22
    LocalForward 8895 /tmp/jupyter-<mark>your_username</mark>.sock
    LocalForward 8896 /tmp/rstudio-<mark>your-username</mark>.sock
</code></pre>
</div>

#### 1B.2 Fully-configured SSH Config Example

As an example, a fully-configured entry looks like this:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_ssh_2.png")


Once you've logged in via SSH, open a web browser on your local machine (but keep the SSH window open!) and enter:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/localhost_test.png")

Moving back to your SSH window, you should see some error messages populate the screen:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_ssh_local_forward_test.png")

If you see these error messages in your SSH window, Congratulations! 

This means you've configured SSH correctly! The error messages appear because the browser is attempting to connect, but there is nothing on the other end (yet) to accept the connection.

These error messages will continue to appear in your SSH window as long as you keep the `localhost:8895` browser tab open. Feel free to close the browser tab now and type `clear` in your SSH window to clear the messages from your terminal screen.


#### 1C.1 Troubleshooting

If you don't see the error messages in your SSH window:

1. Make sure the `localhost:<port>` you're visiting in browser matches one of the `LocalForward <port>` lines in your SSH config file. 
2. Check that you're logging in with the `ssh biostats` alias from your SSH config file.
3. Verify that these ports aren't being used by something else on your machine (i.e. a local Jupyter Notebook).


### 1D. Get Launch scripts

To launch an RStudio/JupyterLab session, you'll need a copy of the `rstudio_helper.sh` and `jupyter_helper.sh` scripts. These scripts help automate some of the setup for RStudio/JupyterLab sessions.

In your SSH window, navigate to your home directory (`cd ~`) and run:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_rstudio_launch.png")

This job will also produce two output files `rstudio_helper.out` and `rstudio_helper.err` which will log outputs or errors that the system encounters. 

If you *don't* see your Job ID in the `squeue` list, try inspecting the two above files for any error messages.

### 2A. Connect to RStudio

If you can see your RStudio job running in `squeue`, go back to your web browser and visit

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_rstudio_interface.png")

Congratulations! You can now use RStudio on the cluster!

Feel free to try out the interface and verify that everything works as expected. 

When you're finished, shut down the RStudio job by following the instructions in [Quit the RStudio/JupyterLab Job](#quit-the-rstudiojupyterlab-session)

#### 2A.1 Troubleshooting

If you *don't* see the RStudio interface in your browser:

1. Verify that you used the correct port in the browser. (If you used the default config, RStudio is `8896`).
2. Double check your SSH config file and make sure your `LocalForward` directives match the template from [1B.1 SSH Config Template](#b-1-ssh-config-template)
2. Run `squeue` again and verify that your job is still running. If the job is not running, check `rstudio_helper.err` and `rstudio_helper.out` for more information. 


### 2B. Customizing the RStudio Job

The `rstudio_helper.sh` script essentially just automates some cleanup tasks and submits a new `sbatch` batch script which launches RStudio.

If you open `rstudio_helper.sh` and scroll down to the `sbatch <<==SBATCH=SCRIPT==` section, you can customize the parameters of the underlying SLURM job to suit your needs:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_jupyter_launch.png")

This job will also produce two output files `jupyter_helper.out` and `jupyter_helper.err` which will log outputs or errors that the system encounters. 

If you *don't* see your Job ID in the `squeue` list, try inspecting the two above files for any error messages.

**IMPORTANT:** The first time you launch JupyterLab, it will create a Python `virtualenv` under `~/jupyterlab_env`. This process takes time (in my experience, up to 10 minutes). If you are unable to connect to your JupyterLab instance immediately after launching the job, don't worry! The setup process will log output to the output and error logs listed above.

### 3A. Connect to JupyterLab

If you can see your JupyterLab job running in `squeue`, go back to your web browser and visit 

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_jupyter_interface.png")

Congratulations! You can now use JupyterLab on the cluster!

Feel free to try out the interface and verify that everything works as expected. 

When you're finished, shut down the JupyterLab job by following the instructions in [Quit the RStudio/JupyterLab Job](#quit-the-rstudiojupyterlab-session)

#### 3A.1 Troubleshooting

If you *don't* see the JupyterLab interface in your browser:

1. Verify that you used the correct port in the browser. (If you used the default config, JupyterLab is `8895`).
2. Double check your SSH config file and make sure your `LocalForward` directives match the template from [1B.1 SSH Config Template](#b-1-ssh-config-template).
3. Run `squeue` again and verify that your job is still running. If the job is not running, check the `jupyter_helper.err` and `jupyter_helper.out` files for more information.
4. If you're launching JupyterLab for the first time, it could take up to 10 minutes for the script to initialize the `/jupyterlab_venv` virtual environment. If the job is running (via `squeue`) but you can't connect through your browser, try waiting ~10 minutes for environment to initialize.
    - After the venv setup is complete, future launches of JupyterLab through `./jupyter_helper.sh` should take only a few seconds.

### 3B. Customizing the JupyterLab Job

The `jupyter_helper.sh` script essentially just automates some cleanup tasks and submits a new `sbatch` batch script which launches JupyterLab.

If you open `jupyter_helper.sh` and scroll down to the `sbatch <<==SBATCH=SCRIPT==` section, you can customize the parameters of the underlying SLURM job to suit your needs:

[]("figures/CIDA_BIOS_Cluster_Interactive_IDEs/biostats_hpc_rstudio_diagram.png")

To facilitate a secure connection, each RStudio/JupyterLab job creates a link between your (local) computer and the compute node running the job via a pair of SSH tunnels.

The first SSH tunnel is configured locally on your machine (see the [First-time Setup](#first-time-setup) section above):

This SSH tunnel forwards any local traffic on `localhost:8895` or `localhost:8896` to specific Unix sockets (not ports) on the `csphbiostats` head node. We use Unix sockets for this since they:

1. Allow for file-like permissions (i.e. the socket is created and owned by your user, and cannot be accessed by others). 
2. Since Unix sockets are exposed as file-like objects, we can enforce unique naming (each Unix socket uses the user's name as part of the socket path) to prevent port conflicts.

The second SSH tunnel is opened by the RStudio/JupyterLab job on the compute node. Once the job begins executing on the compute node, the RStudio/JupyterLab launch script will:

1. Launch an RStudio/JupyterLab instance advertised on a Unix socket (again, we use Unix sockets instead of ports for the reasons listed above).
2. Open a background SSH tunnel to the `csphbiostats` node, which forwards all traffic on the `csphbiostats`'s Unix socket to the compute node's Unix socket (which is hosting the JupyterLab/RStudio instance).

In order for this to work seamlessly, the compute node needs to be able to SSH into the head node without prompting for a password. The launch script takes care of this by generating a SSH keypair (located at `~/.ssh/cluster_rsa`) which the compute node may use to log in to the head node. 

Together, these two SSH tunnels form a connection between your browser visiting `localhost:8895` or `localhost:8896` and the RStudio/JupyterLab instance running on the compute node. 

In summary, the container's launch script will:

1. Check if the SSH keypair `~/.ssh/cluster_rsa` exists. 
    - If not, the launch script will automatically create this keypair and use it for future job launches.
2. Check if your job is running on the head node `csphbiostats` or a compute node (any node which is not `csphbiostats`)
    - In the event that the job is running on `csphbiostats`, we don't need the second SSH tunnel, as your local machine will already forward traffic directly to the configured Unix socket.
3. Launch the RStudio/JupyterLab instance. 

