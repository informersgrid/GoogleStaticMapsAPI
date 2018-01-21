# Enter your Google Static Maps API access key between the ""
APIKEY = ""
# Default Image Dimensions
DEFAULT_IMAGE_LENGTH = 600
DEFAULT_IMAGE_HEIGHT = 600
# Default Map Zoom
DEFAULT_ZOOM = 16
# Default Intitialization Latitude and Longitude
DEFAULT_LATITUDE = 0
DEFAULT_LONGITUDE = 0
# Default Image Scale
DEFAULT_SCALE = 0
DEFAULT_IMAGE_FORAMT = "png"
DEFAULT_MAP_TYPE = "hybrid"

# Google Map Path Class
class GoogleMapsPath:

    # Intitialize Path Parameters
    def __init__(self,color="0x0000ff",weight=5):
        # Path Color
        self.color = color
        # Path Weight (Thickness)
        self.weight = weight
        # Path Coordinates (Latitude,Longitude) List
        self.coordinates = []
        # Set Default Path Visibility to Off (False)
        self.visible = False

        #TODO Fillcolor,geodesic,encoded polylines, etc.

    # Append new coordinate to path coordinate list
    def add_to_path(self,lat,long):
        self.coordinates.append([lat,long])

    # Get List of path Coordinates
    def get_path_list(self):
        path_str = ""
        for coord in self.coordinates:
            path_str = path_str + "|"+str(self.coord[0]) + "," + str(self.coord[1])
        return path_str

    def get_path_str(self):
        formatted_str = ""
        if self.visible == True:
            formatted_str = "&path=color:" + str(self.color) \
                  + "|weight:" + str(self.weight)  \
                  + self.get_path_list()

        return formatted_str

# Google Maps Marker Class
class GoogleMapsMarker:
    
    # Initialise Marker Parameters
    def __init__(self,visible=False):
        # Set Default Marker Visibility to False
        self.visible = visible
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


class GoogleStaticMapAPI:
    # Intitialization of Class Members
    def __init__(self,api_key = APIKEY,latitude=DEFAULT_LATITUDE,longitude=DEFAULT_LONGITUDE,zoom=DEFAULT_ZOOM,iLength=DEFAULT_IMAGE_LENGTH,iHeight=DEFAULT_IMAGE_HEIGHT,scale=DEFAULT_SCALE,format=DEFAULT_IMAGE_FORMAT,map_type=DEFAULT_MAP_TYPE,path=GoogleMapsPath,marker=GoogleMapsMarker):
        # Central Coordinates (Latitude and Longitude)
        self.latitude = latitude
        self.longitude = longitude
        # Zoom Level
        self.zoom = zoom
        # Map Image Dimentions (Length x Height)
        self.iLength = iLength
        self.iHeight = iHeight
        # Map Image Scale Factor
        self.scale = scale
        # Map Image Format
        self.format = format
        # Map Type
        self.map_type = map_type
        # Google Maps Marker: an object of class GoogleMapsMarker
        self.marker = marker
        # Google Static Maps API Key
        self.api_key = api_key
        # Google Maps Path: an object of class GoogleMapsPath
        self.path = path
        # Base URL for Static Maps
        self.BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

    # Method that genterates and returns the Google Static Maps API URL
    def get_url(self):
        # Initialise the URL with the BASE_URL
        url = self.BASE_URL
        # Append other Map parametrs in the required format
        url += "center=" + str(self.latitude)+","+str(self.longitude)\
              + "&zoom=" + str(self.zoom)\
              + "&size=" + str(self.iLength) + "x" + str(self.iHeight)\
              + "&maptype="+ str(self.map_type)\
              + self.marker.get_marker_str()\
              + "&key=" + str(self.api_key)
        # Return generated URL
        return url


