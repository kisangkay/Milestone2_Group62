# Software Design Document

## Project Name: Nutrient Analyzer
## Group Number: 62

## Team members

| Student Number | Name          | 
|----------------|---------------|
| s5278432       | Simarjot Kaur |
| s5330485       | Stephen Koech | 
| s5376549       | Harsh Patel   | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Software Design Document](#software-design-document)
  * [Project Name: Nutrient Analyzer](#project-name-nutrient-analyzer)
  * [Group Number: 62](#group-number-62)
  * [Team members](#team-members)
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.1 System  overview](#11-system--overview)
    * [1.2 Benefit  Analysis](#12-benefit--analysis)
  * [2. Requirements](#2-requirements)
    * [2.1 User  Requirements](#21-user--requirements)
    * [2.2 Software  Requirements](#22-software--requirements)
    * [2.3 Use Case Diagram](#23-use-case-diagram)
      * [The Use Case diagram of “Nutrient Analyzer” is as follows:](#the-use-case-diagram-of-nutrient-analyzer-is-as-follows)
    * [2.4 Use Cases](#24-use-cases)
      * [These five usage scenarios each illustrates a crucial system function:](#these-five-usage-scenarios-each-illustrates-a-crucial-system-function)
* [3.	Software Design and System Components](#3-software-design-and-system-components-)
  * [3.1	Software Design](#31software-design)
* [3.2	System Components](#32system-components)
  * [3.2.1 Functions](#321-functions)
  * [1. Function 1 searching for a food by its name:](#1-function-1-searching-for-a-food-by-its-name)
  * [2. Function 2 displays a visual representation of a selected food's nutritional breakdown:](#2-function-2-displays-a-visual-representation-of-a-selected-foods-nutritional-breakdown)
  * [3. Function 3 filters foods based on a selected nutrient value range (min-max)](#3-function-3-filters-foods-based-on-a-selected-nutrient-value-range-min-max)
  * [4. Function 4 Calculates nutritional level in a nutritional property (low, mid, high)](#4-function-4-calculates-nutritional-level-in-a-nutritional-property-low-mid-high)
  * [5. Function 5 filters foods by selected levels (low, mid, high)](#5-function-5-filters-foods-by-selected-levels-low-mid-high)
  * [6. Function 6 nutritional density visualizer](#6-function-6-nutritional-density-visualizer)
  * [3.2.2 Data Structures Used](#322-data-structures-used)
    * [<table><tr><td> 1. Data Structure name (food_name_and_its_data): for (Food name and its nutritional information) </td></tr></table>](#tabletrtd-1-data-structure-name-foodnameanditsdata-for-food-name-and-its-nutritional-information-tdtrtable)
    * [<table><tr><td> 2. Data Structure name (selected_food) for: (Food selected and its nutritional information) </td></tr></table>](#tabletrtd-2-data-structure-name-selectedfood-for-food-selected-and-its-nutritional-information-tdtrtable)
    * [<table><tr><td> 3. Data Structure name (calculated_nutrient_levels) for: (storing already calculated nutrient threshold) </td></tr></table>](#tabletrtd-3-data-structure-name-calculatednutrientlevels-for-storing-already-calculated-nutrient-threshold-tdtrtable)
    * [<table><tr><td> 4. Data Structure name (calculated_nutrient_range) for: (storing already calculated min or max value of a calculated nutrient range) </td></tr></table>](#tabletrtd-4-data-structure-name-calculatednutrientrange-for-storing-already-calculated-min-or-max-value-of-a-calculated-nutrient-range-tdtrtable)
* [3.2.3 Detailed Design](#323-detailed-design)
    * [1. Function 1 Detailed design: _search_food_by_its_name()_](#1-function-1-detailed-design-searchfoodbyitsname)
    * [2. Function 2 Detailed design: _display_all_nutritional_breakdown()_](#2-function-2-detailed-design-displayallnutritionalbreakdown)
    * [3. Function 3 Detailed design: _filter_foods_by_nutrient_range()_](#3-function-3-detailed-design-filterfoodsbynutrientrange)
    * [4. Function 4 Detailed design: _calculate_nutrient_level()_](#4-function-4-detailed-design-calculatenutrientlevel)
    * [5. Function 5 Detailed design: _filter_foods_by_nutrient_level()_](#5-function-5-detailed-design-filterfoodsbynutrientlevel)
    * [6. Function 6 Detailed design: _nutritional_density_visualizer()_](#6-function-6-detailed-design-nutritionaldensityvisualizer)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [Planned structure of the application frames in wxForm builder:](#planned-structure-of-the-application-frames-in-wxform-builder)
    * [4.1.2 Information Grouping](#412-information-grouping)
    * [4.1.3 Navigation](#413-navigation)
      * [4.1.3.1 Navigation Logic](#4131-navigation-logic)
    * [4.2	Visual Design](#42visual-design)
    * [Nutrient Analyzer Wireframes](#nutrient-analyzer-wireframes)
    * [1. Main Home Screen](#1-main-home-screen)
      * [Components of Home Screen:](#components-of-home-screen)
    * [Justification of the Home screen design:](#justification-of-the-home-screen-design)
    * [2. Food Search Screen](#2-food-search-screen)
      * [Components of the Food Search Screen:](#components-of-the-food-search-screen)
    * [Justification of Food Search Screen design](#justification-of-food-search-screen-design)
    * [3. Nutritional Breakdown Screen](#3-nutritional-breakdown-screen)
      * [Components of the Nutritional Breakdown Screen:](#components-of-the-nutritional-breakdown-screen)
    * [Justification of Nutritional Breakdown Screen design](#justification-of-nutritional-breakdown-screen-design)
    * [4. Nutrition Range Filter Screen](#4-nutrition-range-filter-screen)
      * [Components of the Nutrition Range Filter Screen:](#components-of-the-nutrition-range-filter-screen)
    * [Justification of Nutrition Range Filter design](#justification-of-nutrition-range-filter-design)
    * [5. Nutrition Level Filter Screen](#5-nutrition-level-filter-screen)
      * [Components of the Nutrition Level Filter Screen:](#components-of-the-nutrition-level-filter-screen)
    * [Justification of Nutrition Level Filter design](#justification-of-nutrition-level-filter-design)
    * [5. Nutrition Density Visualizer Screen](#5-nutrition-density-visualizer-screen)
      * [Components of the Nutrition Density Visualizer Screen:](#components-of-the-nutrition-density-visualizer-screen)
    * [Justification of Density Visualizer Screen design](#justification-of-density-visualizer-screen-design)
    * [Overall screen navigation and design logic](#overall-screen-navigation-and-design-logic)
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
#### The Use Case diagram of “Nutrient Analyzer” is as follows:

![Use Case Diagram](./UseCase_Diagram.drawio.png)

### 2.4 Use Cases

#### These five usage scenarios each illustrates a crucial system function:



| Use Case ID    | UC - 01                                                                                                                                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Food Search                                                                                                                                                                                                                                      |
| Actors         | User                                                                                                                                                                                                                                             |
| Description    | When a user enters the name of a food, the system will show all of the food's nutritional details.                                                                                                                                               |
| Flow of Events | **1.** The user types a food item's name into the search field. <br/>**2.** The food products that match are retrieved from the database by the system.<br/> **3.** The food products and their nutritional information are shown by the system. |
| Alternate Flow | If no food is found, the system displays a "No Results Found" message.                                                                                                                                                                           |



<br>

| Use Case ID    | UC - 02                                                                                                                                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Nutritional Analysis                                                                                                                                                                                                                                                  |
| Actors         | User                                                                                                                                                                                                                                                                  |
| Description    | Pie charts and bar graphs are used to provide users with a comprehensive nutritional analysis of the food item they have selected.                                                                                                                                    |
| Flow of Events | **1.** A food item is chosen by the user from the search results. <br/>**2.** The chosen food's nutritional information is retrieved by the system.<br/> **3.** The system creates and shows bar graphs and pie charts that illustrate how nutrients are distributed. |
| Alternate Flow | The user is prompted to choose a meal item by the system if none is selected.                                                                                                                                                                                         |

<br>

| Use Case ID    | UC - 03                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Nutrition Range Filtering                                                                                                                                                                                                              |
| Actors         | User                                                                                                                                                                                                                                   |
| Description    | Foods that meet the requirements are filtered after users enter a nutritional type and a range of minimum and maximum values.                                                                                                          |
| Flow of Events | **1.**  The user chooses a type of nutrient (fat, protein, etc.). <br/>**2.** A minimum and maximum range are specified by the user.<br/> **3.** Foods that fall within the designated range are filtered by the system and displayed. |
| Alternate Flow | The user is prompted to choose a meal item by the system if none is selected.                                                                                                                                                          |


<br>

| Use Case ID    | UC - 04                                                                                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Nutrition Level Filtering                                                                                                                                               |
| Actors         | User                                                                                                                                                                    |
| Description    | According to the proportion of nutrient values, users may filter items by their nutritional levels (low, mid, or high).                                                 |
|
| Flow of Events | **1.**  The user chooses a level (low, mid, or high) and a nutritional type. <br/>**2.** The meal is categorized by the system and shown according to the chosen level. |
| Alternate Flow | The system displays a "No Results Found" notice if no meals meet the criteria.                                                                                          |


<br>

| Use Case ID    | UC - 05                                                                                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Additional Feature                                                                                                                                                                                                                            |
| Actors         | User                                                                                                                                                                                                                                          |
| Description    | Using an extra function (e.g., comparing nutritional levels between foods or visualizing a pattern), users do a more in-depth investigation.                                                                                                  |
| Flow of Events | **1.**  The user can choose from a variety of foods or a particular advanced analysis option. <br/>**2.** The system gets the pertinent information. <br/> **3** The system does the analysis or visualizes the data, then shows the outcome. |
| Alternate Flow | The user is prompted to change their option by the system if insufficient data is chosen.                                                                                                                                                     |


# 3.	Software Design and System Components 

## 3.1	Software Design
In the Nutrient Analyzer System software's design, the below flowchart comprehensively and clearly outlines a sequential progression of the steps and operations in the software from start to end.

All Key Events Flowchart:  
![Flowchart all key events](./Flowcharts/Software_design_flowchart.png)

# 3.2	System Components
The system components of the Nutrient Analyzer system covered in this section are:
* The programming functions used to return a desired and expected result from a user input when interacting with the system according to its design.
* The data structures used in this software during initialization to store properties of a function, addressing its type, where it has been used, and a list of functions that have used these data structures.
* A detailed design of the functions mentioned according to their usages, outlined in a flowchart to demonstrate how they work by making use of the data structures.

## 3.2.1 Functions
Below is a list and explanations of the key functions necessary to get the software functional in interacting with the database, the user and the functions to display the expected results.
In each function, there is:
- A description of the purpose of declaring the function,
- The input parameters taken by the function which should be of a specific data type to prevent errors, 
- The resulting value to be returned after the function has completed processing the input, and 
- Any side effects that the function may have to other elements in the software in any way.

## 1. Function 1 searching for a food by its name:
* ### <table><tr><td>   Function name: _search_food_by_its_name()_</td></tr></table>

1. Function's purpose:The above function takes in a value entered by a user and searches for a matching record against the food column in the database, then collects all the corresponding nutritional information of the entered food name.


2. Input parameters of the function: The function will take in the name of the food (food_name) of data type string, which will contain the name of the food to be searched. e.g ('peas canned') or ('cassava').


3. Returned value: After taking in the parameter into the function, the returned value will be of data type dictionary, which will contain all the values of the food nutritional information. food_dictionary = {"food":"cassava", "caloric value": "51"}


4. Side Effects:
No any side affects

## 2. Function 2 displays a visual representation of a selected food's nutritional breakdown:
* ### <table><tr><td> display_all_nutritional_breakdown() </td></tr></table>


1. Function's purpose: To take in the previously gathered nutritional information belonging to a specific food and returning a visual representation of its nutritional breakdown using a bar graph.


2. The function will take in the dictionary data type from the preceding function search_food_by_its_name(), of example food_dictionary = {"food":"cassava", "caloric value": "51"} process it by reading the dictionary properties and returning a visualized overview of the gathered values.


3. Return Value:
Returns a pie chart or a bar graph to give a visual representation of the nutritional properties of the specific food.


4. Side Effects:
No side effects.

## 3. Function 3 filters foods based on a selected nutrient value range (min-max)
* ### <table><tr><td> filter_foods_by_nutrient_range() </td></tr></table>


1. Function's purpose: To filter foods after a user makes a selection of a specific nutrient property of the food, and some value within a range.


2. The function will only take in values of data type string, which will be from a drop down which is a selection option list of values from the database, while also providing an input field on the interface with a string data type restriction to narrow down the options from the drop down selection list. The second input parameter will be of a pair of float, which will be the minimum and maximum values (minimum_value) and (maximum_value). For example the first input will be "protein" and the second pair of input float types would be "7.8" and "30".


3. The return value will be of a list data type that is now a filtered listing of only values that meet the above criteria.


4. Side Effects:
No side effects.


## 4. Function 4 Calculates nutritional level in a nutritional property (low, mid, high)
* ### <table><tr><td> calculate_nutrient_level() </td></tr></table>


1. Function's purpose: This function will take in all the numeric values from a specific column and using this key:
- low: less than 33% of the highest value,
- mid: between 33% and 66% of the highest value,
- high: greater than 66% of the highest value,

will then determine whether to classify an input to either being one and only one of the three options.


2. Input parameters: The function will take in a specific nutrient_name of type string, and all its numeric values in type float, to determine the highest value, then use it to classify whether the nutritional value of a specific food is either low, mid or high which will be returned in a tuple.


3. The function will return a tuple (low, mid, high) which each represents the threshold category a food falls within.


4. No side effects.


## 5. Function 5 filters foods by selected levels (low, mid, high)
* ### <table><tr><td> filter_foods_by_nutrient_level() </td></tr></table>


1. **Function's purpose** and **input parameters:** to filter foods by the levels of their nutritional values. The levels will be determined by the function outlined above calculate_nutrient_level() that calculates the level and returns a tuple of either being low, mid or high. This will work by taking in all the name of the food from the user, and the nutritional content level of type string (low, mid or high) which can be provided by a dropdown select option on the filter page.


2. Return value will be of type list, that will contain all foods fitting in the user selected parameters.


3. No side effects.


## 6. Function 6 nutritional density visualizer
* ### <table><tr><td> nutritional_density_visualizer() </td></tr></table>


1. Function's purpose: to take in food items from a user, check them in the database, calculate and display a visual representation of a food's nutritional density relative to the other selected foods.


2. The function will take in a dictionary type for the food items, and their nutrition density values from the nutrition density column in the database as a float. 


3. The returned result will be of a visual representation of the entered food name items, against each other's nutritional density score on a graph or pie chart,


4. No side effects.


## 3.2.2 Data Structures Used
The section below contains a list of all the data structures to be used in the software, that correspond to support the functions defined in section 3.2.1 of the document.
In each data structure, we outline the type, all its planned usages and  defined functions that use the data structure.


### <table><tr><td> 1. Data Structure name (food_name_and_its_data): for (Food name and its nutritional information) </td></tr></table>

- Data structure type: List of dictionaries
- Usage: This list holds each food item and its corresponding nutritional information. 
- - Each dictionary type has been used to define a food item, with its properties from all other database columns such as "Saturated Fats,  Caloric Value, Fat, Sugars, Carbohydrates".

- All defined functions using the dictionary data type:
- - **search_food_by_name()**
- - **filter_foods_by_nutrient_range()**
- - **filter_foods_by_nutrient_level()**
- - **calculate_nutrient_level()**
- - **nutritional_density_visualizer()**

### <table><tr><td> 2. Data Structure name (selected_food) for: (Food selected and its nutritional information) </td></tr></table>

- Data structure type: a dictionary
- Usage: When a user selects a specific food item, all the nutritional information is stored here.
- All functions using dictionary data type:
- - **display_all_nutritional_breakdown()**

### <table><tr><td> 3. Data Structure name (calculated_nutrient_levels) for: (storing already calculated nutrient threshold) </td></tr></table>

- Data structure type: Tuple
- Usage: It has been used to store the levels of a food nutrient level (which can either be low, mid or high)
- All functions using tuple data type:
- - **calculate_nutrient_level()**
- - **filter_foods_by_nutrient_level()**

### <table><tr><td> 4. Data Structure name (calculated_nutrient_range) for: (storing already calculated min or max value of a calculated nutrient range) </td></tr></table>

- Data structure type: Tuple
- Usage: It has been used to store the levels of a food nutrient level (which can either be low, mid or high)
- Functions Using It:
- - filter_foods_by_nutrient_range()

# 3.2.3 Detailed Design
Below is a flowchart to expound more on the functional process of each function we have outlined above in 3.2.1

### 1. Function 1 Detailed design: _search_food_by_its_name()_
![Function 1 flowchart](./Flowcharts/FLOWCHART_search_food_by_its_name.png)
In the search_food_by_its_name() function, it begins by displaying a message to a user to enter a food item they would like to search. In the event that a user does not close the window and enters an input, it is checked if it matches the data type and a feedback is given if a user inputs an invalid data type. If the input is valid, the input is checked against the stored data structure 'food_name_and_its_data' that contains a list of dictionaries. If a match is found, the function returns the data.

### 2. Function 2 Detailed design: _display_all_nutritional_breakdown()_
![Function 2 flowchart](./Flowcharts/FLOWCHART_display_all_nutritional_breakdown.png)
The function to display_all_nutritional_breakdown() would make use of the data structure food_name_and_its_data containing a list of dictionaries by finding the selected food result inside it and using it to generate a visual bar graph to show in the display panel.

### 3. Function 3 Detailed design: _filter_foods_by_nutrient_range()_
![Function 3 flowchart](./Flowcharts/FLOWCHART_filter_foods_by_nutrient_range.png)
The function filter_foods_by_nutrient_range() uses the data structure food_name_and_its_data containing the list of dictionaries, to find a valid nutrient range property input by a user, and returns a list of only food items fitting the specified parameters.

### 4. Function 4 Detailed design: _calculate_nutrient_level()_
![Function 4 flowchart](./Flowcharts/FLOWCHART_calculate_nutrient_level.png)
After getting its value from food_name_and_its_data data structure, This function is later used in the function filter_foods_by_nutrient_level
() after taking all the values from a nutrient column to either classify as low, medium or high and store in the data structure calculated_nutrient_levels and filter_foods_by_nutrient_level.

### 5. Function 5 Detailed design: _filter_foods_by_nutrient_level()_
![Function 5 flowchart](./Flowcharts/FLOWCHART_filter_foods_by_nutrient_level.png)
After getting the levels category of a nutrient from the function calculate_nutrient_level(), and data structure food_name_and_its_data() this function then takes the user selection of a nutrient, level selected and returns food items falling in within either of the 3 levels. then storing the values in the data structure filter_foods_by_nutrient_level.

### 6. Function 6 Detailed design: _nutritional_density_visualizer()_
![Function 6 flowchart](./Flowcharts/FLOWCHART_nutritional_density_visualizer.png)
The function nutritional_density_visualizer() takes in multiple selected inputs of food items from a user, filters the food items from the food_name_and_its_data data structure to get the comparison in its nutritional density then processes it to return a display of the visual comparison of the entered values.

## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.
- ### 4.1.1 Structure
Using wxForm Builder for our user interface design, we will utilize the event driven approach while having our backend functions run by python. 
For further simplicity, each feature in the software will be carried out in their own frames designed in wxForm builder.

### Planned structure of the application frames in wxForm builder:
1. Main home screen: will serve as the main welcome page that contains the main menu to access any other windows. A short information will be included in the home screen to serve as an education purpose for users new to the software.
2. Food search screen
This screen will contain a search bar to take user input of a food item and display its nutritional details
3. Nutritional breakdown screen
This screen will contain a drop down for a user to select a food items and a display area for pie charts and bra graph.
4. Nutritional range filter screen
This screen will contain a dropdown to select a nutrient, take a pair of minimum and maximum values and a display area field to show the filtered food item results
5. Nutrition level filter screen
THis screen structure will contain a dropdown to select nutrients, buttons to select either low, medium or high nutrient levels, and a display area to show resulting food items
6. Nutrition density visualizer screen 
This screen takes in multiple food items from a user, then returns a visual representation of a comparison between the nutritional densities in the display area field.

### 4.1.2 Information Grouping
To ensure that we maintain a user friendly interface that is free from clutter, we will need to group our components inside wxForm builder. 
We can utilise this feature to group our elements by specific windows.

For instance, in our main home page screen, when making our main menu, we will group our buttons:
- food search button, nutritional breakdown, nutrition range filter, nutrition level filter, analysis and visualization
1. In our window 'food search'
we will group the elements such that the search bar, the 'submit' button and results display area will be contained in the same window.
2. In the nutritional breakdown window, we group the dropdown menu section and the visual element display area which will contain either a pie chart or a bar graph.
3. Nutrition range filter screen
Being the page that takes in a set of input from a user, we group the nutrient dropdown, the pair of input fields, the submit button to filter and the display panel that shows the results of the filtered values.
4. Nutrition level filter screen
On the nutrition level filter screen, we group the elements drop down that selects a specific nutrient, one of three nutrition level low, medium or high, the submit button and results display area.
5. For the additional function, the nutritional density visualizer will take in a maximum of five drop down properties as input from a user, and we will group that with its submit button and the display area that shows a bar graph of the data comparison.

### 4.1.3 Navigation
In our navigation design, we implemented consistency in visual and structural design, such that a common menu will be pinned at the top of the frame and provides access to all functional windows in the software. Besides that, each window visited will have a back button, so that if a user is not able to recall which page they were previously on, simply clicking on the back button would return them to their previous page.
 
![Hierarchy chart showing page navigation](Wireframes_and_Hierarchy/Nutrient_Analyzer_Hierarchy_navigation.png)

#### 4.1.3.1 Navigation Logic
1. The main home screen user interface will provide a possibility to navigate to any other page by clicking of buttons on the top of the screen. This navigation template is reused in all other pages since it does not collide with the functional pages content, and enhances consistency for a users familiarization of the interface. This transition logic where users do not necessarily have to revisit the home page again to navigate to other modules is helpful to maintain ease of screen navigation.

- ### 4.1.4 Design Choices
1. wxForm Builder:
Due to its design simplicity of creating a user interface through the use of a visual user interface, wxForm builder is our go to option since it consequently makes it easier to connect our events from the interface to python backend functions.
In the event that we need to make changes to our design, we simply make the update in wxForm builder then paste the new generated template code to link to our python backend functions.
2. Centralised navigation from all pages.
Providing a pinned common menu accessible from all pages ensures users always have an easy way to switch between pages without necessarily having to go to the main home page once again.
3. Splitting different features into different frames. This contributes to the overall orderliness in the software, providing that users will now only view what is relevant to their current function or what they want to achieve.
4. Usage of graphs and charts for graphical data visualization.
Other than the raw information being accessible to users, presenting a visual version of the data allows users to experience a better way of interpreting data that could otherwise be difficult to tell apart significant differences.

### 4.2	Visual Design
### Nutrient Analyzer Wireframes
### 1. Main Home Screen
This will be the main starting point of the software, where access points to any other location within the program will start from.

#### Components of Home Screen:
- The Title: Nutrient Analyzer
- Menu comprising of:
- - Home
- - Food Search 
- - Nutrition Breakdown 
- - Nutrition Range Filter 
- - Nutrition Level Filter 
- - Nutritional Density Visualizer
- - Close

- #### Welcome message and a brief introduction

![Home Page welcome screen](Wireframes_and_Hierarchy/Home_screen_wireframe.png)
### Justification of the Home screen design:
- This design is meant to provide a familiar interface that is similar to other already existing applications, leading to an intuitive experience where a user can easily point out the location of a feature they are after. Including a grouped menu also simplifies navigation since all the main functions of Nutrient Analyzer are included here.
- The menu on the top of the home page will be consistent throughout the user interaction with the software, for a simplified and straight forward user navigation.


### 2. Food Search Screen
This being the first function of the software, allows a user to enter a food item which will then output all its nutritional information.

#### Components of the Food Search Screen:
- Menu
- Search bar
- - This provides the input field for a user to enter a desired food item of string data type.
- Search button
- - After typing a desired food item entry, the submit button will send a request to search from the food column of the database and list its relative data.
- Results/Message display.
- - This display field will show the results of the user search value in form of a list, or if the user entered an invalid input it would display in this dynamic field.
- -Since the record from the database is large, we want to support a scroll functionality to view more overflowing results.
- Back button to return to the page they were in previously.

![Food search screen design](Wireframes_and_Hierarchy/food-search-screen.png)

### Justification of Food Search Screen design
Ensuring we have enough space to comfortably view the results, the scroll bar enables more data to load in the view. By fixing the search panel on a different section, we ensure a clean interface design that separated the user input section and results section.

### 3. Nutritional Breakdown Screen
This screen will display a visual pie charts and bar graphs to show the nutrients of a food item selected by a user.

#### Components of the Nutritional Breakdown Screen:
- Menu
- Dropdown to select one food item
- Instructional text label to "Select a food item"
- Graphs and Charts Display area at center of the screen.
- Checkbox to change visual layout between a pie chart and a graph.
- Back button to take user to previous page.

![Nutritional breakdown screen design](Wireframes_and_Hierarchy/Nutritional-Breakdown-Screen.png)
### Justification of Nutritional Breakdown Screen design
- The importance of having a visual representation of the nutritional breakdown structure is to present a visually appealing translation of data for better perception of users. Adding a function to switch between either styling of chart presentation would be accommodating for different audience needs.
- Including a dropdown instead of users having to type in the names of the food item makes it easier to access records from the database compared to having a normal manual search.


### 4. Nutrition Range Filter Screen
- This screen allows users to select a nutrient from a dropdown, then a minimum and maximum input of a value pair to display any results falling within the parameters. 

#### Components of the Nutrition Range Filter Screen:
- Menu
- Nutrient dropdown selection
- - An instructional label telling a user to enter a (minimum and maximum value)
- Inputs
- - input for minimum
- - input for maximum
- Apply filter button
- Filtered results display area
- Scroll bar for large data results beyond the first page view

![Nutritional range filter screen design](Wireframes_and_Hierarchy/nutritional-range-filter.png)

### Justification of Nutrition Range Filter design
- Providing a separated section for user input only and for data display provides a cleaner and an orderly interface.
- Providing a user with an option to filer results especially if the data being dealt with is of large amounts can be overwhelming simplifies the approach and user interaction on the software.

### 5. Nutrition Level Filter Screen
The nutrition level filter screen corresponds to the function of allowing a user to view filtered food items based on the level of their nutrient content level which can either be low, medium or high


#### Components of the Nutrition Level Filter Screen:
- Dropdown to select a specific nutrient type
- - Informative label placeholder to ask a user to select a nutrient type
- - Informative label to ask a user to select the nutrition level they want
- Nutrient level selection option (Radio buttons will be used because of their property of selecting only one value in a group)
- Button to apply filter
- Filtered results display section in the screen
- scroll bar in the display section
- back button to the user's previous screen

![Nutrition level filter screen design](Wireframes_and_Hierarchy/nutrition-level-filter.png)

### Justification of Nutrition Level Filter design
When it comes to making a selection to apply a filter, we want to make it as easy as possible for the user. Hence the use of radio buttons in the nutrition level group which only takes one option. This way a user knows they are supposed to only pick one option.

### 5. Nutrition Density Visualizer Screen
This will be the last option on the pinned menu on the user interface, and once on this page, a user can enter several food items to compare their nutritional density, getting a visual representation of the comparison.
For ease of use of this analysis feature, we limit the food selection options to 5 food items.

#### Components of the Nutrition Density Visualizer Screen:
- A maximum of 5 food item selection list
- - An informative label to ask a user to select up to 5 food items from the drop-down options.
- - Compare button
- Display panel to show a bar graph that compares the nutritional density levels of the selected food items.
- Back button to return a user to their previous page.

![Food density visualizer screen design](Wireframes_and_Hierarchy/food-density-visualizer.png)

### Justification of Density Visualizer Screen design
- With this additional feature, we need to compare and get a better representation of the nutritional density of several food items, hence the need to take in multiple selection options of the food items.
- With this implementation, we restrict a user from selecting the same food item more than once as this will have no comparison value as a duplicate.  

### Overall screen navigation and design logic
- The consistency employed in the design of all the screens is so that it can give users a familiarized user interface, and the pinned menu at the top ensures a user can freely navigate to a screen of their choice if they do not wish to return to the previous screen.