from Drag_and_Drop import Drag_Drop
from Drag_and_Drop import Locators
from Drag_and_Drop import Data
from time import sleep


#creating object from Drag_and_Drop

My_Drag_and_Drop=Drag_Drop()

def test_start():
    assert My_Drag_and_Drop.start()==None
    print("Automation Started")

# Creating positive test case for Source box display

def test_source_box_displayed():
    assert My_Drag_and_Drop.Source_Box
    print("Source Box is Displayed Properly")

#Creating negative test case for Source box display

# def test_source_box_Not_displayed():
#     assert My_Drag_and_Drop.Source_Box==False
#     print("Source Box is Not Displayed Properly")

#Creating positive test case for Target box display

def test_target_box_displayed():
    assert My_Drag_and_Drop.Target_Box
    print("Target Box is Displayed Properly")

#Creating negative test case for Source box display

# def test_target_box_Not_displayed():
#     assert My_Drag_and_Drop.Target_Box==False
#     print("Target Box is Not Displayed Properly")

#creating test case for drag and drop function

def test_Drag_and_Drop_Function():
    assert My_Drag_and_Drop.drag_and_drop()==None
    print("Successful Drag and Drop")




