import wx
import wx.xrc
import wx.grid
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import pandas as pd
import re
import template_frame
import gettext
_ = gettext.gettext

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

# Load the CSV file
csv_file = 'Food_Nutrition_Dataset.csv'
food_data = pd.read_csv(csv_file)

class FoodDataTable(wx.grid.GridTableBase):
    def __init__(self, data):
        super(FoodDataTable, self).__init__()
        self.data = data
        self.col_labels = data.columns.tolist()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.col_labels)

    def GetValue(self, row, col):
        return str(self.data.iloc[row, col])

    def GetColLabelValue(self, col):
        return self.col_labels[col]


# Create a subclass of the MainFrame generated by wxFormBuilder
class MyAppFrame(template_frame.MainFrame):
    def __init__(self, parent=None):
        super(MyAppFrame, self).__init__(parent)

        # Bind the event for the "Food Search" button
        self.FoodSearch_button.Bind(wx.EVT_BUTTON, self.on_food_search_click)
        self.NutrientBreakdown_button.Bind(wx.EVT_BUTTON, self.on_nutrient_breakdown_click)
        self.NutritionRangeFilter_button.Bind(wx.EVT_BUTTON, self.on_nutrient_range_filter_click)
        self.NutritionalLevelFilter_button.Bind(wx.EVT_BUTTON, self.on_nutrient_level_filter_click)
        self.NutritionalDensityVisualizer_button.Bind(wx.EVT_BUTTON, self.open_nutritional_density_visualizer)

    # Event handler for the Food Search button
    def on_food_search_click(self, event):
        dialog = FoodSearchDialog(self)
        dialog.ShowModal()  # Open the dialog when the button is clicked
        dialog.Destroy()

     # Event handler for the Nutrient Breakdown button
    def on_nutrient_breakdown_click(self, event):
        dialog = NutrientBreakdown_Dialog(self)
        dialog.ShowModal()
        dialog.Destroy()

    def on_nutrient_range_filter_click(self, event):
        dialog = NutrientRangeFilter_Dialog(self)
        dialog.ShowModal()
        dialog.Destroy()

    def on_nutrient_level_filter_click(self, event):
        dialog = NutritionalLevelFilter_Dialog(self)
        dialog.ShowModal()
        dialog.Destroy()

    def open_nutritional_density_visualizer(self, event):
        dialog = NutritionalDensity_Comparison_Dialog(self)
        dialog.ShowModal()
        dialog.Destroy()


# Create a subclass of FoodSearch_Dialog generated by wxFormBuilder
class FoodSearchDialog(template_frame.FoodSearch_Dialog):
    def __init__(self, parent):
        super(FoodSearchDialog, self).__init__(parent)

        # Load the CSV data (Food_Nutrition_Dataset.csv)
        self.df = pd.read_csv('Food_Nutrition_Dataset.csv')

        # Set initial grid table with full data
        self.table = FoodDataTable(self.df)
        self.m_grid3.SetTable(self.table, takeOwnership=True)
        self.m_grid3.AutoSize()

        # Bind the Search button event
        self.Search_button.Bind(wx.EVT_BUTTON, self.on_search_click)

    # Event handler for the Search button
    def on_search_click(self, event):
        search_term = self.m_textCtrl1.GetValue().lower()  # Get search term from the text box
        if search_term:
            # Filter food data based on the search term in the 'Food' column
            filtered_data = self.df[self.df['food'].str.contains(search_term, case=False)]

            # Update the grid with the filtered data
            self.update_grid(filtered_data)

    # Function to update the grid with filtered data
    def update_grid(self, data):
        self.m_grid3.ClearGrid()

        # Create a new table with the filtered data and set it in the grid
        self.table = FoodDataTable(data)
        self.m_grid3.SetTable(self.table, takeOwnership=True)
        self.m_grid3.AutoSize()

        # # Optionally, update any static text to show the number of results found
        # result_count = f"{len(data)} results found"
        # self.SetStatusText(result_count)
