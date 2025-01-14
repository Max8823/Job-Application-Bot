


# Job Application Bot



This Bot is used to automate the process of applying for jobs on various sites such as
<br><br>
<a href="https://LinkedIn.com/" target="_blank">LinkedIn</a>
<br>
<a href="https://seek.com.au/" target="_blank">Seek</a>
<br>
<a href="https://au.gradconnection.com/" target="_blank">GradConnection</a>
<br> <br>




# Table of Contents
- [Installation](#installation)
- [Usage](#usage)


# Installation
[(Back to top)](#table-of-contents)

1. Check what version of chrome is running and download the corresponding version from 
<a href="https://googlechromelabs.github.io/chrome-for-testing/" target="_blank">Here</a>

To find the current version of chrome enter the following into the browser
```shell
chrome://settings/help
```
<br>
2. Create a new Chrome profile a guide can be found <a href="https://support.google.com/chrome/answer/2364824?hl=en&co=GENIE.Platform%3DDesktop" target="_blank">Here</a>

<br><br>
3. sign into gmail with the new chrome profile.
<br><br><br>
4. Move the profile folder located at the destination below to a new directory

C:\Users\{user}\AppData\Local\Google\Chrome\User Data
<br><br>
*note the first profile is named 'Default' the 2nd is named 'Profile 1' and so on*
<br><br>

5. Clone repo
```shell
git clone https://github.com/Max8823/Job-Application-Bot
```
<br><br>
6. Change values in Settings.YAML to reflect job preferences, login details, minimum salary, ect <br><br>


# Usage
[(Back to top)](#table-of-contents)

The app is fully automated including login / signup, generation of cover letters, Database logging to ensure the same job isn't applied for twice across different sites.

