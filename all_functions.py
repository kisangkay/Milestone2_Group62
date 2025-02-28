
def on_search(df, search_term):

    if search_term:
        filtered_data = df[df['food'].str.contains(search_term, case=False, na=False)]
        return filtered_data
    return df.iloc[0:0]  # Return an empty DataFrame if no search term

def get_on_food_selected(food_data, selected_food):

    # Find the row corresponding to the selected food
    food_info = food_data[food_data['food'] == selected_food].iloc[0]

    # Extract nutrient data for the pie chart
    categories = ['Caloric Value', 'Fat', 'Saturated Fats', 'Protein']
    sizes = [food_info['Caloric Value'], food_info['Fat'], food_info['Saturated Fats'], food_info['Protein']]

    return categories, sizes


def get_on_filter(food_data, nutrient, min_density, max_density):

    # Filter the DataFrame based on nutrient density
    results = food_data[
        (food_data[nutrient] >= min_density) & (food_data[nutrient] <= max_density)
    ]
    return results


def get_filter_nutrition_level(food_data, selected_nutrient, level):

    max_value = food_data[selected_nutrient].max()

    # Apply level checks on the specified nutrient
    if level == 'Low':
        results = food_data[food_data[selected_nutrient] < (0.33 * max_value)]
    elif level == 'Mid':
        results = food_data[(food_data[selected_nutrient] >= (0.33 * max_value)) &
                            (food_data[selected_nutrient] <= (0.66 * max_value))]
    elif level == 'High':
        results = food_data[food_data[selected_nutrient] > (0.66 * max_value)]
    else:
        raise ValueError("Invalid level specified")

    return results


def get_comparison_click(food_data, selected_nutrient, selected_foods):

    if len(selected_foods) != 3:
        raise ValueError("Exactly three foods must be selected for comparison.")

    try:
        # Retrieve data for each selected food
        food_values = [food_data[food_data['food'] == food].iloc[0][selected_nutrient] for food in selected_foods]
    except IndexError:
        raise ValueError("One or more selected foods are not present in the dataset.")

    return selected_foods, food_values





