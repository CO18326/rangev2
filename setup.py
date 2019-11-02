from distutils.core import setup
setup(
  name = 'rangev2',         
  packages = ['rangev2'],  
  version = '0.1',      
  license='MIT',        
  description = 'A new version of python range',   
  author = 'Ishan Gambhir',                   
  author_email = 'ishugambhir2001@gmail.com',      
  url = 'https://github.com/co18326/rangev2',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['range', 'latest', 'beginer','library','gp','agp'],  
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
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
