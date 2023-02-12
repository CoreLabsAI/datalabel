# from setuptools import setup

# setup(
#     name='datalabel',
#     version='0.1',
#     packages=['labeler', 'labeler/class_utils'],
#     author='TitanLabs',
#     author_email='product@titanlabs.co',
#     description='quickly and effortlessly edit your dataframes without having to write any code. Its intuitive interface makes it ideal for both experienced data professionals and those new to data editing.',
#     install_requires=['pandas', 'requests', 'fastapi', 'uvicorn'],
# )


from setuptools import setup, find_packages

setup(
    name='datalabel',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    author='TitanLabs',
    author_email='product@titanlabs.co',
    description='quickly and effortlessly edit your dataframes without having to write any code. Its intuitive interface makes it ideal for both experienced data professionals and those new to data editing.',
    install_requires=['pandas', 'requests', 'fastapi', 'uvicorn'],
)
