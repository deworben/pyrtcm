from setuptools import setup, find_packages
import version
setup(name='pyrtcm',
      version=version.get_git_version(),
      description='Pyubx2',
      url='https://github.com/deworben/pyrtcm.git',
      author='Benjamin De Worsop',
      author_email='ben@swoop.aero',
      license='MIT',
      packages=find_packages(),
      package_data={},
      # Actually requires companionCode install_requires=["flight-controller-sim==4.1.80", "MAVProxy==3.9.0", "aircraft-communication==1.0.24"],
      include_package_data=True,  # include files specified in MANIFEST.in
      zip_safe=False)
