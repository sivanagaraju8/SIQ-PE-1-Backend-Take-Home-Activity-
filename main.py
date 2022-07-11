class ParkingLot:
    def __init__(self, vehicle_number, driver_age, slot_number):
        self.vehicle_number = vehicle_number
        self.driver_age = driver_age
        self.slot_number = slot_number


fileOut = open("output.txt", 'w')

parking_lots_list = []
slot_number = 0
number_of_slots_created = 0
slots_available = []


def print_command(cmd):
    print(cmd)


def write_line(line):
    fileOut.write(str(line) + '\n')


def create_parking_lot(command):
    global number_of_slots_created
    global slots_available
    number_of_slots_created = int(command[1])
    slots_available = [x for x in range(1, number_of_slots_created + 1, 1)]
    write_line(f"Created parking of {number_of_slots_created} slots")


def park(command):
    global slot_number
    if len(slots_available) > 0:
        slot_number = slots_available[0]
        lot = ParkingLot(command[1], command[3], slot_number)
        parking_lots_list.append(lot)
        slots_available.remove(slot_number)
        write_line(
            "Car with vehicle registration number {} has been parked at slot number {}"
            .format(command[1], lot.slot_number))
    else:
        write_line(
            "No more parking spaces are available to allocate a parking lot.")


def slot_numbers_for_driver_of_age(command):
    slot_numbers = []
    for lot in parking_lots_list:
        if lot.driver_age == command[1]:
            slot_numbers.append(str(lot.slot_number))
    if len(slot_numbers) > 0:
        write_line(",".join(slot_numbers))


def slot_number_for_car_with_number(command):
    slot_numbers = []
    for lot in parking_lots_list:
        if lot.vehicle_number == command[1]:
            slot_numbers.append(str(lot.slot_number))
    if len(slot_numbers) > 0:
        write_line(",".join(slot_numbers))


def add_slot_to_list(slot_number):
    global slots_available
    index = len(slots_available)
    for i in range(len(slots_available)):
        if slots_available[i] > slot_number:
            index = i
            break
    if index == len(slots_available):
        slots_available = slots_available[:index] + [slot_number]
    else:
        slots_available = slots_available[:index] + [
            slot_number
        ] + slots_available[index:]


def leave(command):
    for lot in parking_lots_list:
        if lot.slot_number == int(command[1]):
            write_line(
                "Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of "
                "the car was of age {}".format(lot.slot_number,
                                               lot.vehicle_number,
                                               lot.driver_age))
            add_slot_to_list(lot.slot_number)
            parking_lots_list.remove(lot)
            break


def vehicle_registration_number_for_driver_of_age(command):
    vehicle_numbers = []
    for lot in parking_lots_list:
        if lot.driver_age == command[1]:
            vehicle_numbers.append(lot.slot_number)
    if len(vehicle_numbers) > 0:
        write_line(",".join(vehicle_numbers))


def extractCommand(line):
    line = line.strip()
    command = line.split(" ")
    globals()[command[0].lower()](command)


fileIn = open('input.txt', 'r+')
count = 0
while True:
    line = fileIn.readline()
    if not line:
        break
    if line == '\n' or line == 'r\n':
        continue
    try:
        extractCommand(line)
    except:
        write_line(f"Couldn't able to proces this statement: {line}")
        continue

fileIn.close()
fileOut.close()
