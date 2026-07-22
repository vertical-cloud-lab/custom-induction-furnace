# Code Files

This directory contains the control and operational code for the custom induction furnace system.

## Structure

- **induction-furnace-control-code/** - Main LabVIEW control and tuning software
  - `induction-furnace-control.vi` - Primary furnace control interface
  - `manual-induction-furnace-control.vi` - Manual control mode
  - `pid-tuning.vi` - PID controller tuning utility
  - `pid-tuning-v2.vi` - PID tuning v2
  - `send-email.vi` - Email notification module

- **manual-ramping-v5/** - Manual ramping control software (v5)
  - `manual-induction-furnace-control-v5.vi` - v5 furnace control with ramping
  - `send-email-v5.vi` - v5 email notification module

- **plotheatcurve.m** - MATLAB script for plotting heating curves

## File Formats

- `.vi` - LabVIEW virtual instrument files
- `.m` - MATLAB script files

All filenames have been canonicalized (spaces replaced with hyphens, lowercase).
