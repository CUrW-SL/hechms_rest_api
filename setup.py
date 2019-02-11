from setuptools import setup, find_packages

setup(
    name='hechms_rest_api',
    version='1.0.0',
    packages=find_packages(),
    url='http://www.curwsl.org',
    license='',
    author='Hasitha',
    author_email='hasithadkr7@gmail.com',
    description='HecHms distributed version rest api',
    install_requires=['FLASK', 'Flask-Uploads', 'Flask-JSON', 'pandas'],
    zip_safe=True
)
