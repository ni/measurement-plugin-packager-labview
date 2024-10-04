# Measurement builder tool for LabVIEW

This repository contains the source code for the Measurement Builder tool which helps to build NI packages for the LabVIEW measurement plug-ins.

## Table of Content

- [Measurement builder tool for LabVIEW](#measurement-builder-tool-for-labview)
  - [Overview](#overview)
    - [Builder tool for LabVIEW](#builder-tool-for-labview)
  - [Software Dependencies](#software-dependencies)
  - [Getting Started](#getting-started)

## Overview

### Builder tool for LabVIEW

A LabVIEW measurement plug-in comes with two build specifications: a PPL for the measurement UI, and an EXE for the measurement logic. The measurement EXE build specification has a post-build action VI, which makes the installer or package creation difficult for the users. The measurement builder tool solves this problem by providing an easy way to build measurement plug-ins as NI packages.

## Software Dependencies

- [LabVIEW 2021 SP1 or later](https://www.ni.com/en/support/downloads/software-products/download.labview.html#443865)
- [Measurement Plug-In SDK for LabVIEW 3.0.0.3](https://github.com/ni/measurement-plugin-labview/releases/tag/v3.0.0.3)

## Getting Started

- You can refer to the [Measurement Plug-in Builder User Manual](https://github.com/ni/measurement-builder-tool/releases/download/v2.0.0.1/Measurement_Plug-in_Builder_User_Manual.pdf) to understand the workflow for measurement reuse in LabVIEW.
