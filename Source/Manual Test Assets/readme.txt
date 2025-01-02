The 'Measurement.lvproj' project contains three sample measurement plug-ins to assist with the
manual testing of the 'Measurement Plug-In Packager' tool.

niScope EX Getting Started:
- This plug-in is actually a measurement VI converted into a measurement plug-in using the
'Measurement Plug-In Converter' tool. The base measurement VI, which is one of the many examples for
NI-SCOPE, shares the same name as the plug-in and can be found using the LabVIEW Example Finder.
- This measurement demonstrates the minimal code required to use NI-SCOPE. The plug-in includes a
'Waveform Graph' control in its 'Measurement Results.ctl'.
- This measurement service cannot be executed because of the invalid datatype in the 'Measurement
Results.ctl', and so it is expected to fail during the package build process.

Sample:
- This measurement plug-in was generated using the 'Measurement Plug-In Generator' tool. It is a
basic loopback measurement that takes the inputs and writes them to the associated outputs.
- The package build for this plug-in is expected to be successful as the measurement is valid.

Z Power Module:
- The 'Z Power Module' measurement plug-in is also a measurement converted into a plug-in using the
Converter tool.
- It demonstrates how to acquire a single buffer of power measurements using a DAQmx device. This
measurement is valid, and so the package build for the plug-in is expected to be successful.
- Required Hardware: This measurement requires a TestScale Programmable Power Supply, also known as
TestScale Power Module (e.g. TS-15200).
- To simulate a TestScale Programmable Power Supply in software: open `NI Hardware Configuration
Utility`, click `Edit` -> `Add Hardware...`, select the `Simulated` tab, and select the `TS-15200`
device in the `Power` category. You may need to also simulate a TestScale chassis (e.g. TS-15000) if
none exist in the system.
