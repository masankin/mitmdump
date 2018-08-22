#!/usr/bin/mitmdump -s
 
from __future__ import print_function
 
import os
from urlparse import urlsplit 
#from libmproxy.protocol.http import decoded
from mitmproxy.models import decoded


def response(flow):
  #print(flow.response.headers['Content-Type'])
  with decoded(flow.response):
    ctype = flow.response.headers['Content-Type'];
    if ctype.startswith('image/'):
      #print(flow.response.headers['Content-Type'])
      url = urlsplit(flow.request.url)
      name = os.path.basename(url.path)
      outfile=''
      #print('==>>',url,name)
      path_arr = url.path.split('/');
      path_arr.pop();
      print('/'.join(path_arr))
      outfile = ('/Users/xxxx/Desktop/www/'.join(path_arr)+'/')  
      if not os.path.exists(outfile):
         os.makedirs(outfile)
      outfile = outfile + name;
      with open(outfile, 'wb') as f:
        f.write(flow.response.content)
        f.close()
      print(outfile, ' written')
    if (ctype.startswith('text/') or ctype.startswith('application/')):
      #print(flow.response.headers['Content-Type'])
      url = urlsplit(flow.request.url)
      name = os.path.basename(url.path)
      outfile=''
      path_arr = url.path.split('/');
      path_arr.pop();
      print('/'.join(path_arr))
      outfile = ('/Users/xxxx/Desktop/www/'.join(path_arr)+'/')  
      if not os.path.exists(outfile):
         #print('zy==>>',outfile) 
         os.makedirs(outfile)
      outfile = outfile + name;
      with open(outfile, 'wb') as f:
        f.write(flow.response.content)
        f.close()
      print(outfile, ' written')