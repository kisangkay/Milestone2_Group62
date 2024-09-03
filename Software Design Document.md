# Software Design Document

## Project Name: My Nutrition
## Group Number: 62

## Team members

| Student Number | Name          | 
|----------------|---------------|
| s5278432       | Simarjot Kaur |
| s              | Stephen Koech | 
| s              | Harsh Patel   | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification:

1. **System Benefits:**
This system is used for analyzing and visualizing nutritional data from various food items. It helps the users in the following ways:

1. **Food Search**: Enables consumers to obtain comprehensive nutritional data regarding certain meals swiftly.

2. **Visualizing Nutrient Breakdown**: Visual representations such as pie charts and bar graphs are provided to help people better comprehend the nutritional makeup of certain meals.

3. **Filtering by Nutrition Ranges**: This feature helps with diet planning and health management by allowing users to find items that fit within a given range of nutrients.

4. **Nutritional Level Categorization**: This feature makes it simpler for users to find foods that fall into particular dietary categories (low, mid, or high) by allowing them to filter items based on their levels of nutritional content.

Furthermore, the tool known as Nutrient Correlation Analysis provides a more in-depth understanding of the connections among distinct nutrients, assisting users in comprehending the possible links between different nutrients and their availability in different diets.

2.  **Dataset:**

The Nutritional_Food_Database.csv dataset, which includes comprehensive nutritional data for a variety of food products, is the one that was utilized. The following columns are part of the dataset:

- **Food:** The food item's name or kind.

- **Caloric Value:** The total energy contained in food, expressed as kilocalories (kcal) per 100 grams, is known as its calorie value.

- **Fat (in g):** Total fat content in grams, broken down into monounsaturated, polyunsaturated, and saturated fats.

- **carbs (in g):** Total carbs (including sugars) in 100 grams.

- **Protein:** The total amount of proteins in 100 grams.

- **Nutritional Fibre (g):** The amount of fiber in 100 grams.

- **Cholesterol (in mg):** The amount of cholesterol in milligrams, or mg/100 grammes.

- **Sodium (in g):** The amount of sodium in 100 grams.

- **Water (g):** The amount of water in 100 grammes.

- **Vitamins:** Different vitamins per 100 grammes (A, B1, B11, B12, B2, B3, B5, B6, C, D, E, and K in mg).

- **Minerals:** Different minerals per 100 grammes (Calcium, Copper, Iron, Magnesium, Manganese, Phosphorus, Potassium, Selenium, Zinc in mg).

- *Nutrition Density:** A measure of a food's nutritious content per calorie.

<![endif]>Data  Input/Output:  What  kind  of  data  input  and  output  is  required?

3. **Data Input:**

These are the data input types that the system needs:

**1. Food Name Enter:** Users may search for and obtain nutritional information about an item by entering its name.

**2. Input for Nutrient Selection:** Users may filter items according to their nutritional composition or choose certain nutrients (such as fat, protein, and carbs) to see how they are broken down.

**3. Input of Nutrient Range:** For a certain nutrient (fat between 5g and 10g, for example), users may enter the lowest and maximum values to filter meals that fall within that range.

**4. Choosing Nutrient Levels:** Foods may be filtered by the user according to the levels of fat, protein, carbs, and other nutrients (low, mid, and high).

**5. Input for Nutrient Correlation (for the extra feature):** Inn order to create scatter plots and determine correlation coefficients, users can choose two or more nutrients and examine their association.

4. **Data Output:**

The following categories of data output are offered by the system:

**1. Display of Nutritional Data:** The system provides all of the nutritional data, including calories, fats, carbs, proteins, vitamins, and minerals, for the food item that is being searched.

**2. Illustrations:** The system produces visuals that break down various nutrients (such as fat, protein, and carbs) for specific foods, such as pie charts and bar graphs.

**3. Food List Filtered:** meals that meet certain dietary criteria may be easily identified by the system, which provides a list of meals that match the user's selected nutritional range or level.

**4. Analysis of Nutrient Correlation (for the extra feature):** Scatter plots illustrating the link between certain nutrients produced by the system, together with trend lines and correlation coefficients that shed light on how these nutrients relate to one another in various diets.


- Target Users: Who will use the system, and why?

### 1.2 System capabilities/overview

- System Functionality: What will the system do?
- Features and Functionalities: Describe the key features and functionalities of the system.

### 1.3	Benefit Analysis

How will this system provide value or benefit?

## 2. Requirements

### 2.1 User Requirements

Detail how users are expected to interact with or use the program. What functionalities must the system provide from the end-user perspective? This can include both narrative descriptions and a listing of user needs.

Note: Since no specific client or user is assigned, you may create a fictional user. Who do you envision using your software?

### 2.2	Software Requirements
Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.

Example Functional Requirements:  
- R1.1 The program shall accept multiple file names as arguments from the command line.  
- R1.2 Each file name can be a simple file name or include the full path of the file with one or more levels.  

- etc …

### 2.3 Use Case Diagram
Provide a system-level Use Case Diagram illustrating all required features.

Example:  
![Use Case Diagram](./UCD.png)

### 2.4 Use Cases
Include at least 5 use cases, each corresponding to a specific function.


| Use Case ID    | xxx  |
|----------------|------|
| Use Case Name  | xxxx |
| Actors         | xxxx |
| Description    | xxxx |
| Flow of Events | xxxx |
| Alternate Flow | xxxx |



## 3.	Software Design and System Components 

### 3.1	Software Design
In the My Nutrition software's design, the below flowchart outlines a sequential progression of the steps and possibilities from start to end.

Draft 1:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Draft 1:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



