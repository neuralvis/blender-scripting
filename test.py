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

if __name__ == "__main__":
    response = synchronous_fetch("http://httpbin.org/get") 
    print(response)

    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "test"
    bpy.ops.render.render(animation=False, write_still=True)

    while True:
       break
    
