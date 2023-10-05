from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='db-converter',  # Kütüphane ismi
    version='0.1.0',  # Versiyon numarası
    packages=find_packages(),  # Dahil edilecek paketlerin listesi
    install_requires=[  # Gerekli bağımlılıklar
        'numpy',
        'pandas',
        'pymongo',
        'PyMySQL',
        'python-dateutil',
        'pytz',
        'six'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
