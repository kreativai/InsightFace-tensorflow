from setuptools import setup, find_packages

setup(name='InsightFace-tensorflow',
      version='1.0',
      description='InsightFace-tensorflow',
      url='https://github.com/kreativai/InsightFace-tensorflow',
      author='',
      author_email='',
      license='',
      package_dir={'insightface': ''},
      packages=[
        'insightface',
        'insightface.backbones'
      ],
      zip_safe=False)
