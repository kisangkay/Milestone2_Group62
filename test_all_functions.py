import pandas as pd
import pytest

from all_functions import on_search, get_on_food_selected, get_on_filter, get_filter_nutrition_level, \
    get_comparison_click


def test_on_search_valid():
    df = pd.DataFrame({'food': ['apple', 'banana', 'cherry', 'apple pie', 'blueberry']})
    result = on_search(df, 'apple')
    assert not result.empty
    assert len(result) == 2  # 'apple' and 'apple pie'

    result = on_search(df, 'banana')
    assert not result.empty
    assert len(result) == 1  # 'banana'

    result = on_search(df, 'berry')
    assert not result.empty
    assert len(result) == 1  # 'blueberry'



def test_on_search_invalid():
    df = pd.DataFrame({'food': ['apple', 'banana', 'cherry', 'apple pie', 'blueberry']})
    result = on_search(df, '')
    assert result.empty  # Should be empty since no search term is provided

    result = on_search(df, 'group62')
    assert result.empty  # Should be empty as the search term does not exist in the data


def test_on_food_selected_valid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana'],
        'Caloric Value': [52, 89],
        'Fat': [0.2, 0.3],
        'Saturated Fats': [0.03, 0.11],
        'Protein': [0.3, 1.1]
    })

    selected_food = 'Apple'
    categories, sizes = get_on_food_selected(food_data, selected_food)

    # Assert that the extracted nutrient data matches the expected values for 'Apple'
    assert categories == ['Caloric Value', 'Fat', 'Saturated Fats', 'Protein']
    assert sizes == [52, 0.2, 0.03, 0.3]


def test_on_food_selected_invalid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana'],
        'Caloric Value': [52, 89],
        'Fat': [0.2, 0.3],
        'Saturated Fats': [0.03, 0.11],
        'Protein': [0.3, 1.1]
    })

    selected_food = 'Orange'

    # Call the function and check if the appropriate exception is handled
    with pytest.raises(IndexError) as exc_info:
        get_on_food_selected(food_data, selected_food)
    assert exc_info.type is IndexError


def test_on_filter_valid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Nutrition Density': [30, 45, 10],
        'Protein': [0.3, 1.1, 0.9]
    })

    # Test with Nutrition Density filter
    nutrient = 'Nutrition Density'
    min_density = 10
    max_density = 50
    results = get_on_filter(food_data, nutrient, min_density, max_density)

    assert len(results) == 3  # All rows are within range
    assert 'Apple' in results['food'].values
    assert 'Banana' in results['food'].values
    assert 'Carrot' in results['food'].values

    # Test with Protein filter
    nutrient = 'Protein'
    min_density = 0.5
    max_density = 2
    results = get_on_filter(food_data, nutrient, min_density, max_density)

    assert len(results) == 2  # Only Banana and Carrot are within the range
    assert 'Banana' in results['food'].values
    assert 'Carrot' in results['food'].values


def test_on_filter_invalid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Nutrition Density': [30, 45, 10],
        'Protein': [0.3, 1.1, 0.9]
    })

    # Test with an invalid nutrient
    nutrient = 'group62'
    min_density = 0
    max_density = 50

    # Call the function and check if the appropriate exception is raised
    with pytest.raises(KeyError) as exc_info:
        get_on_filter(food_data, nutrient, min_density, max_density)
    assert exc_info.type is KeyError


def test_filter_nutrition_level_valid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Protein': [0.3, 1.1, 0.9]
    })

    max_protein = food_data['Protein'].max()  # max value is 1.1

    # Test with 'Low' level
    results = get_filter_nutrition_level(food_data, 'Protein', 'Low')
    assert len(results) == 1  # Only 'Apple' should be in the Low category
    assert 'Apple' in results['food'].values

    # Test with 'Mid' level
    results = get_filter_nutrition_level(food_data, 'Protein', 'Mid')
    assert len(results) == 0  # No food item falls in the Midcategory according to the range

    # Test with 'High' level
    results = get_filter_nutrition_level(food_data, 'Protein', 'High')
    assert len(results) == 2  # Both 'Banana' and 'Carrot' should be in the High category
    assert 'Banana' in results['food'].values
    assert 'Carrot' in results['food'].values




def test_filter_nutrition_level_invalid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Protein': [0.3, 1.1, 0.9]
    })

    # Test with an unknown nutrient
    with pytest.raises(KeyError) as exc_info:
        get_filter_nutrition_level(food_data, 'group62', 'Low')
    assert exc_info.type is KeyError

    # Test with an invalid level
    with pytest.raises(ValueError) as exc_info:
        get_filter_nutrition_level(food_data, 'Protein', 'large')
    assert exc_info.type is ValueError


def test_get_comparison_click_valid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Protein': [0.3, 1.1, 0.9]
    })

    selected_nutrient = 'Protein'
    selected_foods = ['Apple', 'Banana', 'Carrot']

    labels, values = get_comparison_click(food_data, selected_nutrient, selected_foods)

    # Assert that the labels and values match the expected output
    assert labels == ['Apple', 'Banana', 'Carrot']
    assert values == [0.3, 1.1, 0.9]


def test_get_comparison_click_invalid():
    # Mock food data
    food_data = pd.DataFrame({
        'food': ['Apple', 'Banana', 'Carrot'],
        'Protein': [0.3, 1.1, 0.9]
    })

    selected_nutrient = 'Protein'

    # Test with less than three foods
    selected_foods = ['Apple', 'Banana']
    with pytest.raises(ValueError) as exc_info:
        get_comparison_click(food_data, selected_nutrient, selected_foods)
    assert str(exc_info.value) == "Exactly three foods must be selected for comparison."

    # Test with a food not present in the dataset
    selected_foods = ['Apple', 'Banana', 'Orange']
    with pytest.raises(ValueError) as exc_info:
        get_comparison_click(food_data, selected_nutrient, selected_foods)
    assert str(exc_info.value) == "One or more selected foods are not present in the dataset."
