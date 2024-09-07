# Software Design Document

## Project Name: XXXX
## Group Number: 001

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

1. **Problem Identification:**


1. **System Benefits:**
This system is used for analyzing and visualizing nutritional data from various food items. It helps the users in the following ways:

1. **Food Search**: Enables consumers to obtain comprehensive nutritional data regarding certain meals swiftly.

2. **Visualizing Nutrient Breakdown**: Visual representations such as pie charts and bar graphs are provided to help people better comprehend the nutritional makeup of certain meals.

3. **Filtering by Nutrition Ranges**: This feature helps with diet planning and health management by allowing users to find items that fit within a given range of nutrients.

4. **Nutritional Level Categorization**: This feature makes it simpler for users to find foods that fall into particular dietary categories (low, mid, or high) by allowing them to filter items based on their levels of nutritional content.

Furthermore, the tool known as Nutrient Correlation Analysis provides a more in-depth understanding of the connections among distinct nutrients, assisting users in comprehending the possible links between different nutrients and their availability in different diets.

**2. Dataset:**

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


**3. Data Input:**

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

**Target Users:**

**1. Nutritionists and dietitians:** This data is being used by the nutritionists and dietitians, because of the following reasons:

**Reasons:**

To provide their clients with customized meal plans, they must examine and display the nutritional value of different foods. With this application, individuals may more easily create customized nutrition plans by searching for items, seeing comprehensive nutritional breakdowns, and filtering possibilities according to certain dietary requirements.

**2. Health-Conscious Individuals:** This data is being used by health-conscious people, because of the following reasons:

**Reasons:**

Those committed to controlling their diet, level of exercise, or health may utilize the system to help them make well-informed food choices. They can do food searches, view nutritional analyses, and identify items that fit their dietary requirements—for example, balanced, high-protein, low-fat, or both.

**3.** **Fitness enthusiasts and athletes:** This data is being used by  fitness enthusiasts and athletes, because of the following reasons:

**Reasons:**

People who are committed to fitness and athletes frequently keep a careful eye on their food consumption. They can quickly identify foods that contain the proper ratios of macronutrients (fats, proteins, and carbs) and evaluate nutritional density to maximize performance thanks to this approach.

**4. Researchers in Medicine:** This data is being used by researchers in medicine, because of the following reasons:

**Reasons:**

By using the method, nutrition and health researchers may examine the relationships between various nutrients and dietary outcomes. For their study, the nutritional correlation analysis function and the visualizations offer insightful information.

**5. Producers and Developers of Food:** This data is being used by producers and developers of food, because of the following reasons:

**Reasons:**

Food product developers may use the system to compare their goods to others on the market and to identify nutritional trends. This aids in their ability to properly sell their products and fulfill nutritional guidelines.

**6. Academic Institutions (Professors & Students):** This data is being used by academic institutions, because of the following reasons:

**Reasons:**

This tool may be used for instructional reasons by professors and students studying food science, nutrition, and health. It offers a useful, interactive method for investigating nutritional information, spotting patterns, and learning more about the nutrient makeup of different meals.

**7. Providers of Healthcare:**

**Reasons:**

For managing chronic disorders like diabetes or heart disease, doctors and other healthcare practitioners may utilize the system to help patients choose meals that match certain dietary criteria, such as low cholesterol or low salt.

### 1.1 System  overview

**System Functionality:**

The technology will give users access to an extensive interface for analyzing and visualizing nutritional information from an extensive food database. Users of the system may see nutritional breakdowns, filter items according to nutrient levels and ranges, search for certain foods, and visualize data using graphs and charts. Users may also investigate relationships between various nutrients using the system, which can assist in identifying trends and patterns in eating habits.

**Features and Functionalities:**

**1. Food Search:**

**Functionality:** Any food item may be searched for by name by users.

**Output:** It shows all of the nutritional data, including calories, fats, carbs, proteins, vitamins, and minerals, for the meal that was searched for.

