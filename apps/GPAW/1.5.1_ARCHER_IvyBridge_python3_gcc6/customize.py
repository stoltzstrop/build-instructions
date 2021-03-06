"""User provided customizations.

Here one changes the default arguments for compiling _gpaw.so (serial)
and gpaw-python (parallel).

Here are all the lists that can be modified:

* libraries
* library_dirs
* include_dirs
* extra_link_args
* extra_compile_args
* runtime_library_dirs
* extra_objects
* define_macros
* mpi_libraries
* mpi_library_dirs
* mpi_include_dirs
* mpi_runtime_library_dirs
* mpi_define_macros

To override use the form:

    libraries = ['somelib', 'otherlib']

To append use the form

    libraries += ['somelib', 'otherlib']
"""

compiler = 'cc'
mpicompiler = 'cc'  # use None if you don't want to build gpaw-python
mpilinker = 'cc'
platform_id = ''
# O2 (rather than O3) is needed to make the xc/xc.py revTPSS test
# work.
extra_compile_args = ['-O2']

# ScaLAPACK
scalapack = True
define_macros += [('GPAW_NO_UNDERSCORE_CBLACS', '1')]
define_macros += [('GPAW_NO_UNDERSCORE_CSCALAPACK', '1')]

# LibXC
xc = os.environ['LIBXC_DIR'] +'/'
include_dirs += [xc + 'include']
# Dynamic linking.  Use this if there is a libxc.so.
library_dirs += [xc + 'lib']
if 'xc' not in libraries:
    libraries.append('xc')
## Static linking.  Use this if there is only a libxc.a but the objects
## in the libxc library need to be compiled with -fPIC.
#extra_link_args += [xc + 'lib/libxc.a']
#if 'xc' in libraries:
#    libraries.remove('xc')

if 'blas' in libraries:
    libraries.remove('blas')
if 'lapack' in libraries:
    libraries.remove('lapack')
