# -*- coding: utf-8 -*-
PROCESS_DICT = {}

# Import the process_definitions to fill the process.PROCESS_DICT with process_definitions
from graas_openeo_core_wrapper.process_definitions.filter_bbox_process import FilterBBoxProcess
from graas_openeo_core_wrapper.process_definitions.filter_daterange_process import FilterDataRangeProcess
from graas_openeo_core_wrapper.process_definitions.ndvi_process import SimpleNDVIProcess