**2. Nutritional Analysis Visualization:**

**Functionality:** Lets users choose a food and see the nutritional analysis of that item.

**Output:** It produces bar graphs and pie charts that illustrate the ratios of different nutrients (such as lipids, proteins, and carbs) in the chosen meal.

**3. Filter for Nutrition Range:**

**Functionality:** By entering minimum and maximum values for nutrients like fat, protein, carbs, etc., users may filter items based on given nutritional ranges.

**Output:** It provides a list of meals that are within the designated range of nutrients, making it easier for users to choose alternatives that satisfy their dietary needs.

**4. Filter for Nutrition Level:**

**Functionality:** Foods may be filtered by users according to three levels of nutritional content (low, mid, and high) for components including fat, protein, carbs, sugar, and total nutritional density.

**Output:** Assists users with locating foods that meet particular dietary requirements by classifying items as low, mid, or high for the selected nutrient.

**5. Analysis of Nutrient Correlation (Additional Feature):**

**Functionality:** Users may examine how two or more nutrients are correlated, for example, how fat and carbs or vitamins and minerals are related.

**Output:** To assist users in understanding the relationships between various nutrients, scatter plots displaying the correlation are provided, along with trend lines and correlation coefficients.

**6. Export Data:**

**Functionality:** The nutritional data and visualizations may be exported by users for additional study or distribution.

**Output:** Enables data to be exported for offline analysis or display in a variety of formats (CSV, PNG for graphs).

**7. Easily navigable graphical interface:**

**Functionality:** The system offers a graphical user interface that is simple to use and intuitive for smooth data processing and visualization.

**Output:** A user-friendly, aesthetically pleasing interface that leads non-technical people through the process of exploring data.

**8. Options for Sorting and Filtering Data:**

**Functionality:** The food list may be sorted by the user according to various parameters (e.g., foods with the lowest fat or highest to lowest protein content).

**Output:** To facilitate decision-making, lists are sorted according to user-selected filters or sorting choices.

### 1.2 Benefit  Analysis

There are several important domains in which the suggested data analysis and visualization system would be extremely valuable.

**1. Enhanced Nutritional Awareness:** The technology will assist consumers in comprehending the nutritional value of the foods they eat on a deeper level. Users are provided with comprehensive statistics and graphical displays, such as pie charts and bar graphs, to enable them to observe the distribution of various nutrients, including proteins, carbs, and fats, in their diet. Making educated food choices is made simpler and healthy eating habits are encouraged by this realization.

**2. Personalized Dietary Planning:** Users may choose foods with low fat or high protein content by filtering items according to their dietary requirements or preferences. This makes it possible to plan meals in a more individualized and customized way, which aids in the achievement of certain health objectives including blood sugar regulation, muscular growth, and weight loss.

**3. Time Efficiency for Healthcare Professionals:** By eliminating the need to laboriously go through big datasets, nutritionists, dietitians, and other healthcare workers may swiftly evaluate nutritional data. Professionals will be able to concentrate more on giving their patients and clients tailored advice and treatment plans thanks to this time-saving feature.

**4. Data-Driven Food Research and Development:** The system will be a useful resource for specialists in the food sector in assessing patterns in nutritional content and pinpointing chances for the creation of new food products. Food producers may provide healthier food alternatives that satisfy consumer desires by utilizing the information.

**5. Simple Food Comparison:** By comparing the nutritional values of various foods side by side, users may choose healthier options with more ease. People who are trying to increase their total nutritional intake or who have dietary limitations may find this option especially helpful.

**6. Visual Nutritional Breakdown:** Users can more easily understand and interact with complicated nutritional data thanks to the system's visualization tools, which include pie charts and bar graphs. As a result, the user experience is enhanced overall and a larger audience—including those lacking technical or nutritional expertise—can more easily obtain nutritional data.

