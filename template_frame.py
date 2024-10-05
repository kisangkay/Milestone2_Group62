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

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.Home = wx.Button( self, wx.ID_ANY, _(u"Home"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.Home, 0, wx.ALL, 5 )

        self.FoodSearch_button = wx.Button( self, wx.ID_ANY, _(u"Food Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.FoodSearch_button, 0, wx.ALL, 5 )

        self.NutrientBreakdown_button = wx.Button( self, wx.ID_ANY, _(u"Nutrient Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.NutrientBreakdown_button, 0, wx.ALL, 5 )

        self.NutritionRangeFilter_button = wx.Button( self, wx.ID_ANY, _(u"Nutrition Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.NutritionRangeFilter_button, 0, wx.ALL, 5 )

        self.NutritionalLevelFilter_button = wx.Button( self, wx.ID_ANY, _(u"Nutrition Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.NutritionalLevelFilter_button, 0, wx.ALL, 5 )

        self.NutritionalDensityVisualizer_button = wx.Button( self, wx.ID_ANY, _(u"Nutritional Density Visualizer"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.NutritionalDensityVisualizer_button, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class FoodSearch_Dialog
###########################################################################

class FoodSearch_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 618,270 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Food Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.Search_button = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.Search_button, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer5, 0, 0, 0 )

        self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid3.CreateGrid( 5, 5 )
        self.m_grid3.EnableEditing( True )
        self.m_grid3.EnableGridLines( True )
        self.m_grid3.EnableDragGridSize( False )
        self.m_grid3.SetMargins( 0, 0 )

        # Columns
        self.m_grid3.EnableDragColMove( False )
        self.m_grid3.EnableDragColSize( True )
        self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid3.EnableDragRowSize( True )
        self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer3.Add( self.m_grid3, 0, wx.ALL, 0 )


        self.SetSizer( bSizer3 )
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
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,900 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.Label = wx.StaticText( self, wx.ID_ANY, _(u"Select Food:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Label.Wrap( -1 )

        bSizer7.Add( self.Label, 0, wx.ALL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        m_listBox6Choices = []
        self.m_listBox6 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox6Choices, 0 )
        bSizer10.Add( self.m_listBox6, 0, 0, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10.Add( self.m_panel3, 0, 0, 5 )


        bSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer7, 5, wx.EXPAND, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


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

        bSizer121.Add( self.nutrient_label, 0, wx.ALL, 5 )

        nutrient_choiceChoices = []
        self.nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nutrient_choiceChoices, 0 )
        self.nutrient_choice.SetSelection( 0 )
        bSizer121.Add( self.nutrient_choice, 0, wx.ALL, 5 )


        bSizer12.Add( bSizer121, 1, wx.EXPAND, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Min Range: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer12.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Max Range:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer12.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.Filter_button = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.Filter_button, 0, wx.ALL, 5 )


        bSizer11.Add( bSizer12, 0, wx.EXPAND, 2 )

        self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid5.CreateGrid( 5, 5 )
        self.m_grid5.EnableEditing( True )
        self.m_grid5.EnableGridLines( True )
        self.m_grid5.EnableDragGridSize( False )
        self.m_grid5.SetMargins( 0, 0 )

        # Columns
        self.m_grid5.EnableDragColMove( False )
        self.m_grid5.EnableDragColSize( True )
        self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid5.EnableDragRowSize( True )
        self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer11.Add( self.m_grid5, 0, wx.ALL, 0 )


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

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Select level of Nutritional Food:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer13.Add( self.m_staticText11, 0, wx.ALL, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        bSizer14.Add( self.m_staticText14, 0, wx.ALL, 5 )

        self.low_checkbox = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.low_checkbox, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer14.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.medium_checkbox = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.medium_checkbox, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer14.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.High_checkbox = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.High_checkbox, 0, wx.ALL, 5 )

        self.Filter_button = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.Filter_button, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer14, 0, 0, 5 )

        self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid6.CreateGrid( 5, 5 )
        self.m_grid6.EnableEditing( True )
        self.m_grid6.EnableGridLines( True )
        self.m_grid6.EnableDragGridSize( False )
        self.m_grid6.SetMargins( 0, 0 )

        # Columns
        self.m_grid6.EnableDragColMove( False )
        self.m_grid6.EnableDragColSize( True )
        self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid6.EnableDragRowSize( True )
        self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer13.Add( self.m_grid6, 0, wx.ALL, 0 )


        self.SetSizer( bSizer13 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class NutritionalDensityVisualizer_Dialog
###########################################################################

class NutritionalDensityVisualizer_Dialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Select Foods to Visualize Nutritional Density:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer15.Add( self.m_staticText18, 0, wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        SelectFood_ChoiceChoices = []
        self.SelectFood_Choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SelectFood_ChoiceChoices, 0 )
        self.SelectFood_Choice.SetSelection( 0 )
        bSizer16.Add( self.SelectFood_Choice, 0, wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer16.Add( self.m_staticText19, 0, wx.ALL, 5 )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.m_button12 = wx.Button( self, wx.ID_ANY, _(u"Visualize"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button12, 0, wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer16.Add( bSizer17, 1, wx.EXPAND, 5 )


        bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


