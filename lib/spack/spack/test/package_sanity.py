##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
"""This test does sanity checks on Spack's builtin package database."""

import re

import pytest

import spack
from spack.repository import RepoPath


def check_db():
    """Get all packages in a DB to make sure they work."""
    for name in spack.repo.all_package_names():
        spack.repo.get(name)


@pytest.mark.maybeslow
def test_get_all_packages():
    """Get all packages once and make sure that works."""
    check_db()


def test_get_all_mock_packages():
    """Get the mock packages once each too."""
    db = RepoPath(spack.mock_packages_path)
    spack.repo.swap(db)
    check_db()
    spack.repo.swap(db)


def test_all_versions_are_lowercase():
    """Spack package names must be lowercase, and use `-` instead of `_`."""
    errors = []
    for name in spack.repo.all_package_names():
        if re.search(r'[_A-Z]', name):
            errors.append(name)

    assert len(errors) == 0