**7. Support for Health and Wellness Goals:** By allowing users to filter meals based on their nutritional value, the system will assist them in matching the foods they eat to certain health and wellness objectives, such as controlling cholesterol levels, cutting back on sugar intake, or upping protein intake.

**8. Educational Resource:** By using the method, educators, students, and medical professionals may have a better understanding of how certain nutrients affect general health. It offers an experiential learning opportunity with nutritional data and may be utilized for both academic and self-directed learning.

**9. Enhanced Nutritional Openness:** More transparency about food composition is encouraged by the system's provision of precise and comprehensive nutritional information. Customers may use this to make more moral and health-conscious selections regarding the goods they purchase and eat.

## 2. Requirements

### 2.1 User  Requirements

A wide range of people, including professionals, are expected to utilize this system as they need quick access to comprehensive nutritional data. Key user personas and the interactions they require are listed below.

**Fictional User Persona 1:**

**Sarah, a Health-Conscious Customer:**

Sarah is a thirty-year-old working woman who values leading a healthy lifestyle. She keeps a careful eye on her nutrition to make sure she gets the proper ratio of nutrients to keep her healthy and full of energy.

**User Requirements:**

**1. Search by Food Name:** In order to obtain comprehensive nutritional data fast, Sarah needs to be able to search for items by name.

**2. See Nutritional Breakdown:** She would want to quickly view a visual breakdown of the main macronutrients—fats, proteins, and carbohydrates—as well as other important nutrients, such as minerals and vitamins.

**3. Filter by Nutrition Ranges:** To make better dietary decisions, Sarah would want to filter items based on particular nutritional values (such as low-fat, high-protein meals).

**4. Compare Foods:** To improve meal planning, she must be able to compare various food products side by side.

**5. Track Nutritional Density:** To find foods that offer more nutrients per calorie, Sarah is interested in the "nutrient density" option.

**Fictional User Persona 2:**

**Profile of Dr. Mike, a Nutritionist:**

Dr. Mike is a forty-five-year-old nutritionist who helps patients with high cholesterol and diabetes by offering dietary advice.

**User Requirements:**

**1. Examine Nutritional Data for Clients:** Dr. Mike must enter client-specific specifications (such as minimal salt or sugar content) and obtain dietary suggestions by those specifications.

**2. Visualize Nutritional Breakdown:** To show customers how nutrients are broken down graphically during consultations, he needs tools like pie charts and bar graphs.

**3. Filter by Nutritional Levels:** For dietary planning tailored to each client, the system must enable Dr. Mike to filter meals by high, mid, and low nutritional content (e.g., high protein, low fat).

**4. Save and Export Reports:** To share data with his customers during follow-up consultations, he would want to save and export nutritional reports**.**

**Fictional User Persona 3:**

**Profile of a Food Researcher, Rachel:**

Rachel is a 38-year-old food researcher employed at a business that creates novel food items. She studies dietary patterns and searches for chances to provide better options.

**User Requirements:**

**1. Obtain Complete Nutritional Information:** Rachel needs thorough access to a variety of food products and the nutrients—such as lipids, vitamins, and minerals—that go along with them.

**2. Compare Various Nutritional Values:** To identify possible components for new goods, she has to compare foods from different categories (such as low-calorie, and high-vitamin foods).

**3. Filter by Nutritional Ranges:** For her research and product development, Rachel needs to be able to filter meals depending on particular nutritional levels (e.g., rich in Vitamin D, low in cholesterol).

**4. Provide Visual Data Insights:** To share findings with her colleagues, she must provide visual data insights, such as nutritional comparison charts.

**Functionalities from the End-User Perspective:**

**1.** **Food Search by Name:** To swiftly search any food item by name and obtain its whole nutritional profile, which includes calories, macronutrients (fat, carbs, and protein), and micronutrients (vitamins and minerals), users require a straightforward search bar.

**2. Comprehensive Nutritional Analysis:** The breakdown of lipids, carbs, proteins, and other important nutrients should be shown in tables, pie charts, and bar graphs that allow users to pick any item and examine complete nutritional information.

