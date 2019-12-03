from terminal.menu import Menu

def test_display_menu():
    """Test the method menu.display_menu()"""

    menu = Menu(["Configuration", "Lancer le test"])
    test_menu_selected = menu.display_menu()
    value_expected = "2"
    assert test_menu_selected == value_expected