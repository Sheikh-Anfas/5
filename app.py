def greeting(name):
    name = name.strip()
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greeting("GitHub"))