**3. Filter for Nutritional Range:** For low-sodium foods, for instance. the system should allow users to enter the lowest and maximum values for each nutrient and provide a list of items that fit within that range.

**4. Filter for Nutritional Levels:** Foods should be able to be filtered by three nutritional levels (low, mid, and high) for important nutrients such as protein, carbs, fats, and sugars. This aids in locating meals that meet particular dietary requirements.

**5. Comparing Foods:** To help users make educated decisions, the system should allow them to compare many items at once and display their nutritional values side by side.

**6. Visual Guide to Nutrition:** To facilitate comprehension and improve decision-making, users need tools that allow them to create visual representations of nutritional data, such as pie charts and bar graphs.

**7. Data Export and Report Creation:** Nutritionists and researchers, for example, must export or store nutritional data for client consultations, future analysis, and reporting.

**8. Extra feature (to be suggested by the group):** A "Meal Planner" feature, which would allow users to mix and match foods to make meals and view the meal's complete nutritional breakdown, might be added to the system to further improve its usefulness and assist users in maintaining balanced diets.

### 2.2 Software  Requirements

The functional criteria that the system has to meet are listed in this section. For the purpose of ensuring clarity in system design and execution, each need is officially articulated.

**R1: Food Search**

**R1.1** Users will be able to look for meals by name using the system.

**R1.2** Following the search, the system will show all of the nutritional details for the meal that was chosen.

**R1.3** The search results will be shown by the system as a list with clickable items for more information.

**R2: Nutrition Breakdown**

**R2.1** Users will be able to choose a food item and read a comprehensive nutritional breakdown of that food.

**R2.2** The nutritional breakdown will be shown by the system utilizing bar graphs for micronutrients (vitamins and minerals) and pie charts for macronutrients (fat, protein, and carbs).

**R2.3** In addition to the graphical depiction, the system will show the precise values of each nutrient (e.g., grams, milligrams).

**R3: Filter for Nutritional Range**

**R3.1** Users will be able to enter the minimum and maximum amounts of a certain nutrient (such as protein or fat) into the system.

**R3.2** For the chosen nutrient, the system will show a list of foods that are within the designated range.

**R3.3** The food's nutritional value will be shown by the system in the result list.

**R4: Filter for Nutritional Level**

**R4.1** Foods may be filtered by users according to three different nutritional levels: low, mid, and high.

**R4.2** The system will classify the following nutritional levels:

Low: A figure that is under 33% of the maximum.

Mid: From 33% to 66% of the maximum amount.

High: Exceeding 66% of the maximum amount.

**R4.3** Users will be able to filter the system based on several nutrient categories, including protein, sugar, fat, and carbs.

**R5: Extra Functionality (Meal Planning)**

**R5.1** Users will be able to put together various food components to make meals using the system.

**R5.2** After integrating the nutritional values of all the foods that were chosen, the system will show the overall nutritional breakdown of the meal.

**R5.3** The system must have the ability to export or store the nutritional information for the meal.

**R6: Report Generation and Data Export**

**R6.1** Users will be able to export nutritional data in the form of CSV or PDF files from the system.

**R6.2** The system will let users create and store reports depending on the meals they've chosen or the filters they've used.

**R7: Interface with Users**

**R7.1** The system must include a graphical user interface that is easy to use for conducting searches, seeing breakdowns, and applying filters.

**R7.2** The system must guarantee that the interface is responsive and provides easy access to all of the capabilities.

**R7.3** To assist users in navigating the features, the system will include tooltips and help text.

**R8: Information Retrieval**

**R8.1** A CSV file named Nutritional_Food_Database.csv will be loaded by the system with nutritional data.

**R8.2** If new data is added to the CSV file, the system must be able to update the database.
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
Include a flowchart that illustrates how your software will operate.

Example:  
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

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



