from distutils.core import setup
setup(
  name = 'rangev2',         
  packages = ['rangev2'],  
  version = '0.1.1',      
  license='MIT',        
  description = 'A new version of python range',   
  long_description='rangev2 is next version of popular range class of python, which enables you to produce lists even by using *,/,// and % operators along with +,- operators'+
  '\n The syntax is nearly similar to the privious versions'+
  '\nLittle modification is that step (third parametr) is now string containing operand and operator'+
  "\nnew_range(8,100,'*9')"+
'\n[8,72]'+
  '\nprint(new_range(begin,end,step)) will now print the entire list'+
  '\nexample'+ 
"\nprint(new_range(100,1,'//3')"+
"\n[100, 33, 11, 3]"+
   '\nthe list generated can also be accessed via list argument'+ 
  '\nexample : new_range(6).list[0,1,2,3,4,5]',
  author = 'Ishan Gambhir',                   
  author_email = 'ishugambhir2001@gmail.com',      
  url = 'https://github.com/co18326/rangev2',   
  download_url = 'https://github.com/CO18326/rangev2/archive/V_0.1.1.tar.gz',    
  keywords = ['range', 'latest', 'beginer','library','gp','agp'],  
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
