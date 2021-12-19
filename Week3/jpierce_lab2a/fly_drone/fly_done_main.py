from jpierce_lab2a.fly_drone.Drone import Drone


def fly(Drone):
    Drone.toString()
    userinput = str(input(""""Enter '1' to accelerate| '2' to decelerate| '3' to ascend| '4' to descend| or '0' to land"  """)).lower()
    if userinput == "1":
        Drone.accelerate()
        fly(Drone)
    elif userinput == "2":
        Drone.decelerate()
        fly(Drone)
    elif userinput == "3":
        Drone.ascend()
        fly(Drone)
    elif userinput == "4":
        Drone.decend()
        fly(Drone)
    elif userinput == "0":
        print("Landing Successful")
    else:
        print("That option is invalid")
        fly(Drone)


def main():
    drone = Drone()
    fly(drone)


if __name__ == "__main__":
    main()
