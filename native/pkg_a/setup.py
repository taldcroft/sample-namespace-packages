# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup


setup(
    name='example_pkg_a',

    version='1.3',

    description='',
    long_description='',

    author='Jon Wayne Parrott',
    author_email='jonwayne@google.com',

    license='Apache Software License',

    packages=['example_pkg_a', 'example_pkg.a'],
    package_dir={'example_pkg.a': 'example_pkg_a', 'example_pkg_a': 'example_pkg_a'},
    zip_safe=False,
)
