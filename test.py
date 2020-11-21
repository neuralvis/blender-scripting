import sys
path_list = ['/mnt/lustre/msrinivasa/develop/blender-learn', '/mnt/lustre/msrinivasa/develop/blender-learn/env/lib/python37.zip',
             '/mnt/lustre/msrinivasa/develop/blender-learn/env/lib/python3.7', '/mnt/lustre/msrinivasa/develop/blender-learn/env/lib/python3.7/lib-dynload',
             '/mnt/lustre/msrinivasa/develop/blender-learn/env/lib/python3.7/site-packages']
ans = [sys.path.append(path) for path in path_list]



from tornado.httpclient import HTTPClient
import bpy

def synchronous_fetch(url):
   http_client = HTTPClient()
   response = http_client.fetch(url)
   return response.body

# to get the blender image as a numpy array
# we borrow a trick from here: https://ammous88.wordpress.com/2015/01/16/blender-access-render-results-pixels-directly-from-python-2/

if __name__ == "__main__":
    response = synchronous_fetch("http://httpbin.org/get") 
    print(response)

    # switch on nodes
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    links = tree.links

    # clear default nodes
    for n in tree.nodes:
        tree.nodes.remove(n)

    # create input render layer node
    rl = tree.nodes.new('CompositorNodeRLayers')      
    rl.location = 185,285

    # create output node
    v = tree.nodes.new('CompositorNodeViewer')   
    v.location = 750,210
    v.use_alpha = False

    # Links
    links.new(rl.outputs[0], v.inputs[0])  # link Image output to Viewer input

    # render
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "test"
    # bpy.ops.render.render(animation=False, write_still=False)
    bpy.ops.render.render()

    # get viewer pixels
    pixels = bpy.data.images['Viewer Node'].pixels
    # size is always width * height * 4 (rgba)
    print(f"The size of pixels in the buffer is: {len(pixels)}") 
