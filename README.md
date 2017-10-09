![Parqyng Lots](https://github.com/ColoradoSchoolOfMines/parqyng-lots/raw/master/assets/logo.png)
# Xilinx Hackathon Project

This is a hackathon project for tracking the number of cars in an arbitrary
number of parking lots with an arbitrary number of entrances.

View our video here: <https://youtu.be/qi9YZLhS0gk>

[![Video](https://github.com/ColoradoSchoolOfMines/parqyng-lots/raw/master/assets/video.png)](https://www.youtube.com/watch?v=qi9YZLhS0gk)

## Design
![System Diagram](https://github.com/ColoradoSchoolOfMines/parqyng-lots/raw/master/assets/system-diagram.png)

## Installation

### Car Detection Nodes
Open the `client/detector.ipynb` file in Jupyter Notebooks. Follow the
instructions for installing the hardware.

### Server
The server is written in Python using the [TurboGears](http://turbogears.com/)
framework.

1. Install the application and its dependencies:

        $ pip install -e . --user

2. If you do not have `gearbox` installed:

        $ pip install --user tg.devtools

3. Setup the application:

        $ cp development.ini.sample development.ini
        $ gearbox setup-app

4. Finally, serve the application:

        $ gearbox serve --reload --debug

### Server Displays
Open the `client/display_server` file in Jupyter Notebooks. Follow the
instructions for installation of the hardware.

## Hackers
- [Daichi Jameson](https://github.com/daichij)
- [Jack Rosenthal](https://github.com/jackrosenthal)
- [Sam Sartor](https://github.com/samsartor)
- [Sumner Evans](https://github.com/sumnerevans)

## License
This repository is licensed under the MIT License (see LICENSE file).
