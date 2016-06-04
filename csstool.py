import re
import PIL.Image as Image

def css_parse_spec(file_path):
    f = open(file_path)
    context = f.read()
    csses = re.findall('\..*?\{.*?\}',context)
    values = []
    for css in csses:
        css = css.replace(':',';').replace('{',';').replace('}',';')
        cssl = css.split(';')
        try:
            cssg = {
                'id':cssl[0][1:],
                'width':cssl[2][:-2],
                'x':cssl[4].split(' ')[0][:-2],
                'y':cssl[4].split(' ')[1][:-2]
            }
            values.append(cssg)
        except:
            print cssl
    #print cssg
    return values

def cut_images(file_path,csses,height=16):
    image = Image.open(file_path)
    pixels = image.load()
    for css in csses:
        x = -int(css['x'])
        y = -int(css['y'])
        width = int(css['width'])
        filename = css['id']
        new_image = Image.new('RGB',(width,height),(255,255,255))
        new_pixels = new_image.load()
        for x_ in range(x,x+width):
            for y_ in range(y,y+height):
                new_pixels[x_-x,y_-y] = pixels[x_,y_]
        new_image.save(filename+'.png')
