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

A measurement plug-in in LabVIEW comes with two build specifications, one is PPL for the measurement UI, and the other is EXE for the measurement logic. The measurement EXE build specification has post-build action VI, which makes the creation of an installer or package difficult for the users. The measurement builder tool solves the problem by providing an easy way to build measurement plug-in service as an NI package.

## Software Dependencies

- [LabVIEW 2021 SP1 or later](https://www.ni.com/en/support/downloads/software-products/download.labview.html#443865)
- [Measurement Plug-In SDK for LabVIEW 3.0.0.3](https://github.com/ni/measurement-plugin-labview/releases/tag/v3.0.0.3)

## Getting Started

- You can refer to the [Measurement Plug-in Builder User Manual](https://github.com/ni/measurement-builder-tool/releases/download/v2.0.0.1/Measurement_Plug-in_Builder_User_Manual.pdf) to understand the workflow for measurement reuse in LabVIEW.
