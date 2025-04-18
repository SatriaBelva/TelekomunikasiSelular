import geopandas as gpd

def get_map_path() :
    return gpd.read_file(r"C:\Magang Grapari\Magang\streamlit\data\JemberSHP\ADMINISTRASIDESA_AR_25K.shp")

def get_kecamatan_list() :
    return sorted(get_map_path()['WADMKC'].unique())
