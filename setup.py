from setuptools import setup


setup(
    name='notify engine',
    version='0.0.1',
    author='klolik',
    author_email='klolik@ya.ru',
    description=('Notify engine'),
    long_description=('Notify engine'),
    license='BSD',
    url='https://github.com/kloliks/notify_engine',
    packages=[
        'notify_engine',
        'notify_engine/eventloop', 'notify_engine/notify_manager',
    ],
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Topic :: Utilities',
        'License :: BSD License',
    ],
)