class NutrientBreakdown_Dialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="Nutrient Breakdown", pos=wx.DefaultPosition,
                           size=wx.Size(600, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # Vertical box sizer for main layout
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        # Vertical sizer for Label and ListBox/Panel layout
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        # StaticText (Label) for "Select Food"
        self.food_label = wx.StaticText(self, wx.ID_ANY, u"Select Food:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.food_label.Wrap(-1)
        bSizer7.Add(self.food_label, 0, wx.ALL, 5)

        # Horizontal sizer for ListBox and Panel
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        # Load the data from the CSV file using pandas
        self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')  # Ensure the file name matches your actual file

        # Extract food names for the ListBox
        food_choices = self.food_data['food'].tolist()  # Extract the list of food items
        self.m_listBox6 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, food_choices, 0)
        bSizer10.Add(self.m_listBox6, 0, wx.ALL, 5)

        # Add Panel to display pie chart
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background for the panel
        bSizer10.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        # Add horizontal sizer to vertical sizer
        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        # Add everything to the main sizer
        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Bind the ListBox selection event to the handler function
        self.m_listBox6.Bind(wx.EVT_LISTBOX, self.on_food_selected)

    def on_food_selected(self, event):
        # Get the selected food from the ListBox
        selected_food = self.m_listBox6.GetStringSelection()

        # Find the row corresponding to the selected food
        food_info = self.food_data[self.food_data['food'] == selected_food].iloc[0]

        # Extract nutrient data for the pie chart
        categories = ['Caloric Value', 'Fat', 'Saturated Fats', 'Protein']
        sizes = [food_info['Caloric Value'], food_info['Fat'], food_info['Saturated Fats'], food_info['Protein']]
        colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]

        # Create the figure and axis for the pie chart
        fig, ax = plt.subplots(1, 1, figsize=(4, 4))

        # Plot pie chart
        ax.pie(sizes, labels=categories, colors=colors, autopct="%1.1f%%", shadow=True, explode=(0.1, 0.0, 0.0, 0.0))
        ax.set_title(f"Nutrient Breakdown of {selected_food}")

        # Get the panel size to properly fit the chart
        h, w = self.m_panel3.GetSize()
        fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

        # Embed the Matplotlib figure in the wxPython Panel
        canvas = FigureCanvas(self.m_panel3, -1, fig)
        canvas.SetSize((h, w))

        # Update the layout and refresh the panel to display the chart
        self.Layout()
        self.m_panel3.Refresh()


