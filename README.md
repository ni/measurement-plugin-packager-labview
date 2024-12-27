# Measurement Plug-In Packager for LabVIEW

- [Measurement Plug-In Packager for LabVIEW](#measurement-plug-in-packager-for-labview)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Launching Measurement Plug-in Packager](#launching-measurement-plug-in-packager)
    - [Packaging Measurement Plug-in](#packaging-measurement-plug-in)
    - [Editing Configurations](#editing-configurations)
  - [Known Issues](#known-issues)

## Introduction

A LabVIEW measurement plug-in comes with two build specifications: a PPL for the measurement UI, and an EXE for the measurement logic. The measurement EXE build specification has a post-build action VI, which makes the installer or package creation difficult for the users. The measurement builder tool solves this problem by providing an easy way to build measurement plug-ins as NI packages.

## Dependencies

- [LabVIEW 2021 SP1 or later](https://www.ni.com/en/support/downloads/software-products/download.labview.html#443865)
- [Measurement Plug-In SDK for LabVIEW 3.0.0.3](https://github.com/ni/measurement-plugin-labview/releases/tag/v3.0.0.3)
- [JKI VI Package Manager 2021 SP1 or later](https://www.ni.com/en/support/downloads/tools-network/download.jki-vi-package-manager.html#443251)

## Installation

1. Download the required VI package file (.vip) from the latest release:
    - `ni_measurement_plugin_packager-X.X.X-X.vip`
2. Install the package using VI Package Manager.

## Usage

### Launching Measurement Plug-in Packager

1. Open `LabVIEW` → `Tools` → `Plug-In SDKs` → `Measurements` → `Package Measurement Plugin`  
    ![PackgeMeasurement](./docs/Measurement%20Builder%20HLD/PackageMeasurement.png)

### Packaging Measurement Plug-in

1. Select the LabVIEW project which contains the measurement plug-ins.
2. Check the `Open the target directory post build` checkbox to open the build directory post build.
3. Check the `Build package for measurements` checkbox to create packages. If unchecked, then measurements will be built into EXE.
4. To create a new feed for the packages, select “Create New Feed” Option
5. To add the packages to the existing feed, select “Add to existing feed” and select the feed directory.  
    ![AddtoFeed](./docs/Measurement%20Builder%20HLD/AddtoFeed.png)
6. To skip feed creation, deselect both the options.  
    ![Package Measurement](./docs/Measurement%20Builder%20HLD/PackageMeasurement.png)
7. Click the `Next` button
8. Select the measurements to be package and click the `Next` button.  
    ![Measurement Selection](./docs/Measurement%20Builder%20HLD/Measurement_Selection.png)
9. (Optional) Click on the cell to edit the package version. The measurement name cannot be edited.  
    ![Package Versioning](./docs/Measurement%20Builder%20HLD/Package_Versioning.png)
10. Click `Build` to start packaging.
11. Once packaging is complete, the build status will be displayed and the File explorer will be opened based on `Open the target directory post build`.
    ![Build Status](./docs/Measurement%20Builder%20HLD/Build_Status.png)
12. (Optional) Post build, publish the feed/packages in the public repo/SLE.
13. (Optional) To install the packages, refer [Installing Packages from a Feed](https://www.ni.com/docs/en-US/bundle/package-manager/page/install-packages-from-feed.html#:~:text=In%20the%20Add%20feed%20dialog,to%20view%20all%20available%20packages).

### Editing Configurations

1. Open the `C:\ProgramData\National Instruments\Measurement
Builder\Configuration.ini`  
    ![BuilderConfiguration](./docs/Measurement%20Builder%20HLD/BuilderConfiguration.png)

2. Change architecture to support 32 bits. Supported options are shown:
below.
    - 32 – to build package in 32 bits
    - 64 – to build package in 64 bits
    - Both – to build packages in both architectures.
3. Edit the maintainer’s name and email address if required.

## Known Issues

1. When more measurements are available, clicking the scrollbar selects/deselects the measurements.
2. Measurement name starting with `ni-` package build will fail.
