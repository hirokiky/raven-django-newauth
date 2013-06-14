from setuptools import setup, find_packages


setup(
    name='raven-django-newauth',
    version='0.0.1',
    description='Sentry client for django application using django-newauth.',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/raven-django-newauth/',
    license='MIT License',
    classifiers=[
      'Development Status :: 1 - Planning',
      'Environment :: Plugins',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['raven'],
    packages=find_packages(),
)
