
APIKEY = "AIzaSyDA4yWXAXzJyN7kckJWZmCX2vxsFqpttss"
DEFAULT_IMAGE_LENGTH = 600
DEFAULT_IMAGE_HEIGHT = 600
DEFAULT_ZOOM = 18
DEFAULT_LATITUDE = 0
DEFAULT_LONGITUDE = 0
DEFAULT_SCALE = 0


class GoogleMapsPath:

    def __init__(self,color="0x0000ff",weight=5):
        self.color = color
        self.weight = weight
        self.coordinates = []
        self.visible = False

        #TODO Fillcolor,geodesic,encoded polylines, etc.

    def add_to_path(self,lat,long):
        self.coordinates.append([lat,long])
        # self.coordinates.append(str(lat)+","+str(long))
        # print("Adding to path")
        # print(self.coordinates)

    def get_path(self):
        path_str = ""
        for coord in self.coordinates:
            path_str = path_str + "|"+str(coord[0]) + "," + str(coord[1])
        # print(path_str)
        return path_str

    def get_path_str(self):
        str = ""
        if self.visible == True:
            str = "&path=color:" + str(path.color) \
                  + "|weight:" + str(path.weight)  \
                  + self.get_path()

        return str


class GoogleMapsMarker:

    def __init__(self):
        self.visible = False
        self.color = []
        self.label = []
        self.label_position = [] # Can be in string "latitude,longitude" format or a valid Address string
        self.size = []

        # TODO Custom Icons

    def add_marker(self,label_position,color="blue",label="A",size=""):
        self.label_position.append(label_position)
        self.color.append(color)
        self.label.append(label)
        self.size.append(size)
        self.visible = True #Automatically Make the markers visible


    def get_marker_str(self):
        str = ""
        if self.visible==True:
            for i in range(len(color)):
                str += "&markers="

                if not self.size[i]=="":
                    str += "size:" + self.size[i] + "&7C"

                str += "color:" + self.color[i]\
                       + "%7C" + "label:" + self.label[i]\
                       + "%7C" + self.label_position[i]
        return str


class GoogleMapAPI:

    def __init__(self,api_key = APIKEY,latitude=DEFAULT_LATITUDE,longitude=DEFAULT_LONGITUDE,zoom=DEFAULT_ZOOM,iLength=DEFAULT_IMAGE_LENGTH,iHeight=DEFAULT_IMAGE_HEIGHT,scale=DEFAULT_SCALE,format="png",map_type="hybrid",path=GoogleMapsPath):
        self.latitude = latitude
        self.longitude = longitude
        self.zoom = zoom
        self.iLength = iLength
        self.iHeight = iHeight
        self.scale = scale
        self.format = format
        self.map_type = map_type
        self.marker = GoogleMapsMarker()
        self.api_key = api_key
        self.path = path
        self.BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

    def get_url(self):
        url = self.BASE_URL
        url += "center=" + str(self.latitude)+","+str(self.longitude)\
              + "&zoom=" + str(self.zoom)\
              + "&size=" + str(self.iLength) + "x" + str(self.iHeight)\
              + "&maptype="+ str(self.map_type)\
              + self.marker.get_marker_str()\
              + "&key=" + str(self.api_key)
        return url


