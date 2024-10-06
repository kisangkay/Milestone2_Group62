# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 803,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

        bSizer30 = wx.BoxSizer( wx.VERTICAL )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.Home = wx.Button( self, wx.ID_ANY, _(u"Home"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.Home.SetBitmap( wx.Bitmap( u"gui_bitmaps/house.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.Home, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.FoodSearch_button = wx.Button( self, wx.ID_ANY, _(u"Food Search"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.FoodSearch_button.SetBitmap( wx.Bitmap( u"gui_bitmaps/search.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.FoodSearch_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.NutrientBreakdown_button = wx.Button( self, wx.ID_ANY, _(u"Nutrient Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.NutrientBreakdown_button.SetBitmap( wx.Bitmap( u"gui_bitmaps/pie-chart.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.NutrientBreakdown_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.NutritionRangeFilter_button = wx.Button( self, wx.ID_ANY, _(u"Nutrition Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.NutritionRangeFilter_button.SetBitmap( wx.Bitmap( u"gui_bitmaps/arrow.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.NutritionRangeFilter_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.NutritionalLevelFilter_button = wx.Button( self, wx.ID_ANY, _(u"Nutrition Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.NutritionalLevelFilter_button.SetBitmap( wx.Bitmap( u"gui_bitmaps/alt.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.NutritionalLevelFilter_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.NutritionalDensityVisualizer_button = wx.Button( self, wx.ID_ANY, _(u"Nutritional Density Visualizer"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.NutritionalDensityVisualizer_button.SetBitmap( wx.Bitmap( u"gui_bitmaps/bar.bmp", wx.BITMAP_TYPE_RESOURCE ) )
        bSizer1.Add( self.NutritionalDensityVisualizer_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer30.Add( bSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        self.welcome_text = wx.StaticText( self, wx.ID_ANY, _(u"Welcome to Nutrient Analyzer. To get started, please select from the options above"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.welcome_text.Wrap( -1 )

        bSizer29.Add( self.welcome_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer30.Add( bSizer29, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer30 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.FoodSearch_button.Bind( wx.EVT_BUTTON, self.on_food_search_click )
        self.NutrientBreakdown_button.Bind( wx.EVT_BUTTON, self.on_nutrient_breakdown_click )
        self.NutritionRangeFilter_button.Bind( wx.EVT_BUTTON, self.on_nutrient_range_filter_click )
        self.NutritionalLevelFilter_button.Bind( wx.EVT_BUTTON, self.on_nutrient_level_filter_click )
        self.NutritionalDensityVisualizer_button.Bind( wx.EVT_BUTTON, self.open_nutritional_density_visualizer )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_food_search_click( self, event ):
        event.Skip()

    def on_nutrient_breakdown_click( self, event ):
        event.Skip()

    def on_nutrient_range_filter_click( self, event ):
        event.Skip()

    def on_nutrient_level_filter_click( self, event ):
        event.Skip()

    def open_nutritional_density_visualizer( self, event ):
        event.Skip()


###########################################################################
## Class FoodSearch_Dialog
###########################################################################

class FoodSearch_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 803,480 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer35 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, _(u"Enter a food name to view its nutritional details"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer3.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Food Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.Search_button = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.Search_button, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )


        bSizer35.Add( bSizer3, 0, wx.EXPAND, 5 )

        self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

        # Grid
        self.m_grid3.CreateGrid( 5, 5 )
        self.m_grid3.EnableEditing( True )
        self.m_grid3.EnableGridLines( True )
        self.m_grid3.EnableDragGridSize( False )
        self.m_grid3.SetMargins( 0, 0 )

        # Columns
        self.m_grid3.SetColSize( 0, 193 )
        self.m_grid3.SetColSize( 1, 130 )
        self.m_grid3.SetColSize( 2, 135 )
        self.m_grid3.SetColSize( 3, 129 )
        self.m_grid3.SetColSize( 4, 278 )
        self.m_grid3.EnableDragColMove( False )
        self.m_grid3.EnableDragColSize( True )
        self.m_grid3.SetColLabelValue( 0, _(u"Food Name") )
        self.m_grid3.SetColLabelValue( 1, _(u"Nutrition value 1") )
        self.m_grid3.SetColLabelValue( 2, _(u"Nutrition value 2") )
        self.m_grid3.SetColLabelValue( 3, _(u"Nutrition value 3") )
        self.m_grid3.SetColLabelValue( 4, _(u"Nutrition value 4") )
        self.m_grid3.SetColLabelValue( 5, _(u"Nutrition value 5") )
        self.m_grid3.SetColLabelValue( 6, _(u"Nutrition value 6") )
        self.m_grid3.SetColLabelValue( 7, _(u"Nutrition value 7") )
        self.m_grid3.SetColLabelValue( 8, _(u"Nutrition value 8") )
        self.m_grid3.SetColLabelValue( 9, _(u"Nutrition value 9") )
        self.m_grid3.SetColLabelValue( 10, _(u"Nutrition value 10") )
        self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize( True )
        self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer35.Add( self.m_grid3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )


        self.SetSizer( bSizer35 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Search_button.Bind( wx.EVT_BUTTON, self.on_search_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_search_click( self, event ):
        event.Skip()


###########################################################################
## Class NutrientBreakdown_Dialog
###########################################################################

class NutrientBreakdown_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 803,480 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer6.SetMinSize( wx.Size( 803,480 ) )
        self.food_label = wx.StaticText( self, wx.ID_ANY, _(u"Select Food:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.food_label.Wrap( -1 )

        bSizer6.Add( self.food_label, 0, wx.ALL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        m_listBox6Choices = []
        self.m_listBox6 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox6Choices, 0 )
        bSizer10.Add( self.m_listBox6, 0, 0, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_listBox6.Bind( wx.EVT_LISTBOX, self.on_food_selected )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_food_selected( self, event ):
        event.Skip()


###########################################################################
## Class NutrientRangeFilter_Dialog
###########################################################################

class NutrientRangeFilter_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,453 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizer121 = wx.BoxSizer( wx.VERTICAL )

        self.nutrient_label = wx.StaticText( self, wx.ID_ANY, _(u"Select Nutrient"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nutrient_label.Wrap( -1 )

        bSizer121.Add( self.nutrient_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        nutrient_choiceChoices = []
        self.nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nutrient_choiceChoices, 0 )
        self.nutrient_choice.SetSelection( 0 )
        bSizer121.Add( self.nutrient_choice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer12.Add( bSizer121, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Min Range: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer21.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Max Range:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer21.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Filter_button = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.Filter_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer12.Add( bSizer21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer11.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 2 )

        self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid5.CreateGrid( 5, 2 )
        self.m_grid5.EnableEditing( False )
        self.m_grid5.EnableGridLines( True )
        self.m_grid5.EnableDragGridSize( False )
        self.m_grid5.SetMargins( 0, 0 )

        # Columns
        self.m_grid5.SetColSize( 0, 300 )
        self.m_grid5.SetColSize( 1, 200 )
        self.m_grid5.EnableDragColMove( False )
        self.m_grid5.EnableDragColSize( True )
        self.m_grid5.SetColLabelValue( 0, _(u"Food Name") )
        self.m_grid5.SetColLabelValue( 1, _(u"Value") )
        self.m_grid5.SetColLabelValue( 2, wx.EmptyString )
        self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid5.AutoSizeRows()
        self.m_grid5.EnableDragRowSize( True )
        self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer11.Add( self.m_grid5, 1, wx.ALIGN_CENTER, 0 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class NutritionalLevelFilter_Dialog
###########################################################################

class NutritionalLevelFilter_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Select Nutrient to check its levels"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer13.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        nutrient_choiceChoices = []
        self.nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nutrient_choiceChoices, 0 )
        self.nutrient_choice.SetSelection( 0 )
        bSizer13.Add( self.nutrient_choice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, _(u"Select Nutrient Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )

        bSizer13.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.low_radio = wx.RadioButton( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.low_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.medium_radio = wx.RadioButton( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.medium_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.high_radio = wx.RadioButton( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.high_radio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer13.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.Filter_button = wx.Button( self, wx.ID_ANY, _(u"Filter Food Items for that Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
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
    def filter_nutrition_level( self, event ):
        event.Skip()


###########################################################################
## Class NutritionalDensity_Comparison_Dialog
###########################################################################

class NutritionalDensity_Comparison_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,700 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        bSizer25 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Select Foods to Visualize Nutritional Density"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer25.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer251 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, _(u"Which Nutrient do you want to Compare?"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText181.Wrap( -1 )

        bSizer251.Add( self.m_staticText181, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        select_nutrient_choiceChoices = []
        self.select_nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, select_nutrient_choiceChoices, 0 )
        self.select_nutrient_choice.SetSelection( 0 )
        bSizer251.Add( self.select_nutrient_choice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer25.Add( bSizer251, 1, wx.EXPAND, 5 )


        bSizer15.Add( bSizer25, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, _(u"Food Choice 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer16.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        SelectFood_Choice_1Choices = []
        self.SelectFood_Choice_1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), SelectFood_Choice_1Choices, 0 )
        self.SelectFood_Choice_1.SetSelection( 0 )
        bSizer16.Add( self.SelectFood_Choice_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.SelectFood_Choice_21 = wx.StaticText( self, wx.ID_ANY, _(u"Food Choice 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SelectFood_Choice_21.Wrap( -1 )

        bSizer16.Add( self.SelectFood_Choice_21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        SelectFood_Choice_2Choices = []
        self.SelectFood_Choice_2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), SelectFood_Choice_2Choices, 0 )
        self.SelectFood_Choice_2.SetSelection( 0 )
        bSizer16.Add( self.SelectFood_Choice_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.SelectFood_Choice_31 = wx.StaticText( self, wx.ID_ANY, _(u"Food Choice 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SelectFood_Choice_31.Wrap( -1 )

        bSizer16.Add( self.SelectFood_Choice_31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        SelectFood_Choice_3Choices = []
        self.SelectFood_Choice_3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), SelectFood_Choice_3Choices, 0 )
        self.SelectFood_Choice_3.SetSelection( 0 )
        bSizer16.Add( self.SelectFood_Choice_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer15.Add( bSizer16, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

        self.visualize_comparison = wx.Button( self, wx.ID_ANY, _(u"Visualize"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.visualize_comparison, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer15.Add( bSizer24, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        bSizer17.SetMinSize( wx.Size( 500,-1 ) )
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer15.Add( bSizer17, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.visualize_comparison.Bind( wx.EVT_BUTTON, self.visualize_comparison_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def visualize_comparison_click( self, event ):
        event.Skip()


