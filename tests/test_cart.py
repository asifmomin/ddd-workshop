from ddd_workshop.cart import Cart, Item


def test_add_item():
    cart = Cart()
    ipad = Item("IPad Pro")
    pen = Item("HeroInk Pen")
    bat = Item("GM Cricket Bat", 2)
    expected = [ipad, pen, bat]
    cart.addItem(ipad)
    cart.addItem(pen)
    cart.addItem(bat)
    assert cart.length() == 3
    assert cart.getItems() == expected
    assert cart.getTotalItemCount() == 4
