people = ['John', 'Mary', 'Toby']

def fake_function(name: str = people[0]) -> None:
    print( f"{name}, this is a fake function!")

def main():
    fake_function()

if __name__ == '__main__':

    print(people)
    main()
