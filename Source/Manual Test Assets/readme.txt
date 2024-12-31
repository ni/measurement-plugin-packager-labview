The 'Measurement.lvproj' contains 3 example measurement plug-ins to help with the manual testing of
the 'Measurement Plug-In Packager' tool.

niScope EX Getting Started:
- The 'niScope EX Getting Started' is a measurement VI converted into a measurement plug-in using the
'Measurement Plug-In Converter' tool. The base measurement can be found in the LabVIEW Example
Finder under the same name, 'niScope EX Getting Started.vi'.

- This example demonstrates the minimal code required to use NI-SCOPE. The converted measurement
plug-in contains a 'Waveform Graph' control in its 'Measurement Results.ctl'.

- This measurement service cannot be run due to the presence of an invalid datatype in the control,
and it is expected to fail during the package build process.

Sample:
- This measurement plug-in is generated using the 'Measurement Plug-In Generator' tool. It is a basic
loopback measurement, and the package build for this plug-in should be successful.

Z Power Module:
- The 'Z Power Module' measurement plug-in is also a measurement converted into a plug-in using the
Converter tool.

- This example demonstrates how to acquire a single buffer of power measurements using a DAQmx
device. This measurement is valid, and so the package build for the plug-in is expected to be
successful.

- Required Hardware: This measurement requires a TestScale Programmable Power Supply (e.g.,
TS-15200).