class NutrientRangeFilter_Dialog ( wx.Dialog ):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="Nutrition Density Range Filter", pos=wx.DefaultPosition, size=wx.Size(600,453), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer121 = wx.BoxSizer(wx.VERTICAL)

        self.nutrient_label = wx.StaticText(self, wx.ID_ANY, _(u"Select Nutrient"), wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.nutrient_label.Wrap(-1)

        bSizer121.Add(self.nutrient_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        nutrient_choiceChoices = []
        self.nutrient_choice = wx.Choice(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,choices=food_data.columns[1:].tolist())
        self.nutrient_choice.SetSelection(0)
        bSizer121.Add(self.nutrient_choice, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer12.Add(bSizer121, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, _(u"Min Range: "), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer21.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_textCtrl2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, _(u"Max Range:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer21.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_textCtrl3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Filter_button = wx.Button(self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.Filter_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer12.Add(bSizer21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer11.Add(bSizer12, 0, 0, 2)

        self.m_grid5 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid5.CreateGrid(5, 2)
        self.m_grid5.EnableEditing(False)
        self.m_grid5.EnableGridLines(True)
        self.m_grid5.EnableDragGridSize(False)
        self.m_grid5.SetMargins(0, 0)

        # Columns
        self.m_grid5.SetColSize(0, 300)
        self.m_grid5.SetColSize(1, 200)
        self.m_grid5.EnableDragColMove(False)
        self.m_grid5.EnableDragColSize(True)
        self.m_grid5.SetColLabelValue(0, _(u"Food Name"))
        self.m_grid5.SetColLabelValue(1, _(u"Value"))
        self.m_grid5.SetColLabelValue(2, wx.EmptyString)
        self.m_grid5.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid5.AutoSizeRows()
        self.m_grid5.EnableDragRowSize(True)
        self.m_grid5.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid5.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer11.Add(self.m_grid5, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

        # Bind events
        self.Filter_button.Bind(wx.EVT_BUTTON, self.on_filter)

        # Load the data from the CSV file
        self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')

    def on_filter(self, event):
        # Get the input values for Nutrition Density
        nutrient = self.nutrient_choice.GetString(self.nutrient_choice.GetSelection())
        min_nutrition_density = float(self.m_textCtrl2.GetValue() or 0)
        max_nutrition_density = float(self.m_textCtrl3.GetValue() or float('inf'))

        results = food_data[(food_data[nutrient] >= min_nutrition_density) & (food_data[nutrient] <= max_nutrition_density)]

        # Filter the DataFrame based on Nutrition Density
        results = self.food_data[
            (self.food_data['Nutrition Density'] >= min_nutrition_density) &
            (self.food_data['Nutrition Density'] <= max_nutrition_density)
        ]

        # Clear previous results from the grid
        self.m_grid5.ClearGrid()
        self.m_grid5.DeleteRows(0, self.m_grid5.GetNumberRows())  # Clear previous rows

        # Populate the results grid with the filtered food items
        for index, row in results.iterrows():
            self.m_grid5.AppendRows(1)  # Append a new row
            self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows() - 1, 0, row['food'])  # Food name
            self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows() - 1, 1, str(row['Nutrition Density']))  # Nutrition Density (additional columns can be added as needed)

class NutritionalLevelFilter_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Select level of Nutrition"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer13.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.low_radio = wx.RadioButton( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.low_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.medium_radio = wx.RadioButton( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.medium_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.high_radio = wx.RadioButton( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.high_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer13.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.Filter_button = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.Filter_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer13.Add( bSizer23, 0, wx.ALIGN_CENTER, 5 )

        self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid6.CreateGrid( 5, 2 )
        self.m_grid6.EnableEditing( True )
        self.m_grid6.EnableGridLines( True )
        self.m_grid6.EnableDragGridSize( False )
        self.m_grid6.SetMargins( 0, 0 )

        # Columns
        self.m_grid6.SetColSize( 0, 274 )
        self.m_grid6.SetColSize( 1, 121 )
        self.m_grid6.EnableDragColMove( False )
        self.m_grid6.EnableDragColSize( True )
        self.m_grid6.SetColLabelValue( 0, _(u"Food Name") )
        self.m_grid6.SetColLabelValue( 1, _(u"Nutrition Density") )
        self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid6.EnableDragRowSize( True )
        self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer13.Add( self.m_grid6, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


        self.SetSizer( bSizer13 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Filter_button.Bind( wx.EVT_BUTTON, self.filter_nutrition_level )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class

    def filter_nutrition_level(self, event):
        if self.low_radio.GetValue():
            level = 'Low'
        elif self.medium_radio.GetValue():
            level = 'Mid'
        elif self.high_radio.GetValue():
            level = 'High'
        else:
            return

        nutrient = 'Nutrition Density'
        max_value = food_data[nutrient].max()

        if level == 'Low':
            results = food_data[food_data[nutrient] < (0.33 * max_value)]
        elif level == 'Mid':
            results = food_data[(food_data[nutrient] >= (0.33 * max_value)) & (food_data[nutrient] <= (0.66 * max_value))]
        else:
            results = food_data[food_data[nutrient] > (0.66 * max_value)]

        # Clear previous results from the grid
        self.m_grid6.ClearGrid()
        self.m_grid6.DeleteRows(0, self.m_grid6.GetNumberRows())  # Clear previous rows

        # Populate the results grid with the filtered food items
        for index, row in results.iterrows():
            self.m_grid6.AppendRows(1)  # Append a new row
            self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows() - 1, 0, row['food'])
            self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows() - 1, 1, str(
                row['Nutrition Density']))

#Feature 5
class NutritionalDensity_Comparison_Dialog ( wx.Dialog ):


    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(900, 700),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, _(u"Select Foods to Visualize Nutritional Density"),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)

        bSizer25.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer251 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText181 = wx.StaticText(self, wx.ID_ANY, _(u"Which Nutrient do you want to Compare?"),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText181.Wrap(-1)

        bSizer251.Add(self.m_staticText181, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

    #select from the first row (all nutrients listed here so)
        select_nutrient_choiceChoices = []
        self.select_nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                choices=food_data.columns[1:].tolist())
        self.select_nutrient_choice.SetSelection(0)
        bSizer251.Add(self.select_nutrient_choice, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer25.Add( bSizer251, 1, wx.EXPAND, 5 )

        bSizer15.Add( bSizer25, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, _(u"Food Choice 1"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)

        bSizer16.Add(self.m_staticText19, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        SelectFood_Choice_1Choices = []
        self.SelectFood_Choice_1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1),
                                             choices=food_data['food'].tolist())
        bSizer16.Add(self.SelectFood_Choice_1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SelectFood_Choice_21 = wx.StaticText(self, wx.ID_ANY, _(u"Food Choice 2"), wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.SelectFood_Choice_21.Wrap(-1)

        bSizer16.Add(self.SelectFood_Choice_21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        SelectFood_Choice_2Choices = []
        self.SelectFood_Choice_2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), choices=food_data['food'].tolist())
        self.SelectFood_Choice_2.SetSelection(0)
        bSizer16.Add(self.SelectFood_Choice_2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SelectFood_Choice_31 = wx.StaticText(self, wx.ID_ANY, _(u"Food Choice 3"), wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.SelectFood_Choice_31.Wrap(-1)

        bSizer16.Add(self.SelectFood_Choice_31, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        SelectFood_Choice_3Choices = []
        self.SelectFood_Choice_3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), choices=food_data['food'].tolist())
        self.SelectFood_Choice_3.SetSelection( 0 )
        bSizer16.Add(self.SelectFood_Choice_3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer15.Add(bSizer16, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer24 = wx.BoxSizer(wx.HORIZONTAL)

        self.visualize_comparison = wx.Button(self, wx.ID_ANY, _(u"Visualize"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer24.Add(self.visualize_comparison, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer15.Add(bSizer24, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        bSizer17.SetMinSize(wx.Size(500, -1))
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        bSizer15.Add(bSizer17, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer15)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.visualize_comparison.Bind(wx.EVT_BUTTON, self.visualize_comparison_click)

    def __del__(self):
        pass


    # Virtual event handlers, override them in your derived class
    def visualize_comparison_click(self, event):
        # Load the CSV file
        csv_file = 'Food_Nutrition_Dataset.csv'
        food_datas = pd.read_csv(csv_file)

        # Get the selected nutrient from the dropdown
        selected_nutrient = self.select_nutrient_choice.GetString(self.select_nutrient_choice.GetSelection())

        #then we get the 3 different foods from drop down
        selected_food1 = self.SelectFood_Choice_1.GetString(self.SelectFood_Choice_1.GetSelection())
        selected_food2 = self.SelectFood_Choice_2.GetString(self.SelectFood_Choice_2.GetSelection())
        selected_food3 = self.SelectFood_Choice_3.GetString(self.SelectFood_Choice_3.GetSelection())

        #then we retrieve the respective food names by filtering
        food_data1 = food_datas[food_datas['food'] == selected_food1].iloc[0]
        food_data2 = food_datas[food_datas['food'] == selected_food2].iloc[0]
        food_data3 = food_datas[food_datas['food'] == selected_food3].iloc[0]

        #then we generate the labels for the foods based on their selections
        labels = [selected_food1, selected_food2, selected_food3]

        #lets get the nutrient values for the selected foods
        values = [
            food_data1[selected_nutrient],
            food_data2[selected_nutrient],
            food_data3[selected_nutrient]
        ]

        #generate a Matplotlib figure
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['#ff9999', '#66b3ff', '#99ff99'])
        ax.set_title(f'Comparison of {selected_nutrient} in Selected Foods')
        ax.set_ylabel(selected_nutrient)

        #how to fix in the bar graph into our panel
        h, w = self.m_panel6.GetSize()
        fig.set_size_inches(w / fig.get_dpi(), h / fig.get_dpi())

        #to clear panel first
        if self.m_panel6.GetChildren():
            for child in self.m_panel6.GetChildren():
                child.Destroy()

        #place matplotlib figure into the panle
        canvas = FigureCanvas(self.m_panel6, -1, fig)
        canvas.SetSize((w, h))

        # Update the layout and refresh the panel to display the chart
        self.Layout()#layout updates,
        self.m_panel6.Refresh()#refresh panel


# Run the application
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyAppFrame(None)
    frame.Show()
    app.MainLoop()