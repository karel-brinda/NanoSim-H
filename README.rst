NanoSim-H
=========

.. image:: https://travis-ci.org/karel-brinda/NanoSim-H.svg?branch=master
	:target: https://travis-ci.org/karel-brinda/NanoSim-H

.. image:: https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat-square
	:target: https://anaconda.org/bioconda/nanosim-h

.. image:: https://badge.fury.io/py/NanoSim-H.svg
	:target: https://badge.fury.io/py/NanoSim-H


About
-----

NanoSim-H is a simulator of Oxford Nanopore reads that captures the technology-specific features of ONT data,
and allows for adjustments upon improvement of Nanopore sequencing technology.
NanoSim-H has been derived from `NanoSim <https://github.com/bcgsc/NanoSim>`_,
a software package developed by Chen Yang at `Canada's Michael Smith Genome Sciences Centre <http://www.bcgsc.ca/>`_.
The fork was created from version 1.0.1 and the versions of NanoSim-H and NanoSim are kept synchronized.

NanoSim-H is implemented using Python uses R for model fitting.
In silico reads can be simulated from a given reference genome using ``nanosim-h``.
The NanoSim-H package is distributed with several precomputed error profiles, but
additional profiles can be computed using the ``nanosim-h-train``.

The main improvements compared to NanoSim are:

* Support for Python 3
* Support for `RNF <https://www.ncbi.nlm.nih.gov/pubmed/26353839>`_ read names
* Installation from `PyPI <https://pypi.python.org/pypi/NanoSim-H/>`_
* Error profiles distributed with the main package
* Automatic testing using `Travis <https://travis-ci.org/karel-brinda/NanoSim-H>`_
* Reproducible simulations (setting a seed for PRG)
* Improved interface with new parameters (e.g., for merging all contigs) and a progress bar
* Several minor bugs fixed



Quick example
-------------

Simulation of 100 reads from an *E.coli genome*.

.. code-block:: bash

	pip install --upgrade nanosim-h
	curl "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nuccore&dopt=fasta&val=545778205&sendto=on" | \
		nanosim-h -n 100 -



Installation
------------

**From** `BioConda <https://bioconda.github.io/>`_ **(recommended):**


.. code-block:: bash

	conda config --add channels defaults
	conda config --add channels conda-forge
	conda config --add channels bioconda
	conda install -y nanosim-h

**From** `PyPI <https://pypi.python.org/pypi/NanoSim-H/>`_ **:**

.. code-block:: bash

	pip install --upgrade nanosim-h

**From Github:**

.. code-block:: bash

	git clone https://github.com/karel-brinda/nanosim-h
	cd nanosim-h
	pip install --upgrade .

or

.. code-block:: bash

	git clone https://github.com/karel-brinda/nanosim-h
	cd nanosim-h
	python setup.py install


**Dependencies:**

For read simulation:

* `Python <http://python.org>`_ (2.7, 3.2 - 3.6)
* `Numpy <http://www.numpy.org/>`_

For computing new error profiles:

* `LAST <http://last.cbrc.jp/>`_ (tested with version 847)
* `R <https://www.r-project.org/>`_

When installed using Bioconda, all NanoSim-H dependencies get installed automatically.
When installed using PIP, all dependencies for read simulation are installed automatically.


Read simulation
---------------

Simulation stage takes a reference genome and possibly a read profile as input, and outputs simulated reads in FASTA format.


.. command: nanosim-h --help

.. code-block::

	$ nanosim-h --help
	usage: nanosim-h [-h] [-v] [-p str] [-o str] [-n int] [-u float] [-m float]
	                 [-i float] [-d float] [-s int] [--circular] [--perfect]
	                 [--merge-contigs] [--rnf] [--rnf-add-cigar] [--max-len int]
	                 [--min-len int] [--kmer-bias int]
	                 <reference.fa>
	
	Program:  NanoSim-H - a simulator of Oxford Nanopore reads.
	Version:  1.1.0.4
	Authors:  Chen Yang <cheny@bcgsc.ca> - author of the original software package (NanoSim)
	          Karel Brinda <kbrinda@hsph.harvard.edu> - author of the NanoSim-H fork
	
	positional arguments:
	  <reference.fa>        reference genome (- for standard input)
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -p str, --profile str
	                        error profile - one of precomputed profiles
	                        ('ecoli_R7.3', 'ecoli_R7', 'ecoli_R9_1D',
	                        'ecoli_R9_2D', 'yeast', 'ecoli_UCSC1b') or own
	                        directory with an error profile [ecoli_R9_2D]
	  -o str, --out-pref str
	                        prefix of output file [simulated]
	  -n int, --number int  number of generated reads [10000]
	  -u float, --unalign-rate float
	                        rate of unaligned reads [detect from the error
	                        profile]
	  -m float, --mis-rate float
	                        mismatch rate (weight tuning) [1.0]
	  -i float, --ins-rate float
	                        insertion rate (weight tuning) [1.0]
	  -d float, --del-rate float
	                        deletion rate (weight tuning) [1.0]
	  -s int, --seed int    initial seed for the pseudorandom number generator (0
	                        for random) [42]
	  --circular            circular simulation (linear otherwise)
	  --perfect             output perfect reads, no mutations
	  --merge-contigs       merge contigs from the reference
	  --rnf                 use RNF format for read names
	  --rnf-add-cigar       add cigar to RNF names (not fully debugged, yet)
	  --max-len int         maximum read length [inf]
	  --min-len int         minimum read length [50]
	  --kmer-bias int       prohibits homopolymers with length >= n bases in
	                        output reads [6]
	
	Examples: nanosim-h --circular ecoli_ref.fasta
	          nanosim-h --circular --perfect ecoli_ref.fasta
	          nanosim-h -p yeast --kmer-bias 0 yeast_ref.fasta
	
	Notice: the use of `max-len` and `min-len` will affect the read length distributions. If
	the range between `max-len` and `min-len` is too small, the program will run slowlier accordingly.
	

