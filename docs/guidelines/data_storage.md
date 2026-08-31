#CIDA Data Storage Guidelines


## CIDA Data Storage Tools 

### Introduction

This document provides guidelines, recommendations, and current best practices for where code, data, and other documents should be stored and backed up for members of CIDA. These guidelines are intended to explain the pros, cons, and best practices for the data storage tools available to CIDA members. However, a CIDA member may come across exceptions to these guidelines, and the responsibility for proper data handling within a particular project rests on the CIDA member involved.  

Who does this apply to: All members of CIDA (Professor, RA, RI, Senior RI, PRA, Senior PRA)

### Definitions

* **Code** refers to any R, SAS, Stata, etc. (scripts stored as plain text formatted files)
* **Data** refers to spreadsheets, tables, or other information used to run analysis on
* **Report** refers to any document which outlines results of analysis for sending to an investigator
* **PHI** refers to Protected Health Information which is any healthcare data that can be use to identify an individual
* **PII** refers to Personally Identifiable Information which is any data that can be used to distinguish or trace an individual's identity
* **File System** refers to any place where files or data can be stored but has no compute ability
* **Local storage** refers to any university provided computer with a physical hard drive 
* **External server** refers to any server which houses data or runs analysis that isn't a personal computer
* **P-drive** a.k.a the **CIDA (P) Drive** is PHI compliant storage where most CIDA data should be stored. This is officially known as the **Isilon Central File Server**
* **GitHub** is the official repository CIDA should keep code, available [here](https://github.com/CIDA-CSPH) (requires VPN connection)
* **OneDrive for Business** refers to Microsoft’s file-syncing software licensed by the University
* **PetaLibrary** is a large file system that is accessible to Research Computing Tools like Alpine. this is not a PHI compliant storage solution. More information can be found [here](https://www.colorado.edu/rc/resources/petalibrary)
* **Eureka** is the Virtual Machine run by Health Data Compass (HDC)
* **HPC** refers to “High Performance Computing” such as [Alpine](https://www.colorado.edu/rc/alpine).
* **SLCE** refers to Secure Local Compute Environment and are PHI/HIPPA compliant, more information can be found [here](https://medschool.cuanschutz.edu/informationservices/research/slce)


### Data Storage Locations Available to CIDA Members

#### Local Storage

*	All files for any current projects can be stored on a University provided PC or Macintosh, if and only if the computer’s hard drive is encrypted. 
*	Data with PHI/PII should only be locally stored during active work on a project.
*	Pros: data and projects load more quickly when stored locally. 
*	Cons: no natural/default backup process, can be a hassle to do best security practices manually.
*	Best Practices: 
    * Only keep project data on your computer while working on it, and if you do this often, ensure you frequently save your data to the CIDA drive. 
    * Prior to travel with a laptop, any old or unneeded projects should be removed from the computer drive and can be restored upon return to campus.

#### CIDA (P) Drive 

* This drive is officially called the *Isilon Central File Server* in SOM-IT documentation
* Mapping depends on operating system. See instructions here for mapping drives.
    * MAC: `smb://data.ucdenver.pvt/dept/SPH/SPH-CIDA` 
    * Windows: `\\data.ucdenver.pvt\dept\SPH\SPH-CIDA`
    * If you have recently started and are having trouble mapping this drive, contact [SOM-IT](https://medschool.cuanschutz.edu/informationservices). 
* CIDA project data must be stored here on a permanent basis (with certain exceptions, e.g., projects with large data or if the collaboration dictates otherwise). 
* The storage under the CIDA Drive is set up as follows:
    * `SPH-CIDA/Branches`: Long-standing collaborations, including those operating under MOUs, are treated as Branches, and their data should be stored in a subdirectory of CIDA/Branches. 
    * `SPH-CIDA/CIDA/Shared`
        * The CIDA/Shared directory is accessible to all CIDA members who have gained approval from a data manager. Folders are also accessible to external users who have been approved for access. 
        * Files and directories that you create on the shared drive inherit their permissions from their parent folder. You cannot restrict access to specific directories in accordance with data use agreements without the help of IT. 
* Use the following links to [Request to Create a CIDA (P) Folder](https://app.smartsheet.com/b/form/d1d93ae08f4349d48654950eea9b5bbd) or to [Update an Existing CIDA (P) Drive Folder](https://app.smartsheet.com/b/form/c22bbec56f8d4607bedc441be60bf8c8)
* Pros: 
    * All files and directories are backed up nightly; backups are stored for 30 days. 
    * Collaboration and transfers of data among CIDA members can be quick and easy.
    * Data and code are easily findable by CIDA administration and other team members in the case of a CIDA member’s continued absence.
* Con: working directly on this drive can be slow, especially through a VPN.
* Best Practices: 
    * Up-to-date raw data for all projects should be available in their expected location on this drive at least weekly, and especially at project conclusion, or prior to a project not being actively worked on.
    * Eliminate redundancies and intermediate data sets in projects with “big” data; only store the data you need to make code and reports run. 
* CIDA pays for this server storage on a [per-GB-month basis](https://www.cuanschutz.edu/offices/office-of-information-technology/tools-services/storage-servers-and-backups), so be cognizant of the size of the data utilized by your projects. If a project requires storing over 100 GBs of data work with your supervisors or the head of the MOU to determine if extra fees need to be collected for the project.
* For long term archiving of projects, CIDA members should should consider applying lossless compression to files.

#### OneDrive for Business

* OneDrive for Business is a hybrid local and cloud storage system that allows for up to 5TB of cloud storage. Note there are limitations on individual file sizes and types. 
* Unlike the CIDA drive, files and directories saved to the OneDrive directory are private by default and are backed up to the cloud.
* OneDrive for Business is HIPAA compliant. OIT and SOM-IT can access folders created on the directory, but only after a manager enters a data access request that gets approved by HR.
* Files can be downloaded to your local computer from the cloud on an as-needed basis off-site, which ensures a limited amount of data is stored locally. 
* Files can also be shared with other individuals with @cuanschutz.edu email addresses via OneDrive for Business. 
* Things to be aware of:
    * Do not confuse this with a personal OneDrive account! 
    * Do not install OneDrive for Business on an unencrypted or personal computer. Files may sync (and be downloaded) to the local computer, which would leave potentially sensitive data vulnerable. 
    * Concurrent use of OneDrive for Business in directories tracked by Git can lead to some syncing issues with OneDrive. This can typically be solved by restarting OneDrive.
    * Relevant project data stored in OneDrive should be copied over to the CIDA (P) Drive regularly, especially when projects become inactive.
    * Certain institutions and groups may have policies against using OneDrive for Business, so please verify with your research group that it is acceptable for your data to live there. 
	
#### GitHub

*	In general, GitHub should be used for everything, except for data. While tracking small data sets in Git and pushing to GitHub is usually harmless, tracking data sets in Git can snowball the storage needed in GitHub and also slow down your git commands.  
*	Please consult the following guidelines for more information
    * [CIDA's Coding Guidelines](../guidelines/coding_guidelines.md)
	* [CIDA's Intro to Github](../git/git.md)
*	All repositories on GitHub should be updated frequently, but especially prior to leaving on vacation or any other extended time out of office.

#### Eureka by Health Data Compass (HDC)

*	Any patient level data on Eureka should only be moved off of the Google Cloud with explicit permission from HDC for that specific project and data.
*	Raw data or data with PID should not be copied over to any other location except those approved by HDC.
*	Backups of code, reports, and other files should still be copied over to the CIDA drive so that it is accessible to others in CIDA in case of an emergency. 
*	For projects requiring Eureka, the [Eureka Cost Estimator](https://research.cuanschutz.edu/healthdatacompass/home/eureka-cloud-analytics/eureka-pricing) can be used to determine the expected costs of a particular project a priori. These costs should be charged to the project’s PI if possible.

#### Additional External File Systems and Servers

For more information about the following, please visit the links, contact SOM-IT or contact the Research Tools committee

* [Petalibrary](https://www.colorado.edu/rc/resources/petalibrary) - a file system that can mount to the Alpine HPC. Cost of Petalibrary can be found [here](https://curc.readthedocs.io/en/latest/petalibrary/allocation_types.html)
* [Google Workspace](https://www.cuanschutz.edu/offices/office-of-information-technology/tools-services/google-workspace) - Some CIDA members might have access to the University of Colorado managed Google Workspaces
* [CIDA-BIOS HPC](../computing/CIDA_BIOS_Cluster.md) - HIPPA compliant HPC that is considered a SLCE server.
* For very large data, contact SOM-IT for solutions
* SOM-IT also offers cloud storage and computing (either Google Cloud or Microsoft Azure). These systems are pay-as-you-use and can be quite expensive and not often compatible with PHI/PII data.

Care should be taken that data living on an external server remain on the external server. However, code, reports, and any other files necessary to the project should still be copied to the CIDA drive at regular intervals (exceptions may exist, e.g., if other processes are specified in CIDA’s memorandum of understanding with your research group).

#### Unapproved data storage options

*	__Only the options listed above are approved by CIDA for temporary data storage, and only the CIDA drive is approved for ongoing data storage__. Please follow the best practices and ask questions if you have them.
*	__The following non-exhaustive list of data storage options are not approved by CIDA__: 
    * Dropbox
    * OneDrive (personal)
    * Unencrypted hard drive or flash drive

### Data Transfer Options

| Mode of transfer | Notes |
| --- | --- |
| CIDA drive | For transfers among CIDA members, the CIDA drive can be used for data transfer | 
| OneDrive for Business | University-preferred means of transferring data |
| Redcap | Web-based, useful for ongoing projects where data updates are more frequent, ensures data format stays more consistent |
| External hard/flash drive | Acceptable: CIDA’s 48 TB NAS station, or an encrypted flash drive. Unacceptable: Unencrypted drive, even if the file is password protected |
| Email | Email is not an encouraged means of transferring data and should be done in circumstances when no other approach is available. Note that although email between CU-affiliated email addresses are automatically encrypted, this is not the case for external emails. You can manually encrypt by putting one of these keywords in brackets in the subject of an email: secure, safemail, or encrypt. Email from any other email system, such as gmail, is not acceptable. |
| Not acceptable | Non-approved web-based systems including: Dropbox and unencrypted flash/hard drives, even if the file is password protected. Email from any other email system, such as gmail | 

When transferring data it is often a good idea to setup checks to make sure files have not been corrupted or altered. An an example of this can be seen [here](https://tombuntu.com/index.php/2007/12/21/how-to-use-md5sum-to-verify-data-integrity/)

### Useful Links

Health Insurance Portability and Accountability Act (HIPAA):  
http://www.hhs.gov/hipaa/for-professionals/index.html

Health Information Technology for Economic and Clinical Health (HITECH):  
http://www.hhs.gov/hipaa/for-professionals/special-topics/HITECH-act-enforcement-interim-final-rule/index.html

Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule:  
http://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html
