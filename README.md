# 🌾 Crop Irrigation Management System (Python OOP Project)

## 📌 Project Overview

This project is a simple **Object-Oriented Programming (OOP)** based simulation of a crop irrigation management system developed using Python.
It models real-world farming activities by representing **Crop**, **Farmer**, and **Irrigation System** as separate classes interacting with each other.

The system demonstrates how a farmer irrigates crops using available water resources and monitors crop growth until harvest readiness.

## 🎯 Objectives

* Apply **Object-Oriented Programming concepts**
* Demonstrate **class interaction and modular structure**
* Simulate a **basic agriculture irrigation workflow**
* Improve understanding of **real-world problem modeling using Python**


## 🧩 Project Structure

project-folder/
│
├── crop.py
├── farmer.py
├── irrigation.py
└── main.py

## 📦 Classes Used

### 1️⃣ Crop Class

Represents crop details and growth status.

**Attributes**

* `name` → Name of the crop
* `water_need` → Water requirement
* `fertilizer_need` → Fertilizer requirement
* `growth_stage` → Current growth level

**Methods**

* `grow()` → Increases crop growth stage
* `harvest()` → Checks whether crop is ready for harvest

### 2️⃣ Farmer Class

Represents farmer information and responsibilities.

**Attributes**

* `name` → Farmer name
* `experience` → Experience level

**Methods**

* `take_care()` → Handles crop irrigation using irrigation system

### 3️⃣ Irrigation Class

Represents water supply management.

**Attributes**

* `capacity` → Available water units
* 
**Methods**
  
* `irrigate()` → Supplies water and supports crop growth

## ⚙️ How It Works
1. A crop is created with its requirements.
2. A farmer is assigned to manage the crop.
3. An irrigation system provides water.
4. Each irrigation increases crop growth stage.
5. Once growth stage reaches threshold level, crop becomes ready for harvest.

## ▶️ Example Execution
Maize growth stage: 1
Maize growth stage: 2
Maize growth stage: 3
Maize growth stage: 4
Maize growth stage: 5
Maize is ready for harvest!


## 🚀 How to Run the Project

### Step 1: Clone Repository
git clone https://github.com/your-username/crop-irrigation-system.git

### Step 2: Navigate to Folder
cd crop-irrigation-system

### Step 3: Run Program
python main.py

## 🧠 Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Method interaction between classes
* Encapsulation
* Modular programming

