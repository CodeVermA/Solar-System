from numpy import array
from solar_system import Planet, Sun, SolarSystem, SolarBody
import matplotlib.pyplot as plt
from math import sqrt
 
TIME_STEP = 0.001
solar_system = SolarSystem(TIME_STEP)

def add_bodies_to_solar_system():
    global sun

    planets_data = read_data("planet_details.txt")

    G_CONST_IDX = 0
    SUN_INFO_IDX = 1
    ORB_PRD_ALL_PLANETS_IDX = 2
    PLANETS_INFO_STRT_IDX = 3
    PLANETS_INFO_END_IDX = None
    SATELLITE_INFO_IDX = None
    EARTH_RAD_IDX = None

    SolarSystem.gravitational_const = eval(planets_data[G_CONST_IDX])
    sun = Sun(solar_system, eval(planets_data[SUN_INFO_IDX]))
    
    orbital_periods = [eval(period) for period in planets_data[ORB_PRD_ALL_PLANETS_IDX].split(",")]
    solar_system.save_orbital_periods(orbital_periods)

    for planet_data in planets_data[PLANETS_INFO_STRT_IDX:]:
            name, colour, mass, orbital_radius = planet_data.split(",")
            Planet(solar_system, name.strip(), eval(mass), colour.strip(), eval(orbital_radius))


def read_data(filename):
    planet_file = open(filename, "r")
    temp_planets_data = planet_file.readlines()
    planets_data = []

    for data in temp_planets_data:
        if (data[0] != '#' and data.strip() != ""):
            planets_data.append(data)

    return planets_data


    planet_file.close()
def main():
    add_bodies_to_solar_system()
    NUM_OF_FRAMES = 100000

    solar_system.run_simulation(NUM_OF_FRAMES)

    solar_system.compare_orbital_periods()

    solar_system.plot_energies()

if __name__ == "__main__":
    main()