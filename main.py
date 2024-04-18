import pandas 
import geopandas
import requests
import folium


Client_Token = "MLY|25204399145874923|91edfe348b19b66200b3119e41b28487"

class Mapilary:
    def __init__(self, access_toekn, client_id, authorization_url = None):
        self._access_token = access_toekn
        self._client_id = client_id
        self._authorization_url = authorization_url
    
    def set_access_token(access_token):
        _access_token = access_token
    
    def get_vector_tiles(self, z, x, y):
        pass

    def get_image_in_bbox(self, bbox, **filters):
        pass

    def get_image_from_key(self, image_id):
        pass

    def create_map(self, location):
        pass


