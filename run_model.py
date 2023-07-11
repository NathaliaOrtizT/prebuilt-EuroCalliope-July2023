#!/usr/bin/env python3
# -_- coding: utf-8 -_-


import calliope
import create_input
import run
import matplotlib

path_to_model_yaml = '../2050/model/national/model-2018.yaml'
scenarios_string = "industry_fuel,transport,heat,config_overrides,link_cap_dynamic,freeze-hydro-capacities,res_2h,add-biofuel,H2_grid,salt_caverns,electrolysis_limit_3500,H2_imports" 
path_to_netcdf_of_models_inputs = '../2050/national/inputs.nc'

model_input = create_input.build_model(path_to_model_yaml, scenarios_string, path_to_netcdf_of_models_inputs)


path_to_netcdf_of_results = '../Results/test_results.nc'
run.run_model(path_to_netcdf_of_models_inputs, path_to_netcdf_of_results)


# model = calliope.read_netcdf('../Results/test_results.nc')
# model.plot.summary(to_file='./summary.html')


