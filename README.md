# Attendance Management System

This repository contains code for an Attendance Management System built using Python and the Tkinter library.
The system includes features for both users and administrators to manage attendance data.

## Introduction

The Attendance Management System aims to provide a simple and efficient way to track and manage attendance records. It includes two main interfaces: one for users (students) to log their attendance and another for administrators to view and save the attendance data.

## User Interface

The User Interface allows students to enter their attendance status for a particular date. It includes the following components:

1. Name Entry Field: Students can enter their name.
2. Status Selection: Students can choose their attendance status from options (Present, Late, Absent) using a drop-down menu.
3. Date Selection: Students can select the date for which they are logging their attendance using a date picker.
4. Certification Checkbox: Students must certify the accuracy of the information provided by checking the checkbox.

## Administrator Interface

The Administrator Interface is designed for administrators to view and save the attendance data. It provides the following features:

1. Launch Original Excel: Administrators can open the original attendance data Excel file using the "Launch Original Excel" button.
2. Date Range Selection: Administrators can select a date range to filter the attendance data and save it as a new CSV file.
3. Save Data: Administrators can save the filtered attendance data as a new CSV file for further analysis.

## Installation

To run the Attendance Management System, ensure that you have the required packages installed:

```shell
pip install customtkinter tkcalendar pandas
```

## Usage

Run the provided Python code to launch the Attendance Management System. Upon execution, the system will display the welcome page with options to access the User and Administrator interfaces.

## Usage Example

1. Users can log their attendance by selecting their name, attendance status, and date, and then certifying the information.
2. Administrators can view the original attendance data Excel file, select a date range, and save the filtered data as a new CSV file for analysis.
