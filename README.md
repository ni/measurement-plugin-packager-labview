# Measurement Plug-In Packager for LabVIEW

- [Measurement Plug-In Packager for LabVIEW](#measurement-plug-in-packager-for-labview)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Editing Configurations](#editing-configurations)
  - [Usage](#usage)
    - [Launching the Measurement Plug-in Packager](#launching-the-measurement-plug-in-packager)
    - [Packaging LabVIEW Measurement Plug-in(s)](#packaging-labview-measurement-plug-ins)
  - [Known Issues](#known-issues)

## Introduction

The Measurement Plug-In Packager simplifies the creation of NI package files (.nipkg) for LabVIEW measurement plug-ins. This tool enhances efficiency by streamlining the process of building and distributing measurement plug-ins.

## Dependencies

- [LabVIEW 2021 SP1](https://www.ni.com/en/support/downloads/software-products/download.labview.html#443865)  or later
- [Measurement Plug-In SDK for LabVIEW 3.0.0.3](https://github.com/ni/measurement-plugin-labview/releases/tag/v3.0.0.3) or later
- [JKI VI Package Manager 2021 SP1](https://www.ni.com/en/support/downloads/tools-network/download.jki-vi-package-manager.html#443251) or later

## Installation

1. Download and install the `ni_measurement_plugin_packager-X.X.X-X.vip` package from the latest release assets.

## Editing Configurations

To edit the configuration required for the LabVIEW measurement plug-in packager:

1. Open the `C:\ProgramData\National Instruments\Measurement
Builder\Configuration.ini`  
    ![BuilderConfiguration](./docs/Measurement%20Builder%20HLD/BuilderConfiguration.png)

2. Change architecture to support 32 bits. Supported options are shown below:
    - 32 – to build package in 32 bits
    - 64 – to build package in 64 bits
    - Both – to build packages in both architectures.
3. Edit the maintainer’s name and email address if required.

## Usage

### Launching the Measurement Plug-in Packager

1. Open `LabVIEW` → `Tools` → `Plug-In SDKs` → `Measurements` → `Package Measurement Plug-in...`  
    ![PackgeMeasurement](./docs/Measurement%20Builder%20HLD/PackageMeasurement.png)

### Packaging LabVIEW Measurement Plug-in(s)

1. Choose the LabVIEW project that contains the measurement plug-ins to package.
2. Enable the "Open the target directory post build" checkbox to automatically open the build directory after the build process is complete
3. To create a new NIPM feed for the package(s), select the "Create New Feed" option.
4. Else, to add the package(s) to an existing NIPM feed, select the ''Add to Existing Feed'' option, and specify the feed directory.  
    ![AddtoFeed](./docs/Measurement%20Builder%20HLD/AddtoFeed.png)
5. To bypass feed creation, ensure that both the "Create New Feed" and "Add to Existing Feed" options are deselected.  
    ![Package Measurement](./docs/Measurement%20Builder%20HLD/PackageMeasurement.png)
6. Click the `Next` button to continue
7. Select the measurements to be packaged and click the `Next` button.  
    ![Measurement Selection](./docs/Measurement%20Builder%20HLD/Measurement_Selection.png)
8. If needed, you can edit the package version of the measurement plug-in. Note that the measurement name cannot be modified.  
    ![Package Versioning](./docs/Measurement%20Builder%20HLD/Package_Versioning.png)
9. Click `Build` to start the packaging process.
10. After the packaging is complete:
    - The build status will be displayed.
    - If the "Open the target directory post build" option is enabled, the File Explorer will open the build directory.  
    ![Build Status](./docs/Measurement%20Builder%20HLD/Build_Status.png)

### Note

1. Once the build is complete, you can publish the feed or packages to a public repository or SystemLink, if desired.
2. (Optional) To install the packages from feed, refer [Installing Packages from a Feed](https://www.ni.com/docs/en-US/bundle/package-manager/page/install-packages-from-feed.html#:~:text=In%20the%20Add%20feed%20dialog,to%20view%20all%20available%20packages).

## Known Issues

1. When more measurements are available, clicking the scrollbar selects/deselects the measurements.
2. Measurement name starting with `ni-` package build will fail.
