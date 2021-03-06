Instructions for compiling CASTEP 19.11 for ARCHER2 using GCC compilers
=========================================================================

These instructions are for compiling CASTEP 19.11 on [ARCHER2](https://www.archer2.ac.uk)
using the GCC compilers. ARCHER2 is an HPE Cray EX supercomputer with two AMD 7742 64-core
processors per node and the HPE Cray Slingshot interconnect.

We assume that you have obtained the CASTEP source code from the UKCP developers.

Unpack the CASTEP source code
-----------------------------

Unpack the source

```bash
tar -xvf CASTEP-19.11.tar.gz 
```

Setup correct modules
---------------------

Setup the GCC compilers and load the FFTW library module:

```bash
module restore PrgEnv-gnu
module swap gcc gcc/9.3.0
module load cray-fftw
```

Edit the Makefile to set options
--------------------------------

Switch to the main CASTEP directory

```bash
cd CASTEP-19.11
```

Edit `Makefile` and set the following options

```
COMMS_ARCH := mpi
FFT := fftw3
BUILD := fast
MATHLIBS := scilib
```

Edit the arch build options to remove static
--------------------------------------------

ARCHER2 does not currently support building applications statically so the option
to set this must be removed from the `obj/platforms/linux_x86_64_gfortran9.0-XT.mk`
file. Open the file in an editor and remove the `-static` flag from the `LD_FLAGS`
variable. After modification, it should look like:

```
LD_FLAGS = $(OPT) -fopenmp
```

Build CASTEP
------------

Build CASTEP using the following commands:

```bash
unset CPU
CC=cc CASTEP_ARCH=linux_x86_64_gfortran9.0-XT make -j8  clean
CC=cc CASTEP_ARCH=linux_x86_64_gfortran9.0-XT make -j8
```

The install process will ask for the path to the BLAS and LAPACK libraries - just
leave this blank as the compiler wrapper scripts automatically deal with this.

You will also be asked for the path to FFTW; just leave this blank as the compiler 
wrapper scripts automatically deal with this.

Install CASTEP
--------------

To install the binaries in a specified directory use:

```bash
make -j8 INSTALL_DIR=/work/t01/t01/auser/software/CASTEP/19.11-gcc/bin install
```

If you wish to simply install into the `bin/` directory in the CASTEP source
tree you can simply use:

```bash
make -j8 install
```

The built binary is called `castep.mpi`.
