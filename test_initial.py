from main import process
def test_number_one():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            assert process(i) == "FizzBuzz"
        elif i % 3 == 0:
            assert process(i) == "Fizz"
        elif i % 5 == 0:
            assert process(i) == "Buzz"
        else:
            assert process(i) == i