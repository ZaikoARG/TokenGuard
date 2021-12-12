# TokenGuard
![TokenGuard2](https://user-images.githubusercontent.com/67133061/145713451-d7d3aaac-b5c0-4c0b-970d-dacd67adf370.png)
<p align="center">
    <em>TokenGuard, protect your account, prevent token steal. Totally free and open source</em></p>



---
**Discord Server:** <a href="https://discord.gg/EmwfaGuBE8" target="_blank">https://discord.gg/EmwfaGuBE8</a>

**Source Code:** <a href="https://github.com/ZaikoARG/TokenGuard" target="_blank">https://github.com/ZaikoARG/TokenGuard</a>

---

TokenGuard is a program written in Python that aims to mitigate almost 100% the theft of Discord Tokens on your computer.

The main features are:
* **Simple GUI:** TokenGuard has a graphic interface that is too simple, not very invasive and easy to use, which aims to adapt to all types of users.
* **Constant Protection:** The program is in charge of cleaning the traces of the Discord Token constantly, guaranteeing its safety at all times.
* **Low Consumption:** Despite the fact that it is constantly running, the consumption of both the CPU and RAM is very low..

---

## Installation

**Download:** <a href="https://github.com/ZaikoARG/TokenGuard/releases" target="_blank">https://github.com/ZaikoARG/TokenGuard/releases</a>

TokenGuard has a simple, multi-language installer for easy installation.

![Screenshot_6](https://user-images.githubusercontent.com/67133061/145714596-6ee8873a-8248-4254-89c4-36ebf6589fa0.png)

---

## Usage

The interface is very simple, it has a Toggle to turn the protection on and off.

The moment you activate the Toggle, the protection will start to work. And when I deactivate it it will stop working.

When you open the program, an icon will be created in the hidden icon bar. This in order to be able to control the program when it is sent to the background

![Screenshot_8](https://user-images.githubusercontent.com/67133061/145714794-a4050ef4-8404-4322-9577-87e8fabb3352.png)

### Important Things About Usage

* You should keep in mind that when you activate the protection, discord must be open and logged in.
* In the event that Discord is not open, the program will wait for you to open it.
* Just leave the Toggle on if you want and open it to start protection.
* If the Discord process is closed, the program will report an error and only the protection will be disabled. Turn it back on and open the Discord process.
* Minimizing the application will automatically send it to the background. To reactivate it, use the open option of the hidden icon at the bottom right of the screen.
* For added protection, I highly recommend deleting saved Discord sessions in your Browser.
* When using TokenGuard, you will notice that when you reopen Discord, it will ask you to log in again. This is because my program deletes the databases where discord stores the Login Token

---

## For Developers

### How TokenGuard Works

TokenGuard works by trying to clean the absurd and excessive traces of the Token that Discord leaves on your system.
This includes Tokens stored in Files, as well as those stored in Memory.

I did this protection scheme based mainly on the operation of Token Stealer Malwares.

My program will take care of cleaning up the Discord LDB files.
After this, a loop will begin that will erase the memory addresses that contain the User Token every 5 seconds.

### TokenGuard Operation Scheme
![Concept Map (2)](https://user-images.githubusercontent.com/67133061/145716514-c9f04fc0-f4fa-4e97-870a-5827baacfd3a.jpg)

### About the Code
I made the TokenGuard code as organized as possible, dividing the workflow into several files.

- **files.py:** LDB Files Cleanup
- **logs.py:** Log Saving
- **memory.py:** Classes and Functions for Reading and Writing Memory
- **py_toggle.py:** Toggle Button for the GUI
- **shared_variables.py:** Definition of Shared Variables
- **systrayicon.py:** Systray Icon Classes and Functions
- **TokenGuard.py:** Main Program
- **tokenprotection.py:** Token Protection Initialization


I tried to add a good amount of annotations so that whoever wants to use parts of the code can understand how each part works.

```py
if "__main__" == __name__:
    # Define SysTrayIcon Thread
    st = systrayicon.SysTrayIcon()
    # Initialize SysTrayIcon
    st.start()
    # Define the App
    app = QApplication(sys.argv)
    # Define the MainWindow
    window = MainWindow()
    # Start App
    sys.exit(app.exec())
```

I want to clarify that the code was totally made by me and that it possibly contains certain parts where it looks ugly or maybe it could have been done better.

In any case, the tool will have more updates in which I will try to correct the problems that appear.

In the event that you find a bug or any type of bug or code fix, please let me know on my Discord Server.

# Gratitude
I want to thank my colleague and friend Mr20 for helping me with the designs, giving me moral support and accompanying me all the way to develop the tool.

# License
This project is licensed under the terms of the MIT license.

# ☕ Buy me a Coffee

If you wish you can support my work by inviting me for a coffee.

With this you will be motivating me to improve this project and to create new projects.

**Buy me a Coffee:** <a href="https://www.buymeacoffee.com/ZaikoARG" target="_blank">https://www.buymeacoffee.com/ZaikoARG</a>