.. end


**Examples:**

1. If you want to simulate reads from *E. coli* genome, then circular mode should be used because it is a circular genome.

	``nanosim-h --circular Ecoli_ref.fasta``

2. If you want to simulate only perfect reads, i.e. no SNPs, or indels, just simulate the read length distribution.

	``nanosimh-h --circular --perfect Ecoli_ref.fasta``

3. If you want to simulate reads from a *S. cerevisiae* genome with no *k*-mer bias, then linear mode should be chosen because it is a linear genome.

	``nanosimh-h -p yeast --kmer-bias 0 yeast_ref.fasta``


**Output files:**

1. ``simulated.log`` – Log file for simulation process.

2. ``simulated.fa`` – FASTA file of simulated reads. Reads can contain information about how they were created either in RNF, or in the original NanoSim naming convention.

        **RNF naming convention**

        See the associated `RNF paper <https://www.ncbi.nlm.nih.gov/pubmed/26353839/>`_ and `RNF specification <http://karel-brinda.github.io/rnf-spec/>`_.

        **NanoSim naming convention**

	Each reads has "unaligned", "aligned", or "perfect" in the header determining their error rate. "unaligned" means that the reads have an error rate over 90% and cannot be aligned. "aligned" reads have the same error rate as training reads. "perfect" reads have no errors.

	To explain the information in the header, we have two examples:

	* ``>ref|NC-001137|-[chromosome=V]_468529_unaligned_0_F_0_3236_0``
		All information before the first ``_`` are chromosome information. ``468529`` is the start position and *unaligned* suggesting it should be unaligned to the reference. The first ``0`` is the sequence index. ``F`` represents a forward strand. ``0_3236_0`` means that sequence length extracted from the reference is 3236 bases.
	* ``>ref|NC-001143|-[chromosome=XI]_115406_aligned_16565_R_92_12710_2``
		This is an aligned read coming from chromosome XI at position 115406. ``16565`` is the sequence index. `R` represents a reverse complement strand. ``92_12710_2`` means that this read has 92-base head region (cannot be aligned), followed by 12710 bases of middle region, and then 2-base tail region.

	The information in the header can help users to locate the read easily.

3. ``simulated.errors.txt`` – List of introduced errors.

	The output contains error type, position, original bases and current bases.


Error profiles
--------------

Characterization stage takes a reference and a training read set in FASTA format as input. User can also provide their own alignment file in MAF format.


**Profiles distributed with NanoSim-H:**

* ``ecoli_R7``
* ``ecoli_R7.3``
* ``ecoli_R9_1D``
* ``ecoli_R9_2D`` (default error profile for read simulation)
* ``ecoli_UCSC1b``
* ``yeast``

**New error profiles:**

A new error profile can be obtained using the ``nanosim-h-train`` command.

.. command: nanosim-h-train --help

.. code-block::

	$ nanosim-h-train --help
	usage: nanosim-h-train [-h] [-v] [-i str] [-m str] [-b int] [--no-model-fit]
	                       <reference.fa> <profile.dir>
	
	Program:  NanoSim-H-Train - compute an error profile for NanoSim-H.
	Version:  1.1.0.4
	Authors:  Chen Yang <cheny@bcgsc.ca> - author of the original software package (NanoSim)
	          Karel Brinda <kbrinda@hsph.harvard.edu> - author of the NanoSim-H fork
	
	positional arguments:
	  <reference.fa>        reference genome of the training reads
	  <profile.dir>         error profile dir
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -i str, --infile str  training ONT real reads, must be fasta files
	  -m str, --maf str     user can provide their own alignment file, with maf
	                        extension
	  -b int, --num-bins int
	                        number of bins (for development) [20]
	  --no-model-fit        no model fitting
	

.. end

**Files associated with an error profile:**

1. ``aligned_length_ecdf`` – Length distribution of aligned regions on aligned reads.
2. ``aligned_reads_ecdf`` – Length distribution of aligned reads.
3. ``align_ratio`` – Empirical distribution of align ratio of each read.
4. ``besthit.maf`` – The best alignment of each read based on length.
5. ``match.hist``, ``mis.hist``, ``ins.hist``, ``del.hist`` – Histograms of matches, mismatches, insertions, and deletions.
6. ``first_match.hist`` – Histogram of the first match length of each alignment.
7. ``error_markov_model`` – Markov model of error types.
8. ``ht_ratio`` – Empirical distribution of the head region vs total unaligned region.
9. ``training.maf`` – The output of LAST, alignment file in MAF format.
10. ``match_markov_model`` – Markov model of the length of matches (stretches of correct base calls).
11. ``model_profile`` – Fitted model for errors.
12. ``processed.maf`` – A re-formatted MAF file for user-provided alignment file.
13. ``unaligned_length_ecdf`` – Length distribution of unaligned reads