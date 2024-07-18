# Benchmark

## Systems

### 1. Skyrmion

Pd/Fe bilayers on fcc Ir(111), we take the exchange and DMI parameters according Malottki et al. ["Enhanced skyrmion stability due to exchange frustration"](https://www.nature.com/articles/s41598-017-12525-x).

For the lattice constant we choose 3.839 Å (the value from bulk Iridium).

Differently from Malottki et al., we also explicitly simulate the dipole-dipole interactions.
Therefore, we have two configuration files one without explicit dipole-dipole interactions (`cfg_files/pdfe_fcc_skyrmion_no_ddi.cfg`) and one with them (`cfg_files/pdfe_fcc_skyrmion_with_ddi.cfg`).

The system contains $256^2$ spins.

### 2. Hopfion

A hopfion in a bulk magnet with competing exchange interactions.
The system is simple cubic and contains $64^3$ spins with four shells of exchange interactions.
See Rybakov et al. ["Magentic Hopfions in solids"](https://pubs.aip.org/aip/apm/article/10/11/111113/2835168/Magnetic-hopfions-in-solids).

## The benchmark

1. LLG: tests energy minimization of an initial configuration with the VP solver.
   The number of iterations and the convergence criterion for are set in the corresponding `.cfg` files under the keywords `llg_n_iterations` and `llg_force_convergence` respectively.

For now `n_iterations` has been set to 1000 for all benchmarks, therefore it is expected that the force does not fully converge.

## Running the benchmarks

See the `./run_benchmarks.sh` script.
Outputs are written to `benchmark_<...>.txt` files.
