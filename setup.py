#!/usr/bin/env python

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Setup script for customization demo."""

from setuptools import setup

setup(
    name="weblate_customization",
    version="0.1",
    packages=["weblate_customization"],
    include_package_data=True,
    license="GPL-3.0-or-later",
    description="Weblate customization example",
    long_description="Weblate customization example",
    keywords="i18n l10n gettext git mercurial translate",
    url="https://weblate.org/",
    author="Michal Čihař",
    author_email="michal@cihar.com",
    install_requires=["Weblate"],
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
