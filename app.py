def learning_path():
    while True:
        goal = input("Enter what you want to learn (or type 'exit'): ").lower()

        if goal == "exit":
            print("Good luck with your learning! 🚀")
            break

        elif "python" in goal:
            print("\n📚 Learning Path for Python:")
            print("1. Learn basics (variables, loops, functions)")
            print("2. Practice problems")
            print("3. Learn OOP concepts")
            print("4. Work on mini projects")
            print("5. Explore libraries (NumPy, Pandas)\n")

        elif "web" in goal:
            print("\n🌐 Learning Path for Web Development:")
            print("1. Learn HTML")
            print("2. Learn CSS")
            print("3. Learn JavaScript")
            print("4. Build simple websites")
            print("5. Learn React or Node.js\n")

        elif "data" in goal:
            print("\n📊 Learning Path for Data Science:")
            print("1. Learn Python")
            print("2. Learn NumPy & Pandas")
            print("3. Learn Data Visualization")
            print("4. Learn Machine Learning basics")
            print("5. Work on real datasets\n")

        else:
            print("\n⚠️ Sorry, I don't have a roadmap for that yet.\n")

learning_path()
