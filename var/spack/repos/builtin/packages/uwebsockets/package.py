# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install uwebsockets
#
# You can edit this file again by typing:
#
#     spack edit uwebsockets
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Uwebsockets(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/uNetworking/uWebSockets"
    url = "https://github.com/uNetworking/uWebSockets/archive/refs/tags/v20.74.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("ta7mid")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("Apache-2.0", checked_by="ta7mid")

    version("20.74.0", sha256="e1d9c99b8e87e78a9aaa89ca3ebaa450ef0ba22304d24978bb108777db73676c")
    version("20.73.0", sha256="44c18b752991d390f29a96067fc7fe682185fce87f725872de87c90e4bce07ef")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    depends_on("usockets")

    def edit(self, spec, prefix):
        makefile = FileFilter("GNUmakefile")
        buildc = FileFilter("build.c")
        usockets = self.spec["usockets"]

        makefile.filter(r"\$\(MAKE\) -C uSockets", "")
        buildc.filter("uSockets/src", usockets.prefix.include)
        buildc.filter(r"uSockets/\*.o", usockets.libs.joined(" "))
