# swiss_terrain_mesh
Simple functions to acquire vertices/triangles/open3d-mesh from Swiss terrain xyz-file


Demo: getting vertices/triangles/open3d-mesh of ETH-HG building
  1. Download xyz-file: https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2018_2683-1247/swisssurface3d-raster_2018_2683-1247_0.5_2056_5728.xyz.zip
  2. For getting vertices and triangles:
        vertices,triangles = acquire_swiss_terrain.loading_swiss_terrain(
           file_path=(the relative path of downloaded xyz-file above),
           file_name='swissSURFACE3D_Raster_0.5_xyz_CHLV95_LN02_2683_1247.xyz',
           start_west=2683650,
           start_south=1247800,
           map_size_x=100,
           map_size_y=100,
           resolution=0.5
         )
  4. For getting open3d triangle mesh: terrain_o3d_mesh = acquire_swiss_terrain.get_o3d_mesh_from_v_and_t(vertices,triangles)
