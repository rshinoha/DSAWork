# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Project exercise P-2.35
# Ryoh Shinohara
# =======================================================================================
# Write a set of Python classes that can simulate an Internet application in which one
# party, Alice, is periodically creating a set of packets that she wants to send to Bob.
# An Internet process is continually checking if Alice has any packets to send, and if
# so, it delivers them to Bob’s computer, and Bob is periodically checking if his
# computer has a packet from Alice, and, if so, he reads and deletes it.

from random import randrange
from time import time, sleep

class Maker():
    """A class that makes and stores packets"""
    def __init__(self, packets=None):
        """Creates a Maker object"""
        if packets is None:
            self._packets = []
        else:
            if isinstance(packets, list):
                self._packets = packets
            else:
                self._packets = []
                self._packets.append(packets)
    
    def get_packets(self):
        """Gets packets"""
        return self._packets

    def set_packet(self, packet):
        """Adds a packet to the list of packets"""
        if not isinstance(packet, list):
            self._packets.append(packet)
        elif len(packet) != 0:
            for i in packet:
                self._packets.append(i)

    def delete_packets(self, num):
        """Deletes num number of packets from the start of the packet list"""
        for i in range(num):
            del self._packets[0]

class Processor():
    """
    A class that checks the Maker object and sends its packets to a
    Checker object
    """
    def __init__(self, last_time, check_time=10):
        """
        Creates a Processor object
        * last_time = last time packets were checked
        * check_time = how often Processor checks the Maker object (seconds)
        """
        if isinstance(last_time, float):
            self._last_time = last_time
        else:
            raise TypeError('last_time must be in float')
        if isinstance(check_time, int):
            self._check_time = check_time
        else:
            raise TypeError('check_time must be an integer')
    
    def get_last_time(self):
        """Returns last_time"""
        return self._last_time

    def check_packets(self, cur_time, maker, checker):
        """
        Given a Maker object and a current time, cur_time, checks if there are
        any packets only if appropriate time has passed since the last time
        the Processor checked the Maker's packets. If there are packets, it
        sends the packets to the Checker object and deletes the Makers's
        packets as well as returning True. Else, it returns False.
        """
        if cur_time - self._last_time > self._check_time:
            self._set_last_time(cur_time)
            temp_packets = maker.get_packets()
            if len(temp_packets) > 0:
                checker.set_packet(temp_packets)
                maker.delete_packets(len(temp_packets))
                return True
        return False

    def _set_last_time(self, cur_time):
        """Updates the last time packets were checked"""
        self._last_time = cur_time

class Checker(Maker):
    """An object of Checker class"""

    def __init__(self, last_time, check_time=10, read_time=10, packets=None):
        """Creates a Checker class object"""
        super().__init__(packets)
        if isinstance(last_time, float):
            self._last_time = last_time
        else:
            raise TypeError('last_time must be in float')
        if isinstance(check_time, int):
            self._check_time = check_time
        else:
            raise TypeError('check_time must be an integer')
        if isinstance(read_time, int):
            self._read_time = read_time
        else:
            raise TypeError('read_time must be an integer')

    def get_last_time(self):
        """Returns last_time"""
        return self._last_time
    
    def _set_last_time(self, cur_time):
        """Updates the last time packets were checked"""
        self._last_time = cur_time

    def check_packets(self, cur_time):
        """
        If the current time, cur_time, is past the minimum time required
        between the checks, calls the read_packets method.
        """
        if cur_time - self._last_time > self._check_time:
            self._read_packets(cur_time)

    def _read_packets(self, cur_time):
        """Simulates a person reading and deleting packets"""
        if not isinstance(self._packets, list):
            self._set_last_time(cur_time + self._read_time)
        else:
            self._set_last_time(cur_time + len(self._packets) * self._read_time)
        self.delete_packets(len(self._packets))

def generate_packets():
    """Creates random number of packets"""
    num_packets = randrange(10)
    temp_packets = []
    for i in range(num_packets):
        temp_packets.append(randrange(1000))
    return temp_packets

def simulate_packets(maker, processor, checker, max_time):
    """Simulates packet tranfers"""
    start_time = time()
    while time() < max_time + start_time:
        temp_packets = generate_packets()
        maker.set_packet(temp_packets)
        processor.check_packets(time(), maker, checker)
        checker.check_packets(time())
        print("Alice's packets: {}".format(Alice.get_packets()))
        print("Bob's packets: {}".format(Bob.get_packets()))
        sleep(randrange(10))


if __name__ == "__main__":
    start = time()
    Alice = Maker()
    Internet = Processor(start, 3)
    Bob = Checker(start, 10, 1)
    simulate_packets(Alice, Internet, Bob, 60)