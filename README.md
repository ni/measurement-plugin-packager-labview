# Measurement builder tool for LabVIEW

This repository contains the source code and the workflow for measurement builder tool in LabVIEW.

## Table of Content

- [Measurement builder tool for LabVIEW](#measurement-builder-tool-for-labview)
  - [Overview](#overview)
    - [Builder tool for LabVIEW](#builder-tool-for-labview)
  - [Software Dependencies](#software-dependencies)
  - [Getting Started](#getting-started)
  - [Create and Update NI Package Manager Feeds](#create-and-update-ni-package-manager-feeds)

## Overview

## Builder tool for LabVIEW

A measurement plug-in in LabVIEW comes with two build specifications, one is PPL for the measurement UI, and the other is EXE for the measurement logic. The measurement EXE build specification has post-build action VI, which makes the creation of an installer or package difficult for the users. The measurement builder tool solves the problem by providing an easy way to build measurement plug-in service as an NI package.

## Software Dependencies

- LabVIEW 2021 SP1 or later

## Getting Started

- You can refer to the [Measurement Reuse HLD](https://github.com/ni/measurement-builder-tool/blob/main/docs/Measurement%20Builder%20HLD/Measurement%20Reuse%20HLD.md) to understand the workflow for measurement reuse in LabVIEW.

## Create and Update NI Package Manager Feeds

- Packages for various measurement plugins are incorporated into an NI Package Manager feed,
  allowing users to install new packages or receive updates to existing ones by subscribing to the
  feed.

- The feeds for measurement plugins are maintained under the attached repo.
[`package-manager-feeds`](https://github.com/NI-MeasurementLink-Plug-Ins/package-manager-feeds).

- Please follow the procedure mentioned in the attached document for adding new packages or updating new
  versions of existing packages to the feed
  [`README.md`](https://github.com/NI-MeasurementLink-Plug-Ins/package-manager-feeds/blob/main/package-feed-updater/README.md).
