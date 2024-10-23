from Classes_Intro/class_example import Animal

def test_get_name():
    testanimal = Animal("Bob", "Bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "Bob"