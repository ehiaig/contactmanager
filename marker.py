class Marker:
    def __init__(self, color='Red'):
        self.color = color

class MarkerBox:
    def __init__(self, markers=[]):
        self.markers = markers

    def add_marker(self, marker):
        self.markers.append(marker)

    def remove_marker(self, color):
        for marker in self.markers:
            if marker.color == color:
                self.markers.remove(marker)
                return marker
        return None

    """The line below shows the number of markers remaining and their colors"""

    def counter(self):
        print("Number of markers: ")
        print(len(self.markers))
        for col in self.markers:
            print(col.color)

if __name__ == "__main__": #The code below this line is the first to be called when this program runs. So it makes it easy in a case where your program is going to imported as a module.
    mest_markers = MarkerBox()
    mest_markers.add_marker(Marker(color="blue"))
    mest_markers.add_marker(Marker(color="black"))
    mest_markers.add_marker(Marker(color="green"))
    mest_markers.remove_marker("blue")
    mest_markers.counter()


string = "Hello There"
print(string[0:3])
print(string[:2])

a = range(1,10)
print(a)

def f():
    global s
    print(s)
    s = 'Andrew andrew'
    print(s)

