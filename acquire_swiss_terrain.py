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
        resolution: (float): resolution of original xyz-file. Attention: In order to maintain 

    Returns:
        vertices (numpy.ndarray): terrain vertices array with shape: (number of points, 3)
        triangles (numpy.ndarray): terrain triangles array with shape: (number of vertices, 3)

    '''

    num_lines = sum(1 for _ in open(file_path + file_name))

    xyz = open(file_path + file_name)

    line = xyz.readline()
    vertices = np.array([[0,0,0]])
    for n in range(num_lines-1):
        line = xyz.readline()
        x = float(line.split()[0])
        y = float(line.split()[1])
        z = float(line.split()[2])
        if x > start_west and x < (start_west + map_size_x) and y > start_south and y < (start_south + map_size_y):
            vertices = np.append(vertices,np.array([[np.floor((x-start_west)/resolution),np.floor((y-start_south)/resolution),z/resolution]]),axis=0)

    vertices = np.delete(vertices,0,axis=0)
    
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