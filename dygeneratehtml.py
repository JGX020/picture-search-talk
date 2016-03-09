#coding:utf-8
def replace():
    line=open('templates/space.html').read()
    str='<div class="hex grid-3 tertiary"><a href="{{hrefadd}}" title="播放类型"><div class="inner"><img src="../static/assets/img/hex-img-3@2x.png" width="140" height="77" alt="Info on Buffalo\'s Website dev process" /></div><div class="hex-1"><span class="after"></span></div><div class="hex-2"><span class="after"></span></div><span class="after"></span></a></div>'    
    fb=open('templates/space.html','w')
    fb.write(line[0:line.find('<div class="list-hex-grid list-inline-block clearfix">')+len('<div class="list-hex-grid list-inline-block clearfix">')+1]+str+line[line.find('<div class="list-hex-grid list-inline-block clearfix">')+len('<div class="list-hex-grid list-inline-block clearfix">')+1:len(line)+1])
    fb.close()
