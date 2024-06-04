import numpy as np
from matplotlib.tri import Triangulation
import open3d as o3d

def loading_swiss_terrain(
        file_path: str,
        file_name: str,
        start_west: int,
        start_south: int,
        map_size_x: int,
        map_size_y: int,
        resolution: float,
):
    '''
    Function to load swiss terrain data from local xyz-file.

    Args:
        file_path (str): relative path of xyz-file
        file_name: (str): name of xyz-file
        start_west: (int): x-coordinate of west edge (about coordinate definition: Download site -> Selection by rectangle -> Rectangle coordinates)
        start_south: (int): y-coordinate of south edge (about coordinate definition: Download site -> Selection by rectangle -> Rectangle coordinates)
        map_size_x: (int): x-length of terrain rectangle 
        map_size_y: (int): y-length of terrain rectangle
        resolution (int): resolution of the downloaded terrain file (0.5 or 2.0)

    Returns:
        vertices (numpy.ndarray): terrain vertices array with shape: (number of points, 3)
        triangles (numpy.ndarray): terrain triangles array with shape: (number of vertices, 3)

    '''

    vertices_raw = np.loadtxt(file_path + file_name, skiprows=1)

    in_range_x = (vertices_raw[:,0]>start_west) & (vertices_raw[:,0]<(start_west+map_size_x))
    in_range_y = (vertices_raw[:,1]>start_south) & (vertices_raw[:,1]<(start_south+map_size_y))
    in_range = in_range_x & in_range_y

    vertices = vertices_raw[in_range,:]
    vertices[:,0] -= start_west
    vertices[:,1] -= start_south

    if resolution == 0.5:
        vertices[:,:2] -= 0.25
    
    tri = Triangulation(vertices[:,0],vertices[:,1])
    triangles = tri.triangles

    return vertices,triangles

def get_o3d_mesh_from_v_and_t(
        vertices: np.array,
        triangles: np.array,
):
    '''
    Simple function to get open3d mesh from vertices and triangles

    Args:
        vertices (numpy.ndarray): terrain vertices
        triangles (numpy.ndarray): terrain traingles
    
    Returns:
        mesh_o3d (o3d.geometry.TriangleMesh): terrain mesh
    '''
    mesh_o3d = o3d.geometry.TriangleMesh()
    mesh_o3d.vertices = o3d.utility.Vector3dVector(vertices)
    mesh_o3d.triangles = o3d.utility.Vector3iVector(triangles)

    return mesh_o3d