input_sk_with_ddi=./cfg_files/pdfe_fcc_skyrmion_with_ddi.cfg
input_sk_no_ddi=./cfg_files/pdfe_fcc_skyrmion_no_ddi.cfg
input_hopfion=./cfg_files/hopfion.cfg

initial_image_sk=./input_configurations/initial_configuration_skyrmion.ovf
initial_image_hopf=./input_configurations/initial_configuration_hopfion.ovf

python3 run_llg.py $input_sk_with_ddi $initial_image_sk ./benchmark_sk_with_ddi.txt
python3 run_llg.py $input_sk_no_ddi $initial_image_sk ./benchmark_sk_no_ddi.txt
python3 run_llg.py $input_hopfion $initial_image_hopf ./benchmark_hop.txt
