# Measurement Plug-In Packager for LabVIEW

- [Measurement Plug-In Packager for LabVIEW](#measurement-plug-in-packager-for-labview)
  - [Introduction](#introduction)
  - [Software support](#software-support)
  - [Installation](#installation)
  - [Editing Package Configuration](#editing-package-configuration)
  - [Packaging LabVIEW Measurement Plug-in(s)](#packaging-labview-measurement-plug-ins)
    - [Note](#note)
  - [Limitations](#limitations)

## Introduction

The Measurement Plug-In Packager simplifies the creation of NI package files (.nipkg) for LabVIEW
measurement plug-ins. This tool enhances efficiency by streamlining the process of building and
distributing measurement plug-ins.

## Software support

- [LabVIEW 2021 SP1](https://www.ni.com/en/support/downloads/software-products/download.labview.html#443865)  or later
- [JKI VI Package Manager 2021 SP1](https://www.ni.com/en/support/downloads/tools-network/download.jki-vi-package-manager.html#443251) or later

## Installation

Download and install the `ni_measurement_plugin_packager-X.X.X.X.vip` package from the latest
release assets.

## Editing Package Configuration

- The Packager requires user information such as the `MaintainerName`, `MaintainerEmail`, and
  `Architecture` to configure the properties of the NI Packages to be built.
- During the tool installation, these details are updated based on your PC's information in the file
  `C:\ProgramData\National Instruments\Measurement Plugin Packager\Configuration.ini`.

  ![Packager Configuration](./docs/images/Configuration%20File.png)

- If required, you can edit these details to customize the properties of the NI packages built by
  the tool.

**Note:**

- Supported `Architecture` options are:
  - 32 - to build package for 32-bit systems
  - 64 - to build package for 64-bit systems
  - Both - to build package for both 32-bit and 64-bit systems, ensuring compatibility with any
    system architecture
- If these fields are not updated, the default values will be used for packaging the measurement
  plug-ins.

## Packaging LabVIEW Measurement Plug-in(s)

1. Open LabVIEW and navigate to `Tools` → `Plug-In SDKs` → `Measurements` → `Package Measurement
   Plug-in...`.

    ![Measurement Plug-In Packager Tool dialog](./docs/images/Measurement%20Plug-In%20Packager%20dialog.png)

2. In the dialog, select the LabVIEW project that contains the measurement plug-ins to package.  
   Note:
   - If the tool is launched from a project window, the "LabVIEW Project Path" field will be
     automatically populated with the active project path.
   - The "Open the target directory post build" checkbox is enabled by default to open the packages
     directory upon completion of the build process. If needed, you can disable this option.

3. You can create or update a NIPM feed as part of the measurement plug-in packaging,
   - To create a new NIPM feed for the packages, select the "Create New Feed" option.
   - Else, to add the packages to an existing NIPM feed, select the "Add to Existing Feed" option,
     and specify the feed directory.

      ![Add to Feed](./docs/images/Add%20to%20Feed%20Option.png)

   - To bypass feed creation, ensure that both the "Create New Feed" and "Add to Existing Feed"
     options are deselected.

      ![No Feed](./docs/images/Measurement%20Plug-In%20Packager%20dialog.png)

4. Click on the `Next` button to view the measurement plug-ins available in the selected project.
    - In the list, select the measurement plug-ins to be packaged and click `Next`.

      ![Measurement Selection](./docs/images/Measurement%20Selection.png)

5. Review the package version information of the selected measurement plug-ins and edit if required.

      ![Version Information](./docs/images/Version%20Information.png)

6. Click on the `Package` button to start the packaging process.
7. After the packaging is complete:
    - The packaging status will be displayed.
    - If the "Open the target directory post build" option is enabled, the File Explorer will open
      the packages directory.

      ![Packaging Status](./docs/images/Packaging%20Status.png)

### Note

1. Once the packaging is complete, you can publish the feed or packages to a public repository or
   SystemLink, if desired.
2. To install the packages from feed, refer to [Installing Packages from a
   Feed](https://www.ni.com/docs/en-US/bundle/package-manager/page/install-packages-from-feed.html#:~:text=In%20the%20Add%20feed%20dialog,to%20view%20all%20available%20packages).

## Limitations

The packaging process will fail for measurement plug-ins whose destination directory names
configured in their respective EXE Build Specifications are prefixed with 'ni-', regardless of case
sensitivity.
