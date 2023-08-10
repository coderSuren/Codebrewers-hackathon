# Tally's Codebrewers hackathon
## Theme - Wizard of System Programming
# Disk Space Manager 
## Table of Contents
- [Introduction](#introduction)
- [Quick Demo](#quick-demo) 
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Welcome to Disk Space Management App! This Python application is built using the Tkinter library and provides a user-friendly interface to scan for duplicate files and manage system memory efficiently. With this app, you can quickly locate and remove duplicate files, freeing up infrequently accessed files, and viewing disk memory utilization based on drive, directory, file types, etc.

## Quick Demo
Explore the application by running the [gui.exe](https://github.com/coderSuren/Codebrewers-hackathon/releases/tag/v1.0.1) file
  
## Installation

Follow these steps to set up and run the application:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/coderSuren/Codebrewers-hackathon.git
   cd Codebrewers-hackathon
   ```
2. Ensure you have Python 3.x installed on your system. If not, download and install it from [Python's official website](https://www.python.org/downloads/).

3. Install the required dependencies:

   ```bash
   pip install tkinter
   pip install customtkinter
   pip install wmi
   pip install PIL
   ```

4. Run the app:

   ```bash
   python components/gui.py
   ```

## Usage

1. **Duplicate File Scanner**
   - Select the directory or drive you want to scan for duplicate files.
   - Click on the "Scan" button to start the scanning process.
   - After the scan is complete, a list of duplicate files will be displayed with options to delete them.
   - Customize scan options (hashing algorithms) in the settings menu as needed.

2. **Disk Utilization By Drive, Path, File Type**
   - Start the disk scanning by clicking the "Get Disk Utilization" button.
   - After the scan is complete, a list of drives with utilization will be displayed.

3. **Large Files Detector**
   - Select the directory or drive you want to scan for Large files.
   - Click on the "List Files" button to start the scanning for files.
   - After the scan is complete, a list of large files will be displayed with options to delete them.
   - Customize the File size limit in the settings menu.

4. **Infrequent Files Detector**
   - Select the directory or drive you want to scan for infrequent files.
   - Click on the "Get Infrequent Files" button to start the scanning process.
   - After the scan is complete, a list of duplicate files will be displayed with options to delete them.
   - Customize the File accessed time range in the settings menu
   
## Screenshots
|Duplicate Files Detector|Disk Utilization (By Drive)|
|:-------:|:-------:|
|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/44deda1e-6254-4a5f-a81d-4e4017b10424)|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/1dd6005d-d109-4ca3-995e-1115e92f4e2d)|
|Disk Utilization (By Type)|Large Files Detector|
|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/1cf38858-8aba-4b3c-b896-366b59d3360d)|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/9e8cd9bb-0442-4060-8098-5d27fe4904b6)|
|Infrequent Files Detector|Settings (hash function)|
|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/c1163d17-968a-4a41-b863-fa000d6f01cf)|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/7fc42b22-21f0-4dd2-87d7-ffd7c9f7e835)|
|Settings (More options)|Light Theme|
|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/5bf6856e-febe-4ea0-bb5a-3372f0275197)|![image](https://github.com/coderSuren/Codebrewers-hackathon/assets/80509210/fad59f2e-d591-43d5-9ce7-21c243bf80a0)|

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute this project following the terms of the MIT License.
